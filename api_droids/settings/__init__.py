from os import environ

from split_settings.tools import optional, include

ENV = environ.get('DJANGO_ENV') or 'dev'

base_settings = [
    'base.py',  # standard django settings

    # Select the right env:
    '%s.py' % ENV,
    # Optionally override some settings:
    optional('local.py'),
]

# Include settings:
include(*base_settings)
