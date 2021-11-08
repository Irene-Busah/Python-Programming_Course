
import json
import urllib.parse
import urllib.request

api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"
# http://py4e-data.dr-chuck.net/json?
while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break
    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key

    url = serviceurl + urllib.parse.urlencode({"key": api_key, "address": address})
    print("retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print("retrieved", len(data), "characters")
    try:
        js = json.loads(str(data))
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print("=== failure to retrieve ===")
        print(data)
        continue

    print(json.dumps(js, indent=4))

    place_id = js["results"][0]["place_id"]
    print("PLACE ID: ", place_id)
