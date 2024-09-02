import requests


def check_ping(camera):
    url = camera.url
    try:
        if url.startswith('http://'):
            url_https = url.replace('http://', 'https://')
        else:
            url_https = url

        # Пробуем соединиться с HTTPS
        response = requests.get(url_https, timeout=5)
        if response.status_code == 200:
            return round(response.elapsed.total_seconds() * 100)

    except requests.RequestException:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return round(response.elapsed.total_seconds() * 100)
        except requests.RequestException:
            pass

    return 0
