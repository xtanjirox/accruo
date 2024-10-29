from .base import BaseListView, FormViewMixin, BaseDeleteView

from core import models, tables, filters

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from django_select2 import forms as s2forms

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
            choices=models.Company),
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