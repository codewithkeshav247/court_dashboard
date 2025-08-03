from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def scrape_case_data(case_type, case_number, year):
    try:
        # Set up Selenium with local chromedriver
        driver = webdriver.Chrome(service=Service("chromedriver.exe"))

        # Visit eCourt India portal
        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")

        time.sleep(5)  # Let the page load

        # ✅ STOP HERE: CAPTCHA appears on next step, so we stop automation
        print("CAPTCHA appears — scraping blocked. Returning simulated data.")

    except Exception as e:
        print("Error:", str(e))

    finally:
        driver.quit()

    # Fallback simulated response
    return {
        "parties": "Rajesh Kumar vs State of Haryana",
        "filing_date": "15-Feb-2021",
        "next_hearing": "12-Aug-2025",
        "pdf_link": "https://districts.ecourts.gov.in/faridabad/orders/order321.pdf"
    }