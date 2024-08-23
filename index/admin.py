from django.contrib import admin

from index.models import *


class UserPaintingAdmin(admin.ModelAdmin):
    list_filter = ('user', )


class PageLoadAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = ('page', 'user', 'time_stamp',)


class AttemptAdmin(admin.ModelAdmin):
    list_filter = ('user', )

class PaintingPerRoomAdmin(admin.ModelAdmin):
    list_filter = ('room',)


admin.site.register(Painting)
admin.site.register(Room)
admin.site.register(PaintingPerRoom, PaintingPerRoomAdmin)
admin.site.register(UserPainting, UserPaintingAdmin)
admin.site.register(Link)
admin.site.register(Attempt, AttemptAdmin)
admin.site.register(Browser)
admin.site.register(OperatingSystem)
admin.site.register(PageLoad, PageLoadAdmin)
