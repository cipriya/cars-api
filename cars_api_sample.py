import requests

base_url = "https://cars-app.qxf2.com/cars"
username = "qxf2"
password = "qxf2"
response = requests.get(url=base_url + 'cars', auth=(username,password))

print(response.status_code)