from .models import User
from django.contrib import admin
from django.contrib.admin.forms import AdminAuthenticationForm

from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from snowpenguin.django.recaptcha3.widgets import ReCaptchaHiddenInput


class CaptchaAdminAuthenticationForm(AdminAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CaptchaAdminAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['captcha'] = ReCaptchaField(widget=ReCaptchaHiddenInput())


admin.AdminSite.login_form = CaptchaAdminAuthenticationForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_teacher",
        "roles",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_display_links = ("id", "username", "email")
    list_filter = (
        "is_teacher",
        "last_login",
        "date_joined",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    raw_id_fields = ("groups", "user_permissions")
