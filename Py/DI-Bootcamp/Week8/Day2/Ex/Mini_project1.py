import time
import csv
import logging

# Configure console-only logging early so steps can log as the script runs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import chromedriver_autoinstaller
from bs4 import BeautifulSoup


# -----------------------------
# 1. Initialize Selenium WebDriver
# -----------------------------
chromedriver_autoinstaller.install()  # installs matching ChromeDriver if needed
logger.info("Chromedriver install checked/installed")

chrome_options = Options()
# comment this line if you want to see the browser window
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
logger.info("Chrome WebDriver started (headless=%s)", "--headless=new" in chrome_options.arguments)

try:
    # -----------------------------
    # 2. Load the Web Page
    # -----------------------------
    url = "https://www.inmotionhosting.com/"
    driver.get(url)
    logger.info("Requested URL: %s", url)

    # Wait until some dynamic content is loaded (e.g. the "Compare Our Hosting Plans" block)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Shared Hosting')]"))
    )

    # Give a tiny extra delay just in case JS continues rendering
    time.sleep(2)
    logger.info("Waited 2s for additional rendering")

    # -----------------------------
    # 3. Parse the page with BeautifulSoup
    # -----------------------------
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    logger.info("Page parsed with BeautifulSoup (html length=%d)", len(html))

    # We will scrape plan categories from the "Compare Our Hosting Plans" section:
    # Shared Hosting, Hosting for WordPress, VPS Hosting, Dedicated Hosting
    TARGET_TITLES = {
        "Shared Hosting",
        "Hosting for WordPress",
        "VPS Hosting",
        "Dedicated Hosting",
    }

    plans_data = []

    # Find all h3 headings and filter by our target titles
    for h3 in soup.find_all("h3"):
        title_text = h3.get_text(strip=True)
        if title_text not in TARGET_TITLES:
            continue

        plan_category = title_text

        # 4. Identify elements that contain features and pricing
        # Features are listed right after the h3 as <ul><li>...</li>...</ul>
        features_ul = h3.find_next("ul")
        if features_ul:
            features = [li.get_text(strip=True) for li in features_ul.find_all("li")]
        else:
            features = []

        # "Starting at" + price is right after the features list
        # We'll search forward for the first "Starting at" text and the price line after it
        starting_at_el = features_ul.find_next(string=lambda s: s and "Starting at" in s) if features_ul else \
                         h3.find_next(string=lambda s: s and "Starting at" in s)

        starting_price = None
        renews_at = None

        if starting_at_el:
            # Price is usually the next text node containing something like "$3.19/mo"
            price_el = starting_at_el.find_next(string=lambda s: s and "$" in s)
            if price_el:
                starting_price = price_el.strip()

            # The renew price text contains "Renews at"
            renew_el = starting_at_el.find_next(string=lambda s: s and "Renews at" in s)
            if renew_el:
                renews_at = renew_el.strip()

        # -----------------------------
        # Save one "plan" row per category
        # (You could expand this to multiple price variants if you want)
        # -----------------------------
        plans_data.append({
            "plan_category": plan_category,
            "features": "; ".join(features),
            "starting_price": starting_price,
            "renews_at": renews_at,
        })
        logger.debug("Appended plan: %s (features=%d)", plan_category, len(features))

    # -----------------------------
    # 5. Store and Save the Data to CSV
    # -----------------------------
    csv_filename = "inmotion_plans.csv"
    fieldnames = ["plan_category", "features", "starting_price", "renews_at"]

    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(plans_data)

    logger.info("Scraped %d plan categories.", len(plans_data))
    for row in plans_data:
        logger.debug("Row: %s", row)
    logger.info("Data saved to %s", csv_filename)

finally:
    # -----------------------------
    # 6. Close Selenium WebDriver
    # -----------------------------
    driver.quit()