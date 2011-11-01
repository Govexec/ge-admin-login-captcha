from forms import CaptchaAuthenticationForm
from django.contrib import admin

admin.site.login_form = CaptchaAuthenticationForm
admin.site.login_template = "admin_login_captcha/login.html"