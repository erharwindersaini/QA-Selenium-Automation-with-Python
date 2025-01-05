# Selenium Table Search Test using Pytest

## Features
- Uses **pytest** framework to structure test cases.
- Automates browser interactions like opening a website, entering text, and validating search results.
- Executes tests with modularity using **pytest fixtures**.
- Manages WebDriver automatically using **webdriver-manager**.

---

## Prerequisites
- **Python Version:** 3.12.5  
- **Browser:** Google Chrome (latest version)  
- **Internet Connection:** Required for accessing the test website.  

---

## Installation

### Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
pip install -r requirements.txt
pytest -v qa_selenium_test.py
