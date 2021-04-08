from django.contrib import admin


from web_panel.models import ParsingResults

class ParsingResultsAdmin(admin.ModelAdmin):
    list_display = ['date', 'slot_1', 'slot_2', 'slot_3']

admin.site.register(ParsingResults, ParsingResultsAdmin)
