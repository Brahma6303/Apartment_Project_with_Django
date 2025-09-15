from django.contrib import admin
from .models import Flat,Owner,Address
# Register your models here.
class FlatAdmin(admin.ModelAdmin):
    list_display=['block_name','flat_num','br_count','status']
    list_filter=['block_name','flat_num','status']

admin.site.register(Flat,FlatAdmin)
admin.site.register(Owner)
admin.site.register(Address)
