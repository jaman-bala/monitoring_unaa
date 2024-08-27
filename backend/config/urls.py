from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI

from backend.apps.cameras.views import router as cameras_router

api = NinjaAPI(
    title="МОНИТОРИНГ ГАРТСВС при КМ КР", # наименование проекта
   # docs_url=None, # закрыть доступ к документации docs
) # auth=django_auth, csrf=True

api.add_router(
    "api/",
    cameras_router,
    tags=["СПИСОК ДАННЫХ"]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
