from random import random

import requests

ip_addresses = ["mysuperproxy.com:5000", "mysuperproxy.com:5001", "mysuperproxy.com:5100", "mysuperproxy.com:5010",
                "mysuperproxy.com:5050", "mysuperproxy.com:8080", "mysuperproxy.com:8001",
                "mysuperproxy.com:8000", "mysuperproxy.com:8050"]


def proxy_request(request_type, url, **kwargs):
    while True:
        try:
            proxy = random.randint(0, len(ip_addresses) - 1)
            proxies = {"http": ip_addresses(proxy), "https": ip_addresses(proxy)}
            response = requests.get(request_type, url, proxies=proxies, timeout=5, **kwargs)
            print(f"Proxy currently being used: {proxy['https']}")
            break
        except:
            print("Error, looking for another proxy")
    return response
