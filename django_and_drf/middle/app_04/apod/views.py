
from django.shortcuts import render
from django.conf import settings
import requests
import json


def apod(request):
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key='+settings.NASA_API_KEY)
    loaded_json = json.loads(response.text)

    daily_image = loaded_json.get('url')
    title = loaded_json.get('title')
    explanation = loaded_json.get('explanation')
    date = loaded_json.get('date')
    owner = loaded_json.get('copyright')

    context = {
        'daily_image': daily_image,
        'title':title,
        'explanation':explanation,
        'date':date,
        'owner':owner
    }

    return render(request, "apod.html", context)
