from django.contrib import admin
from homepage.models import Post, Contact

class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []
    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields]
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'slug', 'created', 'updated', )
    list_filter = ('created', 'updated',)

    pass


class ContactAdmin(ReadOnlyAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)