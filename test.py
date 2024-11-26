import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name" : "Python Video 1","likes":50, "views": 1000},
        {"name" : "REST API Video 1","likes":80, "views": 100000},
        {"name" : "Fast API Video 1","likes":60, "views": 100}]



for i in range(len(data)):
    response =  requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)


#response = requests.put(BASE + "video/1", {"name" : "Tim","likes":30, "views": 10000})
#print(response.json())

input()

response = requests.get(BASE + "video/2")
print(response.json())