from requests import get

req = get('http://127.0.0.1:8000/api/courses/')

courses = req.json()

print(courses)