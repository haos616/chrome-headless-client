import base64

import requests

url = "https://google.com"

data = [
    {"method": "Page.goto", "params": {"url": url, "timeout": 0, "waitUntil": "networkidle0"}},
    {"method": "Page.captureScreenshot", "params": {"format": "png"}},
    # {
    #     "method": "Page.printToPDF",
    #     "params": {
    #         "printBackground": True,
    #         "marginTop": 0,
    #         "marginBottom": 0,
    #         "marginLeft": 0,
    #         "marginRight": 0,
    #     }
    # },
]

url = "http://chrome-headless-service:8000"

response = requests.post(url=url, json=data)
if response.status_code == 200:
    print(response.content)
    content = response.json()

    pdf_body = base64.b64decode(content[-1]["data"])

    with open("test.png", "wb") as file:
        file.write(pdf_body)
