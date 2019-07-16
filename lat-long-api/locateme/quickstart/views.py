from rest_framework.decorators import api_view
from rest_framework.response import Response
import geoip2.database
from django.conf import settings


@api_view(['GET'])
def status(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = {'status': "UP"}
        return Response(data)

@api_view(['GET'])
def locate(request, ip0, ip1, ip2, ip3):

    if request.method == 'GET':
        ip = "{}.{}.{}.{}".format(ip0, ip1, ip2, ip3)
        path = settings.GEOIP_PATH
        reader = geoip2.database.Reader(path)

        response = reader.city(ip)

        data = {'ip_given': ip,
               'latitude': response.location.latitude,
                'longitude': response.location.longitude }
        return Response(data)
