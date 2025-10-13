from rest_framework.response import Response
from rest_framework import status

def custom_response(success=True, message="", data=None, status_code=status.HTTP_200_OK):
    response_data = {
        "success": success,
        "message": message,
        "data": data
    }
    return Response(response_data, status=status_code)
