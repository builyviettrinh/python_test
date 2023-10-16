import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs

chromedriver_path = 'chromedriver.exe'

# input site info
url = ""
username = ""
password = ""

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


try:
    for x in range(172):
        print(x)
        driver.get(f"https://{username}:{password}@{url}")
        # Wait for the input element to be present
        input_age = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.NAME, "age"))
        )
        input_age.clear()
        time.sleep(1)

        if x > 85:
            x = x - 86
            input_age.send_keys(str(x))
            elements_btn = WebDriverWait(driver, 4).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".-male")))[0]
            elements_btn.click()
            gender_button = WebDriverWait(driver, 4).until(
                EC.presence_of_all_elements_located((By.NAME, "gender"))
            )
            gender_val = gender_button[0].get_attribute("value")
        else:
            input_age.send_keys(str(x))
            elements_btn = WebDriverWait(driver, 4).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".-female")))[0]
            elements_btn.click()
            gender_button = WebDriverWait(driver, 4).until(
                EC.presence_of_all_elements_located((By.NAME, "gender"))
            )
            gender_val = gender_button[1].get_attribute("value")

        time.sleep(1)
        submit_btn = WebDriverWait(driver, 4).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".searchbox__btn")))[0]
        submit_btn.click()
        time.sleep(1)
        share_btn = WebDriverWait(driver, 4).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".btn-share")))[0]
        share_url = share_btn.get_attribute("href")
        parsed_url = urlparse(share_url)
        query_params = parse_qs(parsed_url.query)

        if "incentive" in query_params:
            incentive_value = query_params["incentive"][0]
            time.sleep(1)
            screenshot_path = f"screenshots/{str(x)}_{'female' if (gender_val == '2') else 'male'}_{incentive_value}.png"
            # screenshot_path = f"screenshots/{incentive_value}.png"
            driver.save_screenshot(screenshot_path)
            print(f"Đã chụp màn hình và lưu vào {screenshot_path}")
        time.sleep(1)
except Exception as e:
    print("Unable to find the input element or an error occurred:", str(e))


# Close the browser window
driver.quit()
time.sleep(600)
