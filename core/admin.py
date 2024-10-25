from django.contrib import admin
from core import models

admin.site.register(models.Country)
admin.site.register(models.Company)
admin.site.register(models.Currency)
admin.site.register(models.ExpenseCategory)
admin.site.register(models.Unit)
admin.site.register(models.Item)
admin.site.register(models.PaymentMethod)
admin.site.register(models.Payment)
admin.site.register(models.Expense)
admin.site.register(models.RevenueCategory)
admin.site.register(models.Revenue)
        