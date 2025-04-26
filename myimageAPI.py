import requests #interact with API-host+get request.http request
from PIL import Image
from io import BytesIO

api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjQyM2NlMGQ0ZTUyMWQ3NmRiYzk4MGNiMjI3ZGYwNTFjIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDQtMjNUMDI6MzM6MDUuMTEwOTQ5In0.KKRZaeaOylg_ibTm8WFK3ExxycocBjwBDYpR_z6YLHc" 
# paste your api token inside the double quote

user_input = input("Enter a description for the image: ")
url = "https://api.monsterapi.ai/v1/generate/txt2img"
headers = {"Authorization": f"Bearer {api_token}"}
response = requests.post(url, json={"prompt": user_input, "safe_filter": True}, headers=headers)

if response.status_code == 200: #tracking order
    print("Loading... The image may take a few seconds.")
    process_id = response.json().get("process_id")

    while True:
        status_data = requests.get(f"https://api.monsterapi.ai/v1/status/{process_id}").json()
        status = status_data.get("status")
        # print(status_data)

        if status == "COMPLETED":
            image_url = status_data['result']['output'][0]
            img = Image.open(BytesIO(requests.get(image_url).content)).show()
            break
        elif status == "FAILED":
            print("Image generation failed.")
            break
else:
    print(f"Error: {response.status_code}")