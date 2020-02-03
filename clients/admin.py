from django.contrib import admin

from .models import Client, Comment, vehicle
class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
class vehicleline(admin.ModelAdmin):
    list_display = ( 'client_name', 'vehicle_model', 'VIN')

admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(vehicle)
