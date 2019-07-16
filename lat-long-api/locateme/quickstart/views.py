from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from locateme.quickstart.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import geoip2.database


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


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
        reader = geoip2.database.Reader('/Users/pmercado/lat-long-api/geoip/GeoLite2-City_20190716/GeoLite2-City.mmdb')

        response = reader.city(ip)

        data = {'ip_given': ip,
               'latitude': response.location.latitude,
                'longitude': response.location.longitude }
        return Response(data)
