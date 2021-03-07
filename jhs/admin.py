from django.contrib import admin
from jhs.models import Company

# Register your models here.
# admin.site.register(Company)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'interest_level',
                    'system', 'entered', 'entry_sheet')  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目


admin.site.register(Company, CompanyAdmin)
