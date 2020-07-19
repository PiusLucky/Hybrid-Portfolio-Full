from django.contrib import admin
from main.models import Portfolio, Stack, Archive, Contact


class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ["id","position", "github", "link"]
    list_display_links = ["id"]
    list_editable = ["position", "github","link"]
    list_filter = ["position"]
    search_fields = ["id","position", "github","link"]
    class Meta:
        model = Portfolio
admin.site.register(Portfolio, PortfolioModelAdmin)


class StackModelAdmin(admin.ModelAdmin):
    list_display = ["id", "position", "tech"]
    list_display_links = ["tech"]
    list_filter = ["tech","about_tech"]
    search_fields = ["tech","about_tech"]
    exclude = ('timestamp',)
    readonly_fields = ('timestamp',)
    class Meta:
        model = Stack
admin.site.register(Stack, StackModelAdmin)


class ArchiveModelAdmin(admin.ModelAdmin):
    list_display = ["id", "position", "title", "description", "backend_tech"]
    list_editable = ["position", "title", "description","backend_tech"]
    list_filter = ["title", "description" ]
    search_fields = ["id","title", "description","github", "external_link"]
    class Meta:
        model = Archive
admin.site.register(Archive, ArchiveModelAdmin)


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["id","name", "email", "timestamp"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["id","name", "email"]
    class Meta:
        model = Contact
admin.site.register(Contact, ContactModelAdmin)


