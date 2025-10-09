import requests

url = "https://catfact.ninja/facts"
params = {"limit": 3, "max_length": 120}  # these are the documented params

resp = requests.get(url, params=params, timeout=8)
resp.raise_for_status()
data = resp.json()

print("Final URL:", resp.url)
print("Keys at top level:", list(data.keys()))
for i, fact in enumerate(data["data"], 1):
    print(f"{i}.", fact["fact"])
