import django_filters
from . import models
from django_select2 import forms as s2forms
from django import forms


class ExpensesCategoriesFilter(django_filters.FilterSet):
    name = django_filters.ModelChoiceFilter(
        queryset=models.ExpenseCategory.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            attrs={"class": "col-12"},
            model=models.ExpenseCategory,
            search_fields=['name__icontains']))

    class Meta:
        model = models.ExpenseCategory
        fields = ['name']
        

class RevenuesCategoriesFilter(django_filters.FilterSet):
    name = django_filters.ModelChoiceFilter(
        queryset=models.RevenueCategory.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            attrs={"class": "col-12"},
            model=models.RevenueCategory,
            search_fields=['name__icontains']))

    class Meta:
        model = models.RevenueCategory
        fields = ['name']
        

class ExpensesFilter(django_filters.FilterSet):
    class Meta:
        model = models.Expense
        fields = ['unique_hash', 'expense_date', 'expense_category', 'company', 'payment_method']
        
        
class RevenuesFilter(django_filters.FilterSet):
    class Meta:
        model = models.Revenue
        fields = ['unique_hash', 'revenue_date', 'revenue_category', 'company', 'payment_method']
        