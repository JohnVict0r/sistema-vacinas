from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.forms import ChoiceField

from .models import User, Uf, Municipio, Estabelecimento, Vaccine, User_Vaccine, User_Estabelecimento, EstoqueVacina


""" class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user' """

class VaccineAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_professional_health :
            return True
        else:
            return False
    def has_view_permission(self, request, obj=None):
        if request.user.is_professional_health :
            return True
        else:
            return False
    def has_change_permission(self, request, obj=None):
        if request.user.is_professional_health :
            return True
        else:
            return False
    def has_module_permission(self, request):
        if not request.user.is_authenticated:
            return False
        if request.user.is_professional_health :
            return True
        else:
            return False

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'is_patient', 'is_manager_sus', 'is_professional_health' )
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_professional_health', 'is_manager_sus')}),
    )

    def save_model(self, request, obj, form, change):
        if(obj.is_professional_health):
            """ permission_add_vaccine = Permission.objects.get(name='Can add vaccine')
            permission_view_vaccine = Permission.objects.get(name='Can view vaccine')
            u = User.objects.get(username=obj.username)
            u.user_permissions.add(permission_add_vaccine)
            u.user_permissions.add(permission_view_vaccine) """
            obj.is_staff = True
        if(obj.is_manager_sus):
            obj.is_staff = True
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin )
admin.site.register(Uf, )
admin.site.register(Municipio,)
admin.site.register(Estabelecimento,)
admin.site.register(User_Estabelecimento,)
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(EstoqueVacina, VaccineAdmin)
