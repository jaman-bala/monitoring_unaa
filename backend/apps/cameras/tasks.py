from celery import shared_task
from backend.apps.cameras.models import CameraModels
from backend.apps.cameras.utils import check_ping


@shared_task
def async_check_ping(camera_id):
    camera = CameraModels.objects.get(id=camera_id)
    return check_ping(camera)
