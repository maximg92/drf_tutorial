import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"




get_response = requests.post(endpoint, json={"content": "Hello wrld"})
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())