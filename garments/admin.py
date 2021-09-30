from django.contrib import admin
from garments.models import FormalShirt
from garments.models import CasualShirt
from garments.models import TShirt
from garments.models import TrousersBottomWear
from garments.models import JeansBottomWear
from garments.models import CargoBottomWear


class FormalShirtAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','available','created','updated')

class CasualShirtAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','available','created','updated')

class TShirtAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','available','created','updated')

class TrousersBottomWearAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','available','created','updated')


class JeansBottomWearAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','available','created','updated')

class CargoBottomWearAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','available','created','updated')


# Register your models here.
admin.site.register(FormalShirt,FormalShirtAdmin)
admin.site.register(CasualShirt,CasualShirtAdmin)
admin.site.register(TShirt,TShirtAdmin)
admin.site.register(TrousersBottomWear,TrousersBottomWearAdmin)
admin.site.register(JeansBottomWear,JeansBottomWearAdmin)
admin.site.register(CargoBottomWear,CargoBottomWearAdmin)