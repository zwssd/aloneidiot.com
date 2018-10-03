#_*_coding:utf8_*_

from django.contrib import admin
from .models import User
from .models import Nav
from .models import Content
from .models import Category
from .models import Articles
from .models import Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Nav)
admin.site.register(Content)
admin.site.register(Category)
admin.site.register(Articles)
admin.site.register(Comments)
