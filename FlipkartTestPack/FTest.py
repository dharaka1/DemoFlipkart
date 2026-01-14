import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys



@pytest.fixture()
def test_setup():
    driver=webdriver.Chrome()
    yield driver

def test_Test_flow(test_setup):
    driver=test_setup
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    Search_product = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@title='Search for Products, Brands and More']")))
    Search_product.send_keys("Samsung Galaxy latest mobile", Keys.ENTER)
    driver.save_screenshot("Search_product.png")
    Scroll_Into_Product = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Samsung Galaxy F06 5G (Bahama Blue, 64 GB)']")))
    driver.execute_script("arguments[0].scrollIntoView();", Scroll_Into_Product)
    driver.save_screenshot("Scroll_Into_Product.png")
    Click_Into_Product = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Samsung Galaxy A55 5G (Awesome Navy, 128 GB)']")))
    Click_Into_Product.click()
    Original_Window = driver.window_handles
    driver.switch_to.window(Original_Window[1])
    driver.save_screenshot("Click_Into_Product.png")
    Scroll_Into_cart = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Delivery']")))
    driver.execute_script("arguments[0].scrollIntoView();", Scroll_Into_cart)
    Click_Into_cart = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Add to cart']")))
    Click_Into_cart.click()
    driver.save_screenshot("Click_Into_cart.png")
    Add_item = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Add Item']")))
    Add_item.click()
    driver.save_screenshot("Add_item.png")
    time.sleep(10)
    driver.quit()

