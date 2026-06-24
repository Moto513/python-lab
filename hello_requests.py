import requests

url = "https://httpbin.org/get"
params = {"name": "motokazu"}

try:
    response = requests.get(url, params=params, timeout=20)

    print("Final URL:", response.url)
    print("Status code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))

    if response.status_code == 200:
        print("Response JSON:")
        print(response.json())
    else:
        print("Response was not successful.")
        print(response.text[:500])

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.RequestException as e:
    print("Request failed:")
    print(e)