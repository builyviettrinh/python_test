import os
import requests
from requests.auth import HTTPBasicAuth

# Create folder if not exist
image_folder = "images"
os.makedirs(image_folder, exist_ok=True)

url = ""
username = ""
password = ""
# Request get API
response = requests.get(url, auth=HTTPBasicAuth(username, password))

data = ""
if response.status_code == 200:
    data = response.json()
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)

# Loop data
if data['data']:
    for item in data['data']:
        image_url = item["image_url"]

        # Tải ảnh từ URL
        image_id = item["id"]
        image_path = os.path.join(image_folder, f"image_{image_id}.jpg")
        # response = requests.get(image_url, auth=HTTPBasicAuth(username, password))
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_path, "wb") as f:
                f.write(response.content)
            print(f"Đã tải ảnh {image_id} và lưu vào {image_path}")
        else:
            print(f"Lỗi khi tải ảnh {image_id}")

print("Hoàn tất tải ảnh.")
