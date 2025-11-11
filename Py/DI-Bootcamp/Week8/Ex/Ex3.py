# scrape_accuweather.py
# Scrape weather data from AccuWeather, extract temperature / condition / humidity,
# then analyze: average temperature & most common condition.

import time
import re
from collections import Counter
import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://www.accuweather.com/en/us/attica/30607/weather-forecast/2139413"


# ----------------------------- SELENIUM SETUP -----------------------------------
def setup_driver(headless=True):
    opts = webdriver.ChromeOptions()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1400,1200")
    opts.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
    )
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts
    )
    return driver


def wait_for_forecast(driver, timeout=20):
    selectors = [
        "article",                       # many forecast items are inside <article>
        "[data-qa='daily']",             # daily cards
        "[class*='DailyForecast']",      # daily forecast blocks
    ]
    for sel in selectors:
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, sel))
            )
            return sel
        except:
            pass
    raise RuntimeError("Could not find forecast cards — structure changed")


# -------------------------- PARSING HELPERS -------------------------------------
TEMP_RE = re.compile(r"(-?\d+)\s*°")
HUM_RE = re.compile(r"Humidity:? (\d+)%", re.I)
COND_WORDS = [
    "Sunny", "Cloudy", "Partly", "Mostly", "Clear", "Rain", "Showers",
    "Storm", "Thunder", "Snow", "Overcast", "Fog", "Haze", "Drizzle", "Wind"
]


def extract_condition(text):
    hits = [w for w in COND_WORDS if w.lower() in text.lower()]
    return hits[0] if hits else None


# -------------------------- MAIN PARSER -----------------------------------------
def parse_weather(html: str) -> pd.DataFrame:
    soup = BeautifulSoup(html, "lxml")

    cards = soup.select("article")
    rows = []

    for c in cards:
        block = " ".join(c.stripped_strings)

        # Temperature
        temps = TEMP_RE.findall(block)
        temp_val = None
        if len(temps) >= 2:
            temp_val = (int(temps[0]) + int(temps[1])) / 2
        elif len(temps) == 1:
            temp_val = int(temps[0])

        # Humidity
        hum = None
        m = HUM_RE.search(block)
        if m:
            hum = int(m.group(1))

        # Condition
        cond = extract_condition(block)

        if temp_val is not None or hum is not None or cond:
            rows.append({
                "temp": temp_val,
                "humidity": hum,
                "condition": cond or "Unknown"
            })

    return pd.DataFrame(rows).drop_duplicates().reset_index(drop=True)


# -------------------------- MAIN FUNCTION ---------------------------------------
def main():
    driver = setup_driver(headless=True)
    try:
        driver.get(URL)
        wait_for_forecast(driver)
        time.sleep(2)
        html = driver.page_source
    finally:
        driver.quit()

    df = parse_weather(html)

    if df.empty:
        print("⚠ No data parsed. Page structure may have changed.")
        return

    # Analysis
    avg_temp = df["temp"].dropna().mean() if df["temp"].notna().any() else None
    most_common_condition = Counter(df["condition"]).most_common(1)[0][0]

    print("\nParsed Forecast Data:")
    print(df.head(20))
    print("\n==============================")
    print(f"Average Temperature: {avg_temp:.1f}°F" if avg_temp else "Average Temp: N/A")
    print(f"Most Common Condition: {most_common_condition}")
    print("==============================\n")

    df.to_csv("accuweather_forecast.csv", index=False)
    print("Saved: accuweather_forecast.csv")


if __name__ == "__main__":
    main()