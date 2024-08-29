from django.db import models

import requests


class CategoryModels(models.Model):
    """Models for category models"""

    title = models.CharField("Категория", max_length=255, db_index=True)
    slug = models.SlugField("Теги", max_length=50, unique=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить Категорию"


class RegionModels(models.Model):
    """"Models for regions"""

    title = models.CharField("Название региона", max_length=255, db_index=True)
    slug = models.SlugField("Теги", max_length=50, unique=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить Регион"


class CameraModels(models.Model):
    """Models for"""

    category = models.ForeignKey(CategoryModels, on_delete=models.CASCADE, verbose_name="Категория")
    region = models.ForeignKey(RegionModels, on_delete=models.CASCADE, verbose_name="Регион")
    title = models.CharField("Название камеры", max_length=255, db_index=True)
    url = models.URLField("Вставьте ссылку", db_index=True)

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

    def check_status_sync(self):
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200:
                return "Online"
            else:
                return "Offline"
        except requests.RequestException:
            return "Offline"

    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить Камеру"

    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить Камеру"
