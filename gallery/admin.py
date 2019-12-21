from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Post
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = "Spring Zephyr"
admin.site.site_title = ""
admin.site.index_title = "Photographer, Designer & ITsupervisor"

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'image_type', 'image', 'date_posted')
	search_fields = ('title', 'image_type',)
	list_filter = ['image_type', 'date_posted']

admin.site.register(Post, PostAdmin)