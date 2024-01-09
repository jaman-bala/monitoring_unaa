from django.db import models
import httpx


class Camera(models.Model):
    title = models.CharField("Название камеры", max_length=255, db_index=True)
    url = models.URLField("Вставьте ссылку", db_index=True)

    def __str__(self):
        return self.title

    async def check_status_async(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.url)
            if response.status_code == 200:
                return "Online"
            else:
                return "Offline"
        except httpx.HTTPError:
            return "Offline"

    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить камеру"
