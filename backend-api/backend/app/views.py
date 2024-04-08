# backend/app/views.py

import requests
from django.http import JsonResponse

def get_data_from_golang(request):
    try:
        response = requests.get('http://localhost:8080/api/data')
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Failed to fetch data from Golang API'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
