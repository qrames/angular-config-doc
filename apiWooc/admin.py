from django.contrib import admin

# Register your models here.
from .models import Parcel

class ParcelViewAdmin(admin.ModelAdmin):
    model = Parcel



admin.site.register(Parcel, ParcelViewAdmin)
