"""
Request Module is used to perform all kinds of http requests.
requests.get() this function will get the content of given
url into its parameter. As explained in example.
"""

import requests
# r = requests.get("https://www.youtube.com")
# print(r.text)
# print(r.status_code)
url = "https://www.facebook.com/cookies"
cookies = {"key1" : "Value1"}
data = {
    "email" : "subhanzaheer88@yahoo.com",
    "password" : "Muhammad.63"
}
r2 = requests.get(url= url, cookies= cookies)
print(r2)
print(r2.status_code)
print(r2.url)
# print(r2.text)
print(r2.cookies.values())
# print(r2.headers)
# print(r2.content)