import requests
from backend.apps.cameras.models import CameraModels
from backend.apps.cameras.schemas import CameraOutput, CategorySchemas, RegionSchemas

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
        # Пробуем соединиться с HTTP
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return round(response.elapsed.total_seconds() * 100)
        except requests.RequestException:
            pass

    return 0

def get_cameras_with_ping():
    cameras = list(CameraModels.objects.select_related('category').all())
    results = []
    for camera in cameras:
        ping_result = check_ping(camera)
        category_data = CategorySchemas.from_orm(camera.category)
        region_data = RegionSchemas.from_orm(camera.region)
        camera_output = CameraOutput(
            id=camera.id,
            title=camera.title,
            url=camera.url,
            status=camera.check_status_sync(),
            ping_status=ping_result,
            category=category_data,
            region=region_data,
        )
        results.append(camera_output)

    return results
