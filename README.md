# 🎬 Anime Explorer

![Django](https://img.shields.io/badge/Django-4.2-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Bulma](https://img.shields.io/badge/Bulma-1.0.2-00d1b2?style=for-the-badge&logo=bulma)
![Jikan API](https://img.shields.io/badge/Jikan_API-v4-red?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/tu-usuario/anime-explorer)
![GitHub stars](https://img.shields.io/github/stars/tu-usuario/anime-explorer?style=social)

> Una aplicación web simple construida con Django que consume la API de Jikan (MyAnimeList) para mostrar los animes más populares con un diseño moderno usando Bulma CSS.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [API Reference](#-api-reference)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

## ✨ Características

- ✅ Consumo de la API pública de [Jikan](https://jikan.moe/) (MyAnimeList)
- ✅ Diseño responsivo con **Bulma CSS**
- ✅ Grid de animes con información detallada
- ✅ Tarjetas interactivas con efecto hover
- ✅ Badges de puntuación, año, tipo y episodios
- ✅ Manejo de errores y estados de carga
- ✅ Interfaz moderna y limpia
- ✅ Optimizado para dispositivos móviles

## 🛠️ Tecnologías

### Backend

- **[Django 4.2](https://www.djangoproject.com/)** - Framework web Python
- **[Requests](https://docs.python-requests.org/)** - Cliente HTTP para consumir la API

### Frontend

- **[Bulma CSS 1.0.2](https://bulma.io/)** - Framework CSS moderno
- **[Font Awesome 6](https://fontawesome.com/)** - Iconos vectoriales

### API

- **[Jikan API v4](https://docs.api.jikan.moe/)** - API no oficial de MyAnimeList

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional)

### Pasos de instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu-usuario/anime-explorer.git
cd anime-explorer
```

2. **Crear y activar un entorno virtual**

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Realizar migraciones**

```bash
python manage.py migrate
```

5. **Ejecutar el servidor**

```bash
python manage.py runserver
```

6. **Abrir el navegador**

```
http://localhost:8000
```

## ⚙️ Configuración

### Variables de Entorno (Opcional)

Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-secret-key-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Personalización

Modifica la cantidad de animes mostrados en `views.py`:

```python
animes = data.get('data', [])[:12]  # Cambia 12 por el número deseado
```

## 🚀 Uso

### Funcionalidades

- **Ver animes**: Visualiza el top de animes en tarjetas
- **Información**: Título, sinopsis, puntuación, año, tipo y episodios
- **Enlace externo**: Botón para ver más detalles en MyAnimeList

### Endpoints

| URL       | Descripción                           |
| --------- | ------------------------------------- |
| `/`       | Página principal con el top de animes |
| `/admin/` | Panel de administración de Django     |

## 📂 Estructura del Proyecto

```
anime-explorer/
├── anime_explorer/          # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                    # Aplicación principal
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static/
│   ├── css/
│   │   └── custom.css
│   └── images/
├── requirements.txt
├── manage.py
├── .gitignore
└── README.md
```

### Archivos principales

#### `views.py`

```python
from django.shortcuts import render
import requests

def index(request):
    response = requests.get('https://api.jikan.moe/v4/top/anime')
    data = response.json()

    animes = data.get('data', [])[:12]
    anime_list = []
    for anime in animes:
        anime_list.append({
            'title': anime.get('title'),
            'synopsis': anime.get('synopsis'),
            'image': anime.get('images', {}).get('jpg', {}).get('image_url'),
            'year': anime.get('year'),
            'score': anime.get('score'),
            'episodes': anime.get('episodes'),
            'mal_id': anime.get('mal_id'),
            'type': anime.get('type'),
        })

    return render(request, 'index.html', {'anime_list': anime_list})
```

#### `index.html`

```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Top Anime</title>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
    />
    <link rel="stylesheet" href="{% static 'css/custom.css' %}" />
  </head>
  <body>
    <section class="hero is-primary is-medium">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title is-1"><i class="fas fa-film"></i> Top Anime</h1>
          <p class="subtitle">Los mejores animes según MyAnimeList</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        {% if error %}
        <div class="notification is-danger is-light">
          <button class="delete"></button>
          <strong>Error:</strong> {{ error }}
        </div>
        {% endif %}

        <div class="columns is-multiline is-desktop">
          {% for anime in anime_list %}
          <div class="column is-3-desktop is-4-tablet is-6-mobile">
            <div class="card anime-card">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img
                    src="{{ anime.image }}"
                    alt="{{ anime.title }}"
                    loading="lazy"
                  />
                </figure>
                <div class="anime-score">
                  <i class="fas fa-star"></i> {{ anime.score }}
                </div>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-content">
                    <p class="title is-6">{{ anime.title|truncatechars:35 }}</p>
                    <div class="tags">
                      <span class="tag is-info is-light">
                        <i class="fas fa-calendar"></i> {{ anime.year }}
                      </span>
                      <span class="tag is-success is-light">
                        <i class="fas fa-play-circle"></i> {{ anime.type }}
                      </span>
                      <span class="tag is-warning is-light">
                        <i class="fas fa-video"></i> {{ anime.episodes }} eps
                      </span>
                    </div>
                  </div>
                </div>
                <div class="content">
                  <p class="synopsis-text">
                    {{ anime.synopsis|truncatechars:150 }}
                  </p>
                </div>
                <div class="buttons is-centered mt-3">
                  <a
                    href="https://myanimelist.net/anime/{{ anime.mal_id }}"
                    target="_blank"
                    class="button is-small is-primary is-outlined"
                  >
                    <i class="fas fa-external-link-alt"></i> Ver más
                  </a>
                </div>
              </div>
            </div>
          </div>
          {% empty %}
          <div class="column is-full">
            <div class="notification is-warning is-light">
              No se encontraron animes disponibles
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </section>

    <footer class="footer has-background-light">
      <div class="content has-text-centered">
        <p>
          <strong>Anime Explorer</strong> con
          <i class="fas fa-heart has-text-danger"></i> y
          <a href="https://bulma.io" target="_blank">Bulma</a>
        </p>
      </div>
    </footer>

    <script>
      document.addEventListener("DOMContentLoaded", function () {
        (document.querySelectorAll(".notification .delete") || []).forEach(
          ($delete) => {
            const $notification = $delete.parentNode;
            $delete.addEventListener("click", () => {
              $notification.parentNode.removeChild($notification);
            });
          },
        );
      });
    </script>
  </body>
</html>
```

#### `custom.css`

```css
.anime-card {
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
  height: 100%;
}
.anime-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}
.anime-card .card-image {
  position: relative;
  overflow: hidden;
}
.anime-card .card-image img {
  height: 350px;
  object-fit: cover;
}
.anime-score {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.8);
  color: #ffd700;
  padding: 5px 12px;
  border-radius: 20px;
  font-weight: bold;
  font-size: 0.9rem;
}
.synopsis-text {
  max-height: 80px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
```

## 📡 API Reference

### Jikan API Endpoints

| Endpoint            | Descripción              |
| ------------------- | ------------------------ |
| `GET /v4/top/anime` | Obtiene el top de animes |

**Ejemplo de respuesta:**

```json
{
  "data": [
    {
      "mal_id": 1,
      "title": "Fullmetal Alchemist: Brotherhood",
      "year": 2009,
      "type": "TV",
      "episodes": 64,
      "score": 9.09,
      "images": {
        "jpg": {
          "image_url": "https://cdn.myanimelist.net/images/..."
        }
      },
      "synopsis": "Una historia sobre alquimia..."
    }
  ]
}
```

## 📝 Archivos necesarios

### `requirements.txt`

```txt
Django>=4.2,<5.0
requests>=2.31.0
python-dotenv>=1.0.0
```

### `.gitignore`

```gitignore
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
db.sqlite3
.env
*.log
.DS_Store
*.pid
*.seed
*.pid.lock
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add some AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Directrices

- Usa [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Asegúrate de que las pruebas pasen
- Actualiza la documentación si es necesario

## 📝 Licencia

MIT - ver el archivo [LICENSE](LICENSE)

## 🙏 Agradecimientos

- [Jikan API](https://jikan.moe/)
- [MyAnimeList](https://myanimelist.net/)
- [Bulma](https://bulma.io/)
- [Font Awesome](https://fontawesome.com/)
- [Django](https://www.djangoproject.com/)

## 📬 Contacto

**Tu Nombre** - [@tu_twitter](https://twitter.com/tu_twitter) - tu.email@ejemplo.com

Link del proyecto: [https://github.com/tu-usuario/anime-explorer](https://github.com/tu-usuario/anime-explorer)

---

⭐️ **¡No olvides darle una estrella al proyecto!** ⭐️
