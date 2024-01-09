from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from asgiref.sync import sync_to_async
import asyncio

from ping3 import ping
import httpx

from .models import Camera


async def get_cameras_with_ping():
    cameras = await sync_to_async(list)(Camera.objects.all().select_related())

    async def check_ping(camera):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(camera.url)
            if response.status_code == 200:
                return round(
                    response.elapsed.total_seconds() * 100
                )  # Преобразуем миллисекунды в проценты
            else:
                return 0
        except httpx.HTTPError:
            return f'{"error 0"}'

    tasks = [check_ping(camera) for camera in cameras]
    ping_results = await asyncio.gather(*tasks)

    for camera, ping_result in zip(cameras, ping_results):
        camera.ping_status = ping_result

    return cameras


async def home_view(request):
    cameras = await get_cameras_with_ping()
    online_count = 0
    offline_count = 0
    total_count = len(cameras)
    tasks = [camera.check_status_async() for camera in cameras]
    statuses = await asyncio.gather(*tasks)
    for camera, status in zip(cameras, statuses):
        camera.status = status
        if camera.status == "Online":
            online_count += 1
        else:
            offline_count += 1

    page = request.GET.get("page", 1)
    paginator = Paginator(cameras, 15)  # Показывать 15 камер на странице

    try:
        cameras = paginator.page(page)
    except PageNotAnInteger:
        cameras = paginator.page(1)
    except EmptyPage:
        cameras = paginator.page(paginator.num_pages)

    context = {
        "cameras": cameras,
        "online_count": online_count,
        "offline_count": offline_count,
        "total_count": total_count,
    }
    return render(request, "home.html", context)
