import requests

url = "https://maps.googleapis.com/maps/api/geocode/json?"

parameters = {
    "address":"coding blocks piatmpura",
    "key":"AIzaSyAjbPOrGWgy6Phep5WvcBQrIo_l8bO5f44"
}

r = requests.get(url,params = parameters)

print(r.url)

print(r.content)

