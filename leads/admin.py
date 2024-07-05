# leads/admin.py

from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Lead

def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="leads.csv"'
    writer = csv.writer(response)
    
    writer.writerow(['First Name', 'Last Name', 'Email', 'Country', 'Location', 'Created At'])
    for lead in queryset:
        writer.writerow([lead.first_name, lead.last_name, lead.email, lead.country, lead.location, lead.created_at])

    return response

export_as_csv.short_description = "Export selected leads as CSV"

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'country', 'location', 'created_at')
    actions = [export_as_csv]
