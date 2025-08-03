# Court-Data Fetcher & Mini-Dashboard

## 🧾 Objective

Build a small web app that lets a user choose a Case Type and Case Number for a specific Indian court, then fetches and displays the case metadata and latest orders/judgments.

---

## ⚖ Court Chosen

*Faridabad District Court*  
🔗 https://districts.ecourts.gov.in/faridabad

---

## 📥 Functional Overview

### User Inputs:
- Case Type (e.g., CS)
- Case Number (e.g., 123)
- Filing Year (e.g., 2021)

### Parsed Data Displayed:
- Parties’ names
- Filing Date & Next Hearing Date
- Most Recent Order/Judgment PDF link

### Storage:
- Logs each query and raw response in *SQLite*

### Error Handling:
- Displays user-friendly messages for invalid case numbers or server downtime

---

## 🧠 CAPTCHA Strategy

Indian court websites use CAPTCHA and view-state tokens that block programmatic scraping.

We attempted automation using Selenium. However, due to CAPTCHA, real-time scraping was *not possible within the assignment scope*.  
Hence, the backend simulates the scraping logic using realistic placeholder values.

---

## 🛠 Tech Stack

- Python 3.x
- Flask (Web Framework)
- SQLite (Database)
- HTML/CSS (Frontend)
- BeautifulSoup (Simulated parsing)
- Selenium (used to test real court behavior)
- chromedriver.exe *(Download separately from [official site](https://chromedriver.chromium.org/downloads))*
---

## 🚀 Setup Steps

1. Clone or download this repo
2. Install dependencies:
```bash
pip install flask beautifulsoup4 selenium