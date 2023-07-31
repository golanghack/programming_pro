from django.contrib import admin
import datetime

from main.models import (AdvUser, SuperRubric, 
                        SubRubric, News, AdditionalImage) 
from main.forms import SubRubricForm
from main.utils import send_activation_notification

def send_activation_notifications(modeladmin: str, request: str, queryset: str) -> None:
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
        modeladmin.message_user(request, 
                            'Письма с требованиями активации аккаунта отправлены')
    send_activation_notifications.short_description = '''
                            Отправка писем стребованиями активации''' 

class NonactivatedFilter(admin.SimpleListFilter):
    title = 'Активированы?'
    parameter_name = 'actstate'

    def lookups(self, request: str, model_admin: str) -> tuple:
        return (
            ('activated', 'Успешно активирован'),
            ('threedays', 'Не активирован более 3 суток'),
            ('week', 'Не активирован более недели'),
        )

    def queryset(self, request: str, queryset: str):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, 
                                    is_activated=True)
        elif val == 'threedays':
            day = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, 
                                    is_activated=False,
                                    date_joined__date__lt=day)
        elif val == 'week':
            day = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, 
                                    is_activated=False, 
                                    date_joined__date__lt=day)

class AdvUserAdmin(admin.ModelAdmin):
    """Customisation users for admin panel""" 

    list_display = ('__str__', 
                            'is_activated', 
                            'date_joined')
    search_fields = ('username', 
                            'email',
                            'first_name', 
                            'last_name')
    list_filter = (NonactivatedFilter,)
    fields = (
        ('username', 'email'),
        ('first_name', 'last_name'),
        ('send_messages', 'is_active', 'is_activated'),
        ('is_staff', 'is_superuser'),
        'groups', 
        'user_permissions',
        ('last_login', 'date_joined')
    )

    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications,)

class SubRubricInline(admin.TabularInline):
    """Subrubric Inline"""

    model = SubRubric

class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)

class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class NewsAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 
                        'content', 'author', 'created_at')
    fields = (
        ('rubric', 'author'), 
        'title', 'content', 
        'weight', 'source',
        'image', 'is_active'
    )
    inlines = (AdditionalImageInline,)

admin.site.register(AdvUser, AdvUserAdmin)
admin.site.register(SuperRubric, SuperRubricAdmin)
admin.site.register(SubRubric, SubRubricAdmin)
admin.site.register(News, NewsAdmin)