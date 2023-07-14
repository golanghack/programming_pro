from requests import get

base_url = 'http://127.0.0.1:8000/api/'

req = get(f'{base_url}/courses/')
courses = req.json()

available_courses = ', '.join([course['title'] for course in courses])
print(f'All courses -> {available_courses}')