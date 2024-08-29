import asyncio
from asgiref.sync import sync_to_async
import httpx
from backend.apps.cameras.models import CameraModels
from backend.apps.cameras.schemas import CameraOutput, CategorySchemas, RegionSchemas

# Настройка семафора для ограничения одновременных запросов
SEMAPHORE_LIMIT = 10
semaphore = asyncio.Semaphore(SEMAPHORE_LIMIT)

async def check_ping(camera):
    async with semaphore:
        try:
            async with httpx.AsyncClient(verify=False) as client:
                url = camera.url
                if url.startswith('http://'):
                    url_https = url.replace('http://', 'https://')
                else:
                    url_https = url

                # Пробуем соединиться с HTTPS
                response = await client.get(url_https)
                if response.status_code == 200:
                    return round(response.elapsed.total_seconds() * 100)

        except httpx.RequestError:
            # Пробуем соединиться с HTTP
            try:
                async with httpx.AsyncClient(verify=False) as client:
                    response = await client.get(url)
                    if response.status_code == 200:
                        return round(response.elapsed.total_seconds() * 100)
            except httpx.RequestError:
                pass

        return 0

async def get_cameras_with_ping():
    # Использование кеша для хранения камер
    cameras = await sync_to_async(list)(CameraModels.objects.select_related('category').all())
    tasks = [check_ping(camera) for camera in cameras]
    ping_results = await asyncio.gather(*tasks)

    results = []
    for camera, ping_result in zip(cameras, ping_results):
        # Использование кешированных данных
        category_data = CategorySchemas.from_orm(camera.category)
        region_data = RegionSchemas.from_orm(camera.region)
        camera_output = CameraOutput(
            id=camera.id,
            title=camera.title,
            url=camera.url,
            status=await camera.check_status_async(),
            ping_status=ping_result,
            category=category_data,
            region=region_data,
        )
        results.append(camera_output)

    return results
