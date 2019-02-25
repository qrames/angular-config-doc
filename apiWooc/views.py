from django.shortcuts import render

# Create your views here.
from .models import Parcel

from django.views import View
from django.http import JsonResponse

from woocPy.settings import wcapi
import json

class ParcelViewSet(View):
    """Json View for 1 user parcel"""

    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        print (kwargs['woocUser'])
        queryset = Parcel.objects.filter(woocUser=kwargs['woocUser'])
        json_data = {
            'code': 'django api',
            'message': "it's work",
            'data': {
                'status': 404,
            },
        }
        json_data_parcel = {
            'id utilisateur': kwargs['woocUser'],
            'parcels': {},
        }

        for parcelle in queryset:
            wc_product = wcapi.get("products/" + str(parcelle.woocID), )
            # print ( json.loads(wc_product.text)['name'])
            print ( wc_product.text)
            wc_parcel = json.loads(wc_product.text)
            json_data_parcel['parcels']['id WooCommerce : ' + str(parcelle.woocID)] = {
                'name': parcelle.name,
                'wc name: ': wc_parcel['name'],
                'price: ': wc_parcel['price'],
                'sale_price: ': wc_parcel['sale_price'],
                'regular_price: ': wc_parcel['regular_price'],

            }
        json_data['data'] = json_data_parcel
        return JsonResponse(json_data)
