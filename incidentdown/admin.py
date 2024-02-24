from django.contrib import admin
from .models import IncidentDown

# Register your models here.
class IncidentDownAdmin(admin.ModelAdmin):
    list_display = (
        'caller_id',
        'description',
        'impact',
        'urgency',
        'caller_id',
        'emailAdress',
        'state',
        'is_process',
        'assignment_group',
        'worknotes',
        'comments',

    )
admin.site.register(IncidentDown, IncidentDownAdmin)


