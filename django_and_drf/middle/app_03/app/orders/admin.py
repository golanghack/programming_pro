from django.contrib import admin
from django.utils.html import mark_safe
from django.urls import reverse
from django.http import HttpResponse
from .models import Order, OrderItem
import csv
import datetime

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]

    # one line
    writer.writerow([field.verbose_name for field in fields])
    # write lines
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Экспортировать как CSV'

class OrderItemInline(admin.TabularInline):

    model = OrderItem
    raw_id_fields = ['product']


def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">Представление</a>')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email', 'paid', 'created', 'updated',order_detail]
    list_filter = ['paid', 'created', 'updated',]
    inlines = [OrderItemInline]
    actions = [export_to_csv]

