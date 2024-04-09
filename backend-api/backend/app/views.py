# import requests
# from django.http import JsonResponse

# def get_data_from_golang(request):
#     try:
#         response = requests.get('http://localhost:8080/api/data')
#         if response.status_code == 200:
#             data = response.json()
#             return JsonResponse(data)
#         else:
#             return JsonResponse({'error': 'Failed to fetch data from Golang API'}, status=500)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Students
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser

@csrf_exempt
def studentApi(request, student_id=0):
    if request.method == 'GET':
        students = Students.objects.all()
        student_serializer = StudentSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        try:
            student = Students.objects.get(StudentID=student_data['StudentID'])
        except Students.DoesNotExist:
            return JsonResponse("Student does not exist", status=404)
        
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        try:
            student = Students.objects.get(StudentID=student_id)
        except Students.DoesNotExist:
            return JsonResponse("Student does not exist", status=404)
        
        student.delete()
        return JsonResponse("Deleted Successfully", safe=False)
