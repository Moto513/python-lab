import requests

url = "https://httpbin.org/get"
response = requests.get(url, timeout=10)

print("Status code:", response.status_code)
print("Response JSON:")
print(response.json())