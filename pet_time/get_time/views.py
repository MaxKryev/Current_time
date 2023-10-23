import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse

url_template = 'http://worldtimeapi.org/api/ip/'


class RemoteTimeView(APIView):
    def get(self, request):
        client_ip = request.GET.get('ip_adress')
        response = requests.get(url=url_template+client_ip)
        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            datetime = data.get('datetime')
            return Response({'datetime': datetime}, status=status.HTTP_200_OK)
        return Response({'message': 'Ебаное блядство'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

