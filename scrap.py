#scraping dat
import urllib.request
import time

def download_site(url):
    with urllib.request.urlopen(url) as response:
        print(f"Stiahnutie {url}: {len(response.read())} bytov")

sites = [
    "http://www.example.com",
    "http://www.example.org",
    "http://www.example.net",
    "https://en.wikipedia.org/wiki/Pok%C3%A9mon",
]

smart_time = time.time()
for site in sites:
    download_site(site)

duration = time.time() - smart_time
print(f"Stiahnute {len(sites)} za {duration} sekund")

