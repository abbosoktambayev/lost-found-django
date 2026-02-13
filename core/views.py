from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item


def home(request):
    status = request.GET.get('status')
    query = request.GET.get('q')  # Получаем поисковый запрос

    items = Item.objects.all().order_by('-created_at')

    if status:
        items = items.filter(status=status)

    if query:
        # Ищем по названию ИЛИ описанию
        items = items.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'core/home.html', {
        'items': items,
        'active_status': status,
    })


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'core/item_detail.html', {'item': item})


def add_item(request):
    if request.method == 'POST':
        # Сохраняем вещь с картинкой
        Item.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            status=request.POST['status'],
            location=request.POST['location'],
            contact_info=request.POST['contact_info'],
            image=request.FILES.get('image')  # <--- ВОТ ЭТО ВАЖНО
        )
        return redirect('home')

    return render(request, 'core/add_item.html')