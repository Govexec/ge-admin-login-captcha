=======
GE Admin Login Captcha
=======

Installation
------------
Add ``admin_login_captcha`` and ``captcha`` to the ``INSTALLED_APPS`` in ``settings.py``::

    # settings.py
    INSTALLED_APPS = (
        ...
    	'captcha',
        'admin_login_captcha',
        ...
    )

Add ``captcha`` pattern to ``urlpatterns`` in ``urls.py``::
    
    # urls.py
    urlpatterns = patterns('',
    	...
    	url(r'^captcha/', include('captcha.urls')),
    	...
    )
    
Django Simple Captcha
---------------------

Requires that the Django Simple Captcha app <http://code.google.com/p/django-simple-captcha/w/list> is installed and its settings are imported into the main Django settings file.  
Please see django-simple-captcha's README for additional information.