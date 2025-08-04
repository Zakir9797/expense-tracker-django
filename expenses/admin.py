from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Entry
class EntryResource(resources.ModelResource):
    class Meta:
        model = Entry
@admin.register(Entry)
class EntryAdmin(ImportExportModelAdmin):
    resource_class = EntryResource
    list_display = ['date', 'time', 'type', 'category', 'total_amount', 'currency']
    search_fields = ['category', 'description']
    list_filter = ['type', 'category', 'currency', 'date']