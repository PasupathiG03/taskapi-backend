from rest_framework.response import Response
from datetime import datetime

def custom_response(success, message, data=None, status_code=200):
    return Response({
        "success": success,
        "message": message,
        "data": data,
        "timestamp": datetime.now().isoformat()
    }, status=status_code)
