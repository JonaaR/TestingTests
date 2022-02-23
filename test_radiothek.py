import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search_query = "Nachmittag"

@pytest.fixture(scope="module")
def chrome_driver():
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    website = "https://radiothek.orf.at/search"
    driver.get(website)
    expectation = EC.presence_of_element_located((By.CSS_SELECTOR, "#didomi-notice-agree-button"))
    accept_cookie = WebDriverWait(driver, 5).until(expectation)
    accept_cookie.click()
    time.sleep(2)
    yield driver
    driver.quit()


def test_smooth(chrome_driver):
    search_start = chrome_driver.find_element(By.CSS_SELECTOR, 'input[type=search]')
    search_button = chrome_driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    search_start.send_keys(search_query)
    search_button.click()
    result_is_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.search-has-query h2'))
    result_X = WebDriverWait(chrome_driver, 5).until(result_is_present)

    assert result_X.text == f'Suchergebnis für "{ search_query }"'



def test_fancy( chrome_driver ):
    results = chrome_driver.find_elements( By.XPATH, '//span[@class="type"]' )
    dictionary_results = {}
    for e in results:
        if e.text in dictionary_results:
            dictionary_results[e.text] += 1
        else:
            dictionary_results[e.text] = 1
        assert len(dictionary_results) >= 1

