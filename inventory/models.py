from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=50)
    call = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="image")
    content = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    amount = models.PositiveIntegerField(null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
