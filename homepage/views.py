from django.shortcuts import render
import json
import requests as rq

# Create your views here.


def index(request):
    values = git()
    if not values is None:
        values = list(values)
        title = values[0]
        description = values[1]
        url = values[2]
        zipped = zip(title, description, url)
        length = len(title)
    return render(request, 'frontend/index.html', {'zipped': zipped, 'length': length})


def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load URL")


def load_json(data):
    if not data is None:
        j = json.loads(data)
        length = len(j)
        title = []
        url = []
        description = []
        for i in range(length):
            t = j[i]["name"]
            title.append(t)
            u = j[i]["html_url"]
            url.append(u)
            d = j[i]["description"]
            description.append(d)

        return title, description, url


def git():
    url = "https://api.github.com/users/ajanraj/repos"
    values = load_json(get_data(url))
    return values
