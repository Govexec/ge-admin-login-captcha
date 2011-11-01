from django.contrib.admin.forms import AdminAuthenticationForm
from captcha.fields import CaptchaField

class CaptchaAuthenticationForm(AdminAuthenticationForm):
    captcha = CaptchaField(help_text="TEST")