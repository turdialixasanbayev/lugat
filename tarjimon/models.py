from django.db import models


class Dictionary(models.Model):
    uzbek = models.CharField(max_length=225)
    english = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.english} - {self.uzbek}"

    class Meta:
        verbose_name = "Lug'at"
        verbose_name_plural = "Lug'atlar"
