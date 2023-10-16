import os
import glob
import multiprocessing
import platform
import time
import random2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get info OS
system = platform.system()

chromedriver_path = ''
# For Windows
if system == "Windows":
    chromedriver_path = './chromedriver.exe'
# For macos
else:
    chromedriver_path = 'brew install chromedriver --cask'


def upload_image(image_path):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    url = ""
    try:
        driver.get(url)

        # Input name for image
        input_name = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.NAME, "user_name"))
        )
        input_name.clear()
        input_name.send_keys('text_' + str(random2.randint(0, 9)))
        time.sleep(1)
        # Click to checkbox
        checkbox = WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((By.NAME, "agree_checkbox")))[0]
        if checkbox:
            checkbox.click()
            time.sleep(1)

        # pass path to input file
        input_file = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.NAME, "upload_img"))
        )
        input_file.send_keys(image_path)
        time.sleep(5)

        print(f"Uploaded {image_path}")

    except Exception as e:
        print(f"Error uploading {image_path}: {e}")

    finally:
        driver.quit()


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_files = glob.glob(dir_path + '/upload/*')
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    pool.map(upload_image, image_files)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
