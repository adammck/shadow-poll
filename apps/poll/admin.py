#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin
from models import *


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PollResponse)
