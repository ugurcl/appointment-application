from django.contrib import admin
from .models import AppointmentCreation, AppointmentDetails
from django.utils.html import format_html

@admin.register(AppointmentCreation)
class AppointmentCreationModelAdmin(admin.ModelAdmin):
    list_display = ('id','staff_member','status_display','formatted_date','formatted_time')


    def formatted_date(self, obj):
        return obj.date.strftime('%d.%m.%Y') 
    formatted_date.short_description = "Tarih"

    
    def formatted_time(self, obj):
        return obj.time.strftime('%H:%M') 
    formatted_time.short_description = "Saat"

    def status_display(self, obj):
        if obj.appointment_is_active:
            return format_html('<span style="color: #32de84;">Boş</span>')
        else:
            return format_html('<span style="color: #EF0107;">Dolu</span>')
    status_display.short_description = "Durum"

@admin.register(AppointmentDetails)
class AppointmentDetailModelAdmin(admin.ModelAdmin):
    list_display = ('id',)

