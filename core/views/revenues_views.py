from .base import BaseListView, FormViewMixin, BaseDeleteView

from core import models, tables, filters

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from django_select2 import forms as s2forms

class RevenuesCategoriesListView(BaseListView):
    model = models.RevenueCategory
    table_class = tables.RevenuesCategoriesTable
    filter_class = filters.RevenuesCategoriesFilter
    table_pagination = False
    create_url = reverse_lazy('revenues_categories-create')
    segment = 'Revenues Categories'
    
    
class RevenuesCategoriesCreateView(CreateView, FormViewMixin):    
    model = models.RevenueCategory
    template_name = 'generic/create.html'
    fields = ['name', 'description', 'company']
    segment = 'Revenues Categories'
    success_url = reverse_lazy('revenues_categories-list')
    
    widgets = {
        'company': s2forms.Select2Widget(
            choices=models.Company.objects.all(),
            attrs={"class": "form-control selectpicker form-select", "data-live-search": "true",}
        )
    }


class RevenuesCategoriesUpdateView(UpdateView, FormViewMixin):
    model = models.RevenueCategory
    template_name = 'generic/detail.html'
    fields = ['name', 'description', 'company']
    segment = 'Revenues Categories'
    success_url = reverse_lazy('revenues_categories-list')
    
    widgets = {
        'company': s2forms.Select2Widget(
            choices=models.Company.objects.all()),
    }


class RevenuesCategoriesDeleteView(BaseDeleteView):
    model = models.RevenueCategory
    success_url = reverse_lazy('revenues_categories-list')
    
    
# Expenses

class RevenuesListView(BaseListView):
    model = models.Revenue
    table_class = tables.RevenuesTable
    filter_class = filters.RevenuesFilter
    table_pagination = False
    create_url = reverse_lazy('revenues-create')
    segment = 'Revenues'


class RevenuesCreateView(CreateView, FormViewMixin):
    model = models.Revenue
    template_name = 'generic/create.html'
    fields = ['amount', 'base_amount', 'payment_method',
              'revenue_category', 'company', 'notes', 'revenue_date']
    segment = 'Revenues'
    success_url = reverse_lazy('revenues-list')


class RevenuesUpdateView(UpdateView, FormViewMixin):
    model = models.Revenue
    template_name = 'generic/detail.html'
    fields = ['amount', 'base_amount', 'payment_method',
              'revenue_category', 'company', 'notes', 'revenue_date']
    segment = 'Revenues'
    success_url = reverse_lazy('revenues-list')


class RevenuesDeleteView(BaseDeleteView):
    model = models.Revenue
    success_url = reverse_lazy('revenues-list')
