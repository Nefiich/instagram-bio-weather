import requests
import json

url = "https://instagram.com/accounts/edit"

headers = {
    "authority" : "instagram.com",
    "accept" : "*/*",
    "accept-encoding" : "gzip, deflate, br",
    "accept-language" :  "en-US,en;q=0.9,bs;q=0.8,de-DE;q=0.7,de;q=0.6,la;q=0.5",
    "content-length" : "207",
    "cookie" : "ig_did=7269F6BB-E296-45A9-9834-DE78E581613E; mid=XrRqzAALAAEKRUJvozu3JxXlxiEE; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=512037925; shbid=610; ig_direct_region_hint=ATN; csrftoken=XdgJ7BFUfqZYJpAkZujRRoPTpu9LVpz9; sessionid=512037925%3AU2BoUX73YZeQy5%3A11; rur=ASH; shbts=1596667221.5818622; urlgen='{\"77.78.252.202\": 42560}:1k3S66:4vFe1rlKHRW4vA8y-YYnTQTDaqA\"",
    "origin" : "https://www.instagram.com",
    "referer" : "https://www.instagram.com/accounts/edit",
    "sec-fetch.dest" : "empty",
    "sec-fetch-mode" : "cors",
    "sec-fetch-site" : "same-origin",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "x-csrftoken" : "XdgJ7BFUfqZYJpAkZujRRoPTpu9LVpz9",
    "x-ig-app-id" : "936619743392459",
    "x-ig-www-claim" : "hmac.AR1BdlVdWjqLrKS1QGow5wbMb0mkd4c4FJ09TJ-17WuvcUZP",
    "x-instagram-ajax" : "03fe5521a722",
    "x-requested-with" : "XMLHttpRequest",
}
body = {
    "first_name" : "Nefi%C4%87+%7C+4.",
    "email" : "gd.nefic%40gmail.com",
    "username" : "nefiich",
    "phone_number" : "%2B387+61+667+477",
    "biography" : "temperature+in+breza+%3A+16.25%C2%B0%0A-+Software+Developer",
    "external_url" : "",
    "chaining_enabled" : "on"
}
r = requests.post(url, data=body, headers=headers)
print(r)
print(r.status_code)