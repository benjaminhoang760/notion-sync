import requests

url = "https://httpbin.org/get"
resp = requests.get(url)
print("status:", resp.status_code)
print("final URL:", resp.url)
print("content type:", resp.headers.get("content-type"))
print("first 120 chars", resp.text[:120]) 

