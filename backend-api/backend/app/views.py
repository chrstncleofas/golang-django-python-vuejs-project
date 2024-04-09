import requests
from .models import Students
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

GO_API_BASE_URL = 'http://localhost:8000'

def api_request(method, path, data=None):
    url = f'{GO_API_BASE_URL}{path}'
    response = requests.request(method, url, json=data)
    return response.json(), response.status_code

@require_http_methods(["GET"])
def get_all_students(request):
    try:
        students, status_code = api_request('GET', '/students')
        return JsonResponse(students, status=status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def get_student(request, student_id):
    try:
        student, status_code = api_request('GET', f'/students/{student_id}')
        return JsonResponse(student, status=status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["POST"])
def create_student(request):
    try:
        student_data = request.POST.dict()
        response_data, status_code = api_request('POST', '/students', student_data)
        if status_code == 201:
            student = Students.objects.create(**student_data)
            return JsonResponse(student_data, status=201)
        else:
            return JsonResponse(response_data, status=status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    # booking_data=JSONParser().parse(request)
    # booking_serializer=BookingSerializer(data=booking_data)
    # if booking_serializer.is_valid():
    #     booking_serializer.save()
    #     return JsonResponse("Added Successfully", safe=False)
    # return JsonResponse("Failed to Add", safe=False)

@require_http_methods(["PUT"])
def update_student(request, student_id):
    try:
        updated_student_data = request.POST.dict()
        response_data, status_code = api_request('PUT', f'/students/{student_id}', updated_student_data)
        if status_code == 200:
            student = Students.objects.get(pk=student_id)
            for key, value in updated_student_data.items():
                setattr(student, key, value)
            student.save()
            return JsonResponse(updated_student_data)
        else:
            return JsonResponse(response_data, status=status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["DELETE"])
def delete_student(request, student_id):
    try:
        response_data, status_code = api_request('DELETE', f'/students/{student_id}')
        if status_code == 200:
            student = Students.objects.get(pk=student_id)
            student.delete()
            return JsonResponse({'message': 'Student deleted successfully'})
        else:
            return JsonResponse(response_data, status=status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
