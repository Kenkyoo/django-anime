from django.shortcuts import render
import requests

def index(request):
    try:
        response = requests.get('https://api.jikan.moe/v4/top/anime')
        response.raise_for_status()
        data = response.json()
        
        animes = data.get('data', [])[:12]  # 12 animes para grid de 3 o 4 columnas
        
        anime_list = []
        for anime in animes:
            anime_list.append({
                'title': anime.get('title', 'Sin título'),
                'synopsis': anime.get('synopsis', 'Sin sinopsis disponible'),
                'image': anime.get('images', {}).get('jpg', {}).get('image_url', ''),
                'year': anime.get('year', 'N/A'),
                'score': anime.get('score', 'N/A'),
                'episodes': anime.get('episodes', 'N/A'),
                'mal_id': anime.get('mal_id', ''),
                'type': anime.get('type', 'N/A'),
            })
        
        return render(request, 'index.html', {
            'anime_list': anime_list,
            'total_results': data.get('pagination', {}).get('items', {}).get('total', 0)
        })
    except requests.exceptions.RequestException as e:
        return render(request, 'index.html', {'error': f'Error al conectar con la API: {str(e)}'})