import requests
import datetime as dt


# USERNAME ="rohit837248"
# TOKEN = "hka9yruueorujalk"
USERNAME ="rohit85"
TOKEN = "hka99038iofaja03"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN,
}

# #create a username and password
#
# pixela_params ={
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor":"yes",
# }
#
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)


# #create a new graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name" : "Coding",
#     "unit":"Minutes",
#     "type":"float",
#     "color":"ichou",
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)



# #upade the graph
# graphId_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# graphId_update ={
#     # "name": "Coding Graph",
#     "unit":"Hours",
# }
# response = requests.put(url=graphId_endpoint, json=graphId_update, headers=headers)

#add a pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.datetime.now()
date = today.strftime("%Y%m%d")

add_a_pixel ={
    "date":f"{date}",
    "quantity":input("How many hours you code today?: ")
}
response = requests.post(url=pixel_creation_endpoint, json=add_a_pixel, headers=headers)

# #update a pixel
# update_a_pixel ={
#     "quantity": "300"
# }
# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# response = requests.put(url=pixel_endpoint, json=update_a_pixel, headers=headers)


## delete a pixel
# response = requests.delete(url=pixel_endpoint, headers=headers)
print(response.text)
