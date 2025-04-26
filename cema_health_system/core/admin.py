from django.contrib import admin
from .models import Client, Program
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'contact')  # show these columns in admin list
    search_fields = ('name', 'contact')        # allow search by name or contact
    list_filter = ('programs',)                # allow filtering by related programs
    ordering = ('name',)                       # order by name in the admin panel

admin.site.register(Program)
