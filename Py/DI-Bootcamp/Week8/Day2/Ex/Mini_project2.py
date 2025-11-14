"""
scrape_bbc_weather.py

Scrapes daily weather forecast data from BBC Weather for location 293397
and saves it as a CSV file.
"""

import time
import pandas as pd
from bs4 import BeautifulSoup

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.bbc.com/weather/293397"


def create_driver(headless: bool = True):
    """Create and return a Chrome WebDriver instance."""
    chromedriver_autoinstaller.install()

    options = webdriver.ChromeOptions()
    if headless:
        # New headless mode for recent Chrome versions
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    return driver


def accept_cookies_if_needed(driver, timeout: int = 10):
    """
    Some pages show a cookies popup; this tries to accept or close it.
    If nothing appears, it just continues.
    """
    try:
        # You may need to adjust selectors depending on how BBC shows the banner
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "button[aria-label*='Accept'],"  # generic guess
                )
            )
        )
        buttons = driver.find_elements(
            By.CSS_SELECTOR,
            "button[aria-label*='Accept'], button:contains('Agree')"
        )
        if buttons:
            buttons[0].click()
            time.sleep(1)
    except Exception:
        # No cookies dialog – ignore
        pass


def scrape_bbc_weather():
    driver = create_driver(headless=True)

    try:
        driver.get(URL)

        # Optional: accept cookies if present
        accept_cookies_if_needed(driver)

        # Wait until daily forecast section is loaded
        # You might need to tweak the selector if the HTML changes
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='daily-summary'], .wr-day")
            )
        )

        # Let JS finish rendering (a little buffer)
        time.sleep(2)

        html = driver.page_source

    finally:
        driver.quit()

    # Parse with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    rows = []

    # --- APPROACH 1: using data-testid attributes (more modern BBC markup) ---
    daily_cards = soup.select("[data-testid='daily-summary']")
    if not daily_cards:
        # --- APPROACH 2: fallback to older class names ---
        daily_cards = soup.select(".wr-day")

    for card in daily_cards:
        # You may need to inspect the real HTML in DevTools and adjust these
        # selectors (they are written to be easy to adapt).

        # Day name (e.g. "Fri")
        day_name_el = card.select_one("[data-testid='day'], .wr-date__long")
        # Date text (e.g. "14 Nov")
        date_el = card.select_one("[data-testid='date'], .wr-date__long")
        # Max / min temperature
        max_temp_el = card.select_one(
            "[data-testid='maximum-temperature'] span, .wr-day-temperature__high-value span"
        )
        min_temp_el = card.select_one(
            "[data-testid='minimum-temperature'] span, .wr-day-temperature__low-value span"
        )
        # Weather description (e.g. "Light rain", "Sunny")
        desc_el = card.select_one(
            "[data-testid='description'], .wr-day__weather-type-description"
        )
        # Precipitation chance (e.g. "40%")
        precip_el = card.select_one(
            "[data-testid='precipitation'] span, .wr-u-font-weight-500 span"
        )

        def clean_temp(el):
            if el and el.get_text(strip=True):
                text = el.get_text(strip=True)
                text = text.replace("°", "").replace("C", "").strip()
                try:
                    return int(text)
                except ValueError:
                    return None
            return None

        def clean_percent(el):
            if el and el.get_text(strip=True):
                text = el.get_text(strip=True).replace("%", "").strip()
                try:
                    return int(text)
                except ValueError:
                    return None
            return None

        row = {
            "day_name": day_name_el.get_text(strip=True) if day_name_el else None,
            "date_str": date_el.get_text(strip=True) if date_el else None,
            "max_temp_c": clean_temp(max_temp_el),
            "min_temp_c": clean_temp(min_temp_el),
            "description": desc_el.get_text(strip=True) if desc_el else None,
            "precip_percent": clean_percent(precip_el),
        }

        rows.append(row)

    df = pd.DataFrame(rows)

    # To make date usable, we’ll keep date_str here and parse it later in analysis
    output_file = "bbc_weather_293397_daily.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved {len(df)} rows to {output_file}")


if __name__ == "__main__":
    scrape_bbc_weather()