from django.contrib import admin
from .models import Theme, TGUser
# Register your models here.
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    actions = [
        'create_qr'
    ]
    @admin.action(description='Create qr-codes for selection')
    def create_qr(self, request, queryset):
        pass


class TGUserAdmin(admin.ModelAdmin):
    list_display = [
        'user_ident',
        'created',
        'last_login'
    ]