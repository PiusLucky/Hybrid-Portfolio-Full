from django.contrib import admin

from graphics.models import (
    Graphics_Portfolio, Graphics_Archive, 
    ArchiveFinalDesigns, AchieveMocks , FinalDesigns, 
    Mocks, Graphics_Stack, Tag
)

# for portfolio
class FinalDesignsAdmin(admin.StackedInline):
    model = FinalDesigns
class MocksAdmin(admin.StackedInline):
    model = Mocks

@admin.register(Graphics_Portfolio)
class Graphics_PortfolioAdmin(admin.ModelAdmin):
    inlines = [FinalDesignsAdmin, MocksAdmin]
    class Meta:
        model = Graphics_Portfolio

@admin.register(FinalDesigns)
class FinalDesignsAdmin(admin.ModelAdmin):
  pass

@admin.register(Mocks)
class MocksAdmin(admin.ModelAdmin):
  pass

# for archieve
class ArchiveFinalDesignsAdmin(admin.StackedInline):
    model = ArchiveFinalDesigns
class AchieveMocksAdmin(admin.StackedInline):
    model = AchieveMocks

@admin.register(Graphics_Archive)
class Graphics_ArchiveAdmin(admin.ModelAdmin):
    inlines = [ArchiveFinalDesignsAdmin, AchieveMocksAdmin]
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Graphics_Archive
        readonly_fields = 'slug'


@admin.register(ArchiveFinalDesigns)
class ArchiveFinalDesignsAdmin(admin.ModelAdmin):
  pass

@admin.register(AchieveMocks)
class AchieveMocksAdmin(admin.ModelAdmin):
  pass

# for stack
class Graphics_StackModelAdmin(admin.ModelAdmin):
    list_display = ["id", "position", "tech"]
    list_display_links = ["tech"]
    list_filter = ["tech","about_tech"]
    search_fields = ["tech","about_tech"]
    exclude = ('timestamp',)
    readonly_fields = ('timestamp',)
    class Meta:
        model = Graphics_Stack
admin.site.register(Graphics_Stack, Graphics_StackModelAdmin)


admin.site.register(Tag)
