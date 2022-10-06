from django.contrib import admin
from core.models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_event', 'date_created')
    list_filter = ('title', 'user', 'date_event',)


admin.site.register(Event, EventAdmin)
