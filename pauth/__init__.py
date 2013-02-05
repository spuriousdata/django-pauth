from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

__version__ = (0, 0, 1)

try:
    conf = settings.PAUTH
except AttributeError:
    raise ImproperlyConfigured("django-pauth requires configuration.")

prefer = conf.get('check_first', 'internal')

internal = {}
external = {}

internal = dict(map(lambda x: (x.name, x),
                            [import_module(p).provider for p in conf['providers'].get('internal', [])]))
external = dict(map(lambda x: (x.name, x),
                                 [import_module(p).provider for p in conf['providers'].get('external', [])]))

import pdb; pdb.set_trace()
loaded_providers = internal.copy()
loaded_providers.update(external)

[lp.configure(conf['vendor']) for lp in loaded_providers.values()]

