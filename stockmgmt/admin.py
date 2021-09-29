from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['Category', 'Product_Name', 'Quantity','Alert_Level']
   form = StockCreateForm
   list_filter = ['Category']
   search_fields = ['Category', 'Product_Name']

admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
admin.site.register(Customer)


class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['Name','invoice_number']
   form = InvoiceForm
   list_filter = ['Name']
   search_fields = ['Name', 'invoice_number']

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(daily_accounts)
