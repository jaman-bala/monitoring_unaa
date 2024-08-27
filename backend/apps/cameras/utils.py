import asyncio
from asgiref.sync import sync_to_async
import httpx

from backend.apps.cameras.models import CameraModels
from backend.apps.cameras.schemas import CameraOutput
from backend.apps.cameras.schemas import CategorySchemas
from backend.apps.cameras.schemas import RegionSchemas


async def check_ping(camera):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(camera.url)
        if response.status_code == 200:
            return round(response.elapsed.total_seconds() * 100)
        else:
            return 0
    except httpx.HTTPError:
        return 0


async def get_cameras_with_ping():
    cameras = await sync_to_async(list)(CameraModels.objects.select_related('category').all())
    tasks = [check_ping(camera) for camera in cameras]
    ping_results = await asyncio.gather(*tasks)

    results = []
    for camera, ping_result in zip(cameras, ping_results):
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
