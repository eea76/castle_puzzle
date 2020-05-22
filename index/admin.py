from django.contrib import admin

from index.models import *

class UserPaintingAdmin(admin.ModelAdmin):
    list_filter = ('user', )


class PageLoadAdmin(admin.ModelAdmin):
    list_filter = ('ip_address',)
    list_display = ('page', 'time_stamp', 'ip_address',)


class AttemptAdmin(admin.ModelAdmin):
    list_filter = ('user', )

admin.site.register(Painting)
admin.site.register(UserPainting, UserPaintingAdmin)
admin.site.register(Attempt, AttemptAdmin)
admin.site.register(Browser)
admin.site.register(OperatingSystem)
admin.site.register(PageLoad, PageLoadAdmin)
