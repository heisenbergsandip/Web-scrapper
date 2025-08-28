
---
# 📢 Government FAQ Web Scraper

This project contains **Python web scrapers** built with **Selenium** and **BeautifulSoup** to fetch FAQs from government portals. It automatically expands FAQ items and saves them to CSV for easy access and analysis.

---

## 🛠 Features

- **Dynamic Content Handling:** Automatically clicks questions to reveal answers on JS-driven pages.
- **Multiple Portals Supported:**  
  - Nepali FAQs: [gunaso.opmcm.gov.np/faqs](https://gunaso.opmcm.gov.np/faqs)  
  - Indian FAQs: [pgportal.gov.in/Home/Faq](https://pgportal.gov.in/Home/Faq)  
- **CSV Output:** Stores results in structured CSV files.
- **Duplicate Removal:** Ensures unique questions and answers.
- **Headless Mode:** Option to run scrapers without opening a browser window.

---

## 📂 Project Structure

```bash
web_scraper/
├── data/
│   └── hellosarkar_faq.csv   # Scraped FAQ CSV output
├── src/
│   ├── scrape_selenium.py     # Nepali FAQs scraper
│   └── __init__.py
│   └── utils.py
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
````

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/heisenbergsandip/Web-scrapper.git
cd Web_scraper
```

2. Create and activate a Python virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> Make sure to have **Python 3.10+** installed and Google Chrome browser.

---

## 📝 How to Run
 
```bash
python src/scrape_selenium.py
```

Scraped CSV files will be saved in the `data/` folder:

```
data/hellosarkar_faq.csv
```

---

## 🧩 Customization

* **Headless Mode:** Set `headless=True` in the scraper to run without opening a browser window.
* **Delay Adjustments:** Modify `time.sleep()` values to accommodate slower-loading pages.
* **Output Path:** Change `OUTPUT_PATH` in the script to store CSVs elsewhere.

---

## 📦 Requirements

```text
selenium
beautifulsoup4
pandas
lxml
webdriver-manager
```

---

## ⚡ How it Works

1. **Load Page:** Opens the target FAQ page using Selenium.
2. **Click Questions:** Iterates through FAQ items to reveal hidden answers.
3. **Parse HTML:** Uses BeautifulSoup to extract question and answer text.
4. **Save CSV:** Stores structured FAQs in `data/hellosarkar_faq.csv`.

---

## 📌 License

This project is open source under the **MIT License**.

 