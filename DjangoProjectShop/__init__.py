# DjangoProjectShop/__init__.py

from __future__ import absolute_import, unicode_literals
# Це дозволяє використовувати Celery разом із Django
from .celery import app as celery_app

__all__ = ('celery_app',)
