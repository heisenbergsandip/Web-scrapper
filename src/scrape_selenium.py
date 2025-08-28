# src/scrape_cpgrams_faq.py
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

PAGE = "https://pgportal.gov.in/Home/Faq"
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
os.makedirs(OUTPUT_PATH, exist_ok=True)

def create_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def parse_faq_block(block):
    question_tag = block.find("a", class_="text-primary")
    answer_tag = block.find("div", class_="card-body")
    if question_tag and answer_tag:
        question = question_tag.get_text(strip=True)
        answer = answer_tag.get_text(" ", strip=True)
        return {"question": question, "answer": answer}
    return None

def main():
    driver = create_driver(headless=False)
    driver.get(PAGE)

    # Wait for FAQ accordion to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "card-header"))
    )

    # Click each question to ensure answers are loaded (Bootstrap collapses)
    questions = driver.find_elements(By.CLASS_NAME, "text-primary")
    for q in questions:
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", q)
            driver.execute_script("arguments[0].click();", q)
            time.sleep(0.3)
        except:
            continue

    # Parse the page
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    faq_blocks = soup.find_all("div", class_="card card-light mt-2")

    results = []
    for block in faq_blocks:
        item = parse_faq_block(block)
        if item:
            results.append(item)

    driver.quit()

    if results:
        df = pd.DataFrame(results)
        df.drop_duplicates(inplace=True)
        output_file = os.path.join(OUTPUT_PATH, "hellosarkar_faq.csv")
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Saved {len(df)} FAQs to {output_file}")
    else:
        print("No FAQs found.")

if __name__ == "__main__":
    main()
