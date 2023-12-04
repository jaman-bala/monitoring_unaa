from django.shortcuts import render
import asyncio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Camera
from asgiref.sync import sync_to_async


@sync_to_async
def get_cameras():
    return list(Camera.objects.all().select_related())


async def home_view(request):
    cameras = await get_cameras()
    online_count = 0
    offline_count = 0
    tasks = [camera.check_status_async() for camera in cameras]
    statuses = await asyncio.gather(*tasks)
    for camera, status in zip(cameras, statuses):
        camera.status = status
        if camera.status == 'Online':
            online_count += 1
        else:
            offline_count += 1

    page = request.GET.get('page', 1)
    paginator = Paginator(cameras, 15)  # Показывать 15 камер на странице

    try:
        cameras = paginator.page(page)
    except PageNotAnInteger:
        cameras = paginator.page(1)
    except EmptyPage:
        cameras = paginator.page(paginator.num_pages)

    context = {'cameras': cameras, 'online_count': online_count, 'offline_count': offline_count}
    return render(request, 'home.html', context)
