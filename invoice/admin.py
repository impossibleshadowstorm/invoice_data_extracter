from django.urls import reverse
from django.utils.html import format_html
from import_export import resources
from django.contrib import admin
from .models import File, VendorInvoice
from import_export.admin import ImportExportModelAdmin

class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_file_link']
    search_fields = ['file', 'id']
    list_filter = ['created', 'modified']
    ordering = ['id']
    readonly_fields = ['created', 'modified']

    def display_file_link(self, obj):
        return format_html('<a href="{}">{}</a>', obj.file.url, obj.file.name)
    display_file_link.short_description = 'File'

admin.site.register(File, FileAdmin)

@admin.register(VendorInvoice)
class VendorInvoiceAdmin(ImportExportModelAdmin):
    list_display = [
        'vendor_name', 'gstin', 'state_name', 'invoice_date', 
        'invoice_no', 'po_no', 'tax_percent', 'taxable_amount', 
        'total_amount', 'display_invoice_file_link', 'result',
    ]
    search_fields = [
        'vendor_name', 'gstin', 'state_name', 'invoice_no', 
        'po_no'
    ]
    list_filter = [
        'state_name', 'invoice_date', 'result'
    ]
    date_hierarchy = 'invoice_date'
    ordering = ['invoice_date', 'vendor_name']
    readonly_fields = ['display_invoice_file_link']

    def display_invoice_file_link(self, obj):
        return format_html('<a href="{}">{}</a>', obj.invoice_file.file.url, obj.invoice_file.file.name)
    display_invoice_file_link.short_description = 'Invoice File'