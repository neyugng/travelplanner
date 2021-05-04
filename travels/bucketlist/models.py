from django.db import models

class BucketListLocation(models.Model):
    item = models.CharField(max_length=255)
    list_num = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Location")
        verbose_name_plural = ("locations")
        ordering = ["item"]

    def __str__(self):
        return self.item


class BucketList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("Bucket List")
        verbose_name_plural = ("Bucket Lists")
        ordering = ["name"]

    def __str__(self):
        return self.name
        
