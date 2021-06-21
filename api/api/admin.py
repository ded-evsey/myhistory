from django.contrib import admin
from .models import Theme, TGUser
# Register your models here.
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'short'
    ]
    actions = [
        'create_qr'
    ]
    @admin.action(description='Create qr-codes for selection')
    def create_qr(self, request, queryset):
        pass

@admin.register(TGUser)
class TGUserAdmin(admin.ModelAdmin):
    list_display = [
        'user_ident',
        'created',
        'last_login'
    ]