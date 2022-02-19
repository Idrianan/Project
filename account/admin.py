from django.contrib import admin
from .models import Themes
from .models import Forums
from .models import Post

admin.site.register(Themes)
admin.site.register(Forums)
admin.site.register(Post)