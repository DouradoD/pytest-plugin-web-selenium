from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp_conditions

LOGO = (By.CSS_SELECTOR, '[id="navbar"] img[class="navbar-logo-img"]')
INPUT_SEARCH_FIELD = (By.XPATH, '//input[@id="search-text"]')
BTN_SEARCH = (By.CSS_SELECTOR, 'button[id="search-lens-btn"]')
TXT_SEARCH_QUERY = (By.ID, 'search-query-label')


def test_web_search(driver):
    driver.get("https://www.selenium.dev/")
    driver.logger.info("This is an info message.")
    driver.wait.until(exp_conditions.visibility_of_element_located(LOGO))
    # Input the value in the Search input
    driver.wait.until(exp_conditions.visibility_of_element_located(INPUT_SEARCH_FIELD)).send_keys('Test')
    # Click on the search button
    driver.wait.until(exp_conditions.visibility_of_element_located(BTN_SEARCH)).click()
    # Check the result
    driver.wait.until(exp_conditions.visibility_of_element_located(TXT_SEARCH_QUERY))
