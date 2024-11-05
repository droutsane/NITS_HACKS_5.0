import requests
url = 'https://nitshack.herokuapp.com/iot'
data = {
    "userID": "dsa321dsa",
    "timestamp": {
        "_seconds":1666389816,
        "_nanoseconds": 346000000
    },
    "weight":87.5,
    "dustbinID":"asd123asd",
    "composition": {
        "biodegradable":100,
        "nonbiodegradable": None
    },
    "location":{
        "_latitude": 0,
        "_longitude": 0
    }
}
response = requests.post(url, json=data)
print(data)
print(response)