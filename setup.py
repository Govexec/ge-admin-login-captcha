from distutils.core import setup

setup(
    name='Admin Login Captcha',
    version='0.1.0',
    author_email='GEWebDevTeam@govexec.com',
    packages=['admin_login_captcha'],
    url='https://github.com/Govexec/ge-admin-login-captcha',
    description="Adds django-simple-captcha to admin login (replaces admin login template and form)",
    long_description=open('README.rst').read(),
    install_requires=[
     "Django >= 1.3",
     "django-simple-captcha == 0.3.0",
    ],
)