import requests

name = "index.jpeg"
with open(name, "rb") as f:
    image = f.read()
files = {"file": image}
url = "http://46.191.128.15:8000/filetest"+f"?name={name}"
r = requests.post(url, files=files)
print(r, r.status_code, r.content)
