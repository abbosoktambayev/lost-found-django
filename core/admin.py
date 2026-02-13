from django.contrib import admin
from .models import Item, Category


# Чтобы можно было создавать Категории (Электроника, Документы и т.д.)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # Какие колонки показывать в списке
    list_display = ('title', 'status', 'category', 'location', 'created_at', 'has_image')

    # Фильтры справа (очень удобно!)
    list_filter = ('status', 'category', 'created_at')

    # Строка поиска (ищет по названию, описанию и месту)
    search_fields = ('title', 'description', 'location')

    # КИЛЛЕР-ФИЧА: меняй статус прямо в списке!
    list_editable = ('status',)

    # Показывает дату, но не дает менять вручную
    readonly_fields = ('created_at',)

    # Красивая галочка, если есть фото
    def has_image(self, obj):
        return bool(obj.image)

    has_image.boolean = True
    has_image.short_description = "Photo?"