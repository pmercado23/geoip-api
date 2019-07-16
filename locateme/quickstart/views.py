import geoip2.database
from django.conf import settings
from django.http import JsonResponse


def status(request):
    """
    Returns Status when called
    """
    if request.method == 'GET':
        data = {'status': "UP"}
        return JsonResponse(data)

def locate(request, ip0, ip1, ip2, ip3):
    """
    Given IP, uses package geoip2 and calls local DB with a lookup.
    This returns json:
    data = {'ip': ip,
            'country': response.country.name,
            'city': response.city.name,
            'subdivisions_most_specific_name': response.subdivisions.most_specific.name,
            'postal_code': response.postal.code,
            'latitude': response.location.latitude,
            'longitude': response.location.longitude }
    """

    if request.method == 'GET':
        ip = "{}.{}.{}.{}".format(ip0, ip1, ip2, ip3)
        path = settings.GEOIP_PATH
        reader = geoip2.database.Reader(path)

        response = reader.city(ip)

        data = {'ip': ip,
                'country': response.country.name,
                'city': response.city.name,
                'subdivisions_most_specific_name': response.subdivisions.most_specific.name,
                'postal_code': response.postal.code,
                'latitude': response.location.latitude,
                'longitude': response.location.longitude }

        return JsonResponse(data)

