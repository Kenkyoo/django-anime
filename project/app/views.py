from django.shortcuts import render
import requests

def index(request):
    response = requests.get('https://api.jikan.moe/v4/top/anime')
    data = response.json()
    
    animes = data.get('data', [])[:12]

    anime_list = []
    for anime in animes:
        anime_list.append({
            'title': anime.get('title', 'Sin título'),
            'synopsis': anime.get('synopsis', 'Sin sinopsis'),
            'image': anime.get('images', {}).get('jpg', {}).get('image_url', ''),
            'year': anime.get('year', 'Sin año'),
            'score': anime.get('score', 'Sin puntuación'),
            'episodes': anime.get('episodes', 'Desconocido')
        })
    
    return render(request, 'index.html', {'anime_list': anime_list})