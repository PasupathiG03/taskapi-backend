from rest_framework import status
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from .utils import custom_response


@api_view(['GET', 'POST'])
def task_list(request):
    try:
        if request.method == 'GET':
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return custom_response(
                success=True,
                message="Tasks fetched successfully",
                data=serializer.data,
                status_code=status.HTTP_200_OK
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
                message="Validation failed",
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        return custom_response(
            success=False,
            message=f"An unexpected error occurred: {str(e)}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
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
            return custom_response(
                success=True,
                message="Task retrieved successfully",
                data=serializer.data,
                status_code=status.HTTP_200_OK
            )

        elif request.method == 'PUT':
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return custom_response(
                    success=True,
                    message="Task updated successfully",
                    data=serializer.data,
                    status_code=status.HTTP_200_OK
                )
            return custom_response(
                success=False,
                message="Validation failed",
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        elif request.method == 'DELETE':
            task.delete()
            return custom_response(
                success=True,
                message="Task deleted successfully",
                data=None,
                status_code=status.HTTP_204_NO_CONTENT
            )

    except Exception as e:
        return custom_response(
            success=False,
            message=f"An unexpected error occurred: {str(e)}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
