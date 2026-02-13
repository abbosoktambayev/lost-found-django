from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    # Вот этот кусок добавь:
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('returned', 'Returned'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    # Новые поля
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    def __str__(self):
        return self.title