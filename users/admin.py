from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Beneficiary, Institution, NaturalDonor, LegalDonor,Admin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email","name", "idType", "numID", "role", "profilePicture", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ('Personal info', {'fields': ('name', 'idType', 'numID',"role","profilePicture")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "name", "idType", "numID", "role", "profilePicture","is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Beneficiary)
admin.site.register(NaturalDonor)
admin.site.register(LegalDonor)
admin.site.register(Institution)
admin.site.register(Admin)