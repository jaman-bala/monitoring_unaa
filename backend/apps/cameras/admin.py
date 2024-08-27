from django.contrib import admin
from backend.apps.cameras.models import CameraModels
from backend.apps.cameras.models import CategoryModels
from backend.apps.cameras.models import RegionModels


@admin.register(CategoryModels)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "id")
    search_fields = ("title",)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(RegionModels)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "id")
    search_fields = ("title",)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CameraModels)
class CameraAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "id",)
    list_display_links = ("title", "url",)
    search_fields = ("title",)
    list_per_page = 15
    save_on_top = True


admin.site.site_title = 'ГАРТСВС при КМ КР'
admin.site.site_header = 'ВХОД MONITORING'
admin.site.index_title = 'СПИСОК ДАННЫХ'
