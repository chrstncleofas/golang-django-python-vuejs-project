from .models import Students
from django.http import JsonResponse
from app.serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def studentsApi(request, student_id=0) -> (JsonResponse | None):
    # Fetch all Data API
    if request.method=='GET':
        students = Students.objects.all()
        students_serializer=StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)
    # Create or Add API
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        students_serializer=StudentSerializer(data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    # Update API
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Students.objects.get(student_id=student_data['StudentID'])
        students_serializer=StudentSerializer(student, data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    # Delete API
    elif request.method=='DELETE':
        student=Students.objects.get(student_id=student_id)
        student.delete()
        return JsonResponse("Deleted Successfully", safe=False)
