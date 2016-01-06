from django.contrib import admin
from .models import *


# Register your models here.
class ChoicesBooleanAdmin(admin.ModelAdmin):
    pass


class InterviewLocationAdmin(admin.ModelAdmin):
    pass


class PositionAdmin(admin.ModelAdmin):
    pass


class AreaOfWorkAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


class ProvinceAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class DistrictAdmin(admin.ModelAdmin):
    pass

admin.site.register(ChoicesBoolean, ChoicesBooleanAdmin)
admin.site.register(InterviewLocation, InterviewLocationAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(AreaOfWork, AreaOfWorkAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
