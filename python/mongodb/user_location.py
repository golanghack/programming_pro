import bson

location = bson.SON()
x = 2
y = 2
location['x'] = x
location['y'] = y 

user_doc_location = {
    "username": "one",
    "user_loc": [x, y]
}
