from django.core.cache import cache
from backend.apps.cameras.models import CameraModels
from backend.apps.cameras.schemas import CameraOutput, CategorySchemas, RegionSchemas
from backend.apps.cameras.ping_utils import check_ping
from backend.apps.cameras.tasks import async_check_ping


def get_ping_status(camera):
    return check_ping(camera)


def get_cameras_with_ping():
    cache_key = 'cameras_with_ping'
    cached_data = cache.get(cache_key)

    if cached_data:
        return cached_data

    cameras = list(CameraModels.objects.select_related('category').all())
    results = []
    ping_results = {}

    for camera in cameras:
        ping_results[camera.id] = async_check_ping.delay(camera.id)
        category_data = CategorySchemas.from_orm(camera.category)
        region_data = RegionSchemas.from_orm(camera.region)
        camera_output = CameraOutput(
            id=camera.id,
            title=camera.title,
            url=camera.url,
            status=camera.check_status_sync(),
            ping_status=None,  # placeholder for async result
            category=category_data,
            region=region_data,
        )
        results.append(camera_output)

    # Обновляем ping_status в уже готовых results
    for result in results:
        task = ping_results[result.id]
        try:
            result.ping_status = task.get(timeout=10) or 0  # Установите значение по умолчанию, если None
        except Exception as e:
            result.ping_status = 0  # Устанавливаем значение по умолчанию при ошибке

    cache.set(cache_key, results, timeout=60*5)  # кэшировать на 5 минут
    return results
