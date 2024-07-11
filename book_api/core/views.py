from django.shortcuts import render
import requests


def index(request):
    url = "https://open-library2.p.rapidapi.com/search_title/The%20Lord%20of%20the%20ring"

    headers = {
        "X-RapidAPI-Key": "7e86997538mshd664a4dc3f8a5a1p1cf982jsn54a75b2ae4ec",
        "X-RapidAPI-Host": "open-library2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers).json()

    context = {
        'response': response,
    }
    
    return render(request, 'core/index.html', context)
