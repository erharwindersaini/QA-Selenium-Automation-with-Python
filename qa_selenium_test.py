import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def setup():
    """Setup WebDriver before tests and close it after tests."""
    # Initialize WebDriver options
    options = webdriver.ChromeOptions()

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver  # Provide the WebDriver instance to tests
    driver.quit()  # Teardown WebDriver


def test_open_website(setup):
    """Test if the website opens successfully."""
    setup.get('https://www.lambdatest.com/selenium-playground/table-sort-search-demo')
    assert "Selenium Grid Online | Run Selenium Test On Cloud" in setup.title, "Website failed to load properly."


def test_search_new_york(setup):
    """Test if searching 'New York' displays 5 entries."""
    # Locate the search box and input "New York"
    search_box = setup.find_element(By.XPATH, '//input[@type="search"]')
    search_box.send_keys('New York')

    # Wait for results to load
    setup.implicitly_wait(2)

    # Locate table rows
    rows = setup.find_elements(By.XPATH, '//table[@id="example"]/tbody/tr')

    # Validate the number of rows displayed
    assert len(rows) == 5, f"Expected 5 rows, but got {len(rows)}"

