from .base import BaseListView, FormViewMixin, BaseDeleteView

from core import models, tables, filters

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from django_select2 import forms as s2forms


# Expenses Categories

class ExpensesCategoriesListView(BaseListView):
    model = models.ExpenseCategory
    table_class = tables.ExpensesCategoriesTable
    filter_class = filters.ExpensesCategoriesFilter
    table_pagination = False
    create_url = reverse_lazy('expenses_categories-create')
    segment = 'Expenses Categories'


class ExpensesCategoriesCreateView(CreateView, FormViewMixin):
    model = models.ExpenseCategory
    template_name = 'generic/create.html'
    fields = ['name', 'description', 'company']
    segment = 'Expenses Categories'
    success_url = reverse_lazy('expenses_categories-list')

    widgets = {
        'company': s2forms.Select2Widget(
            choices=models.Company.objects.all(),
            attrs={"class": "form-control selectpicker form-select",
                   "data-live-search": "true", }
        )
    }


class ExpensesCategoriesUpdateView(UpdateView, FormViewMixin):
    model = models.ExpenseCategory
    template_name = 'generic/detail.html'
    fields = ['name', 'description', 'company']
    segment = 'Expenses Categories'
    success_url = reverse_lazy('expenses_categories-list')

    widgets = {
        'company': s2forms.Select2Widget(
            choices=models.Company.objects.all()),
    }


class ExpensesCategoriesDeleteView(BaseDeleteView):
    model = models.ExpenseCategory
    success_url = reverse_lazy('expenses_categories-list')


# Expenses

class ExpensesListView(BaseListView):
    model = models.Expense
    table_class = tables.ExpensesTable
    filter_class = filters.ExpensesFilter
    table_pagination = False
    create_url = reverse_lazy('expenses-create')
    segment = 'Expenses'


class ExpensesCreateView(CreateView, FormViewMixin):
    model = models.Expense
    template_name = 'generic/create.html'
    fields = ['amount', 'base_amount', 'payment_method',
              'expense_category', 'company', 'notes', 'expense_date']
    segment = 'Expenses'
    success_url = reverse_lazy('expenses-list')


class ExpensesUpdateView(UpdateView, FormViewMixin):
    model = models.Expense
    template_name = 'generic/detail.html'
    fields = ['amount', 'base_amount', 'payment_method',
              'expense_category', 'company', 'notes', 'expense_date']
    segment = 'Expenses'
    success_url = reverse_lazy('expenses-list')


class ExpensesDeleteView(BaseDeleteView):
    model = models.Expense
    success_url = reverse_lazy('expenses-list')
