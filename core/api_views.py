from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item
import json


@csrf_exempt
def items_api(request):
    if request.method == 'GET':
        items = list(Item.objects.values())
        return JsonResponse(items, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        item = Item.objects.create(
            title=data['title'],
            description=data['description'],
            status=data['status'],
            location=data['location'],
            contact_info=data['contact_info']
        )
        return JsonResponse({'id': item.id})


@csrf_exempt
def item_detail_api(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'status': item.status,
            'location': item.location,
            'contact_info': item.contact_info,
        })

    if request.method == 'PUT':
        data = json.loads(request.body)
        item.title = data.get('title', item.title)
        item.description = data.get('description', item.description)
        item.status = data.get('status', item.status)
        item.location = data.get('location', item.location)
        item.contact_info = data.get('contact_info', item.contact_info)
        item.save()
        return JsonResponse({'message': 'Updated'})

    if request.method == 'DELETE':
        item.delete()
        return JsonResponse({'message': 'Deleted'})