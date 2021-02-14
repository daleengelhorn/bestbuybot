from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import info

RTX3080 = "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3080-aorus-master-10g-gddr6x-pci-express-4-0-graphics-card-black/6436223.p?skuId=6436223"

options = webdriver.ChromeOptions()
driver= webdriver.Chrome()
driver.maximize_window()
driver.get(RTX3080);
complete = False

while not complete:
    try:
        atcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue
    
    try:
        atcBtn.click()
        driver.get("https://www.com/bestbuy.com/cart")

        checkoutBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-buttons__checkout"))
        ) 
        checkoutBtn.click()

        emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailField.send_keys(info.email)

        passwordField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        passwordField.send_keys(info.password)
        
        signInBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cia-form__controls"))
        )
        signInBtn.click()

        cvvField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        )
        cvvField.send_keys(info.cvv)

        placeOrderBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
        )
        placeOrderBtn.click()
        
        complete = True
    except:
        driver.get(RTX3080)
        print("Error - restarting")
        continue

print("COPPED, GG")

