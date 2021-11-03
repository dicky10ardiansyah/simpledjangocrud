from genericpath import getatime
from django.db import models

# Create your models here.
class TabelBuah(models.Model):
    nama = models.CharField(max_length=50)
    gambar = models.ImageField(upload_to='buah/')
    keterangan = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.nama