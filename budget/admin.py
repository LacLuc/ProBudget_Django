from django.contrib import admin

from .models import category, monthYear


class CategoryAdmin(admin.ModelAdmin):
    ...


class MonthYearAdmin(admin.ModelAdmin):
    ...


admin.site.register(category, CategoryAdmin)

admin.site.register(monthYear, MonthYearAdmin)