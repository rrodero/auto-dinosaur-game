from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def play_dino_game():
    driver = webdriver.Chrome()
    driver.get("chrome://dino")

    # Wait for the game to load and the dinosaur to appear
    runner_canvas = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.runner-canvas'))
    )