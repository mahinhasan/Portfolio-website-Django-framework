# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Topic,Webpage,Access

admin.site.register(Access)
admin.site.register(Topic)
admin.site.register(Webpage)
# Register your models here.
