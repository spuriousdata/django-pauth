##############
django-pauth
##############

Pluggable authentication for django. I wasn't really happy with the other
social-login options available, so I wrote this.

============
Installation
============

Add a url entry in ``urls.py``::

	urlpatterns += patterns('',
		(r'^auth/', include('pauth.urls')),
	)

Add ``pauth`` to your ``INSTALLED_APPS``::

	INSTALLED_APPS = (
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'pauth',
	)

Add ``pauth.backends.PAuthBackend`` to ``AUTHENTICATION_BACKENDS``::

	# put janrain.backends.JanrainBackend first
	AUTHENTICATION_BACKENDS = (
		'pauth.backends.PAuthBackend',
		'django.contrib.auth.backends.ModelBackend',
	)
