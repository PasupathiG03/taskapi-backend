from rest_framework import status
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from .utils import custom_response

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return custom_response(
            success=True,
            message="Tasks fetched successfully",
            data=serializer.data
        )

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(
                success=True,
                message="Task created successfully",
                data=serializer.data,
                status_code=status.HTTP_201_CREATED
            )
        return custom_response(
            success=False,
            message="Failed to create task",
            data=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return custom_response(
            success=False,
            message="Task not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return custom_response(True, "Task retrieved successfully", serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(True, "Task updated successfully", serializer.data)
        return custom_response(False, "Validation failed", serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return custom_response(True, "Task deleted successfully", None, status.HTTP_204_NO_CONTENT)
