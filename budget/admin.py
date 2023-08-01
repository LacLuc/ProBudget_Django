from django.contrib import admin

from .models import (aporty, buylist, category, credity, expense, expensetype,
                     fontpayer, monthYear, paytype, recipe)


class CategoryAdmin(admin.ModelAdmin):
    ...


class MonthYearAdmin(admin.ModelAdmin):
    ...


class fontpayerAdmin(admin.ModelAdmin):
    ...


class expensetypeAdmin(admin.ModelAdmin):
    ...


class paytypeAdmin(admin.ModelAdmin):
    ...


class aportyAdmin(admin.ModelAdmin):
    ...


class credityAdmin(admin.ModelAdmin):
    ...


class expenseAdmin(admin.ModelAdmin):
    ...


class buylistAdmin(admin.ModelAdmin):
    ...


class recipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(monthYear, MonthYearAdmin)

admin.site.register(category, CategoryAdmin)

admin.site.register(fontpayer, fontpayerAdmin)

admin.site.register(expensetype, expensetypeAdmin)

admin.site.register(paytype, paytypeAdmin)

admin.site.register(aporty, aportyAdmin)

admin.site.register(credity, credityAdmin)

admin.site.register(expense, expenseAdmin)

admin.site.register(buylist, buylistAdmin)

admin.site.register(recipe, recipeAdmin)
