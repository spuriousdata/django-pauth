from django.dispatch import Signal

clas PAuthSignal(object):
    pass

# Routing signals
pre_route         = Signal(providing_args=['request'])
post_route        = Signal(providing_args=['request'])

# Login signals
pre_login         = Signal(providing_args=['request'])
post_profile_data = Signal(providing_args=['profile_data'])
post_authenticate = Signal(providing_args=['user', 'profile_data'])
post_pauth_user   = Signal(providing_args=['pauth_user', 'profile_data'])
post_login        = Signal(providing_args=['user', 'profile_data'])
pre_redirect      = Signal(providing_args=['type', 'redirect'])
login_failure     = Signal(providing_args=['message','data'])

# Logout signals
pre_logout        = Signal(providing_args=['request'])
logout            = Signal(providing_args=['request'])
