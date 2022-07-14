"""
Request Module is used to perform all kinds of http requests.
requests.get() this function will get the content of given
url into its parameter. As explained in example.
"""

import requests
# r = requests.get("https://www.youtube.com")
# print(r.text)
# print(r.status_code)
url = "https://www.facebook.com"
data = {
    "email" : "subhanzaheer2003@yahoo.com",
    "password" : "Muhammad.63"
}
r2 = requests.post(url= url, params= data)
print(r2)
print(r2.status_code)
print(r2.url)