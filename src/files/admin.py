from django.contrib import admin
from .models import FileItem
from django.utils.html import format_html

class PageAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'upload_url', 'timestamp', 'updated', 'description', 'download')
	list_display_links = ('name', 'upload_url', 'download')
	search_fields = ('name',)
	list_per_page = 25

	def upload_url(self, obj):
        	return format_html('<a href="%s%s">Upload files</a>' % ('http://www.awscloudservice.com:8000/upload/', obj.url))
	upload_url.allow_tags = True
	upload_url.short_description = 'Upload files'

admin.site.register(FileItem, PageAdmin)
