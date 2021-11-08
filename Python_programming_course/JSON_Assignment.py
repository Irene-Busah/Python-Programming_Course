import json
import urllib.request
import urllib.parse
count = 0

address = input("Enter the url: ")
url = urllib.request.urlopen(address)
info = url.read()
while True:
    if len(address) < 1:
        break

    print("Retrieving: ", address)
    print("Retrieved ", len(info), "characters")
    file = json.loads(info)
    for item in file["comments"]:
        Sum = int(item["count"])
        count = Sum + count
    print(count)
    break


# import urllib
# import urllib.request
# import json
# # http://py4e-data.dr-chuck.net/comments_1303037.json
# url = input("Enter location: ")
# address = urllib.request.urlopen(url)
# data = address.read()
#
# total = 0
#
# while True:
#     if len(url) < 1:
#         break
#
#     print("Retrieving: ", address)
#     print("Retrieved ", len(data), " characters")
#
#     info = json.loads(data)
#     info = info["comments"]
#     for item in info:
#         # print("Count: ", item["count"])
#         total += int(item["count"])
#         # print("Sum: ", total)
#     print("Final sum: ", total)
#     break
