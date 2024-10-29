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