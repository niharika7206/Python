import requests

def check_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            print(f"{url} -> {response.status_code}")
        except:
            print(f"{url} -> Failed")

urls = [
    "https://google.com",
    "https://github.com",
    "https://invalidurl.test"
]

check_urls(urls)
