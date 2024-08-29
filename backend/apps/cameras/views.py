from ninja import Router
from django.http import HttpRequest
from asgiref.sync import sync_to_async
from typing import List

from backend.apps.cameras.models import CameraModels
from backend.apps.cameras.models import CategoryModels
from backend.apps.cameras.models import RegionModels
from backend.apps.cameras.utils import get_cameras_with_ping
from backend.apps.cameras.utils import check_ping
from backend.apps.cameras.schemas import CameraOutput
from backend.apps.cameras.schemas import CategorySchemas
from backend.apps.cameras.schemas import RegionSchemas

router = Router()


@router.get("/categories", response=List[CategorySchemas])
def get_categories(request: HttpRequest):
    qs = list(CategoryModels.objects.all())
    return qs

@router.get("/regions", response=List[RegionSchemas])
def get_regions(request: HttpRequest):
    qs = list(RegionModels.objects.all())
    return qs

@router.get("/cameras", response=List[CameraOutput])
def get_cameras(request: HttpRequest):
    cameras = get_cameras_with_ping()
    return cameras

@router.get("/cameras/{camera_id}", response=CameraOutput)
def get_camera(request: HttpRequest, camera_id: int):
    camera = CameraModels.objects.select_related('category').get(id=camera_id)
    ping_status = check_ping(camera)
    status = camera.check_status_sync()
    category_data = CategorySchemas.from_orm(camera.category)
    region_data = RegionSchemas.from_orm(camera.region)
    return CameraOutput(
        id=camera.id,
        title=camera.title,
        url=camera.url,
        status=status,
        ping_status=ping_status,
        category=category_data,
        region=region_data,
    )