from django_tables2 import SingleTableView
from django.forms import modelform_factory

from django.views import generic

from django.db.models import F, Q, Sum

from core import forms, models

import random
import json


def generate_color(n):
    chars = '0123456789ABCDEF'
    return ['#' + ''.join(random.sample(chars, 6)) for i in range(n)]


class BaseListView(SingleTableView):
    template_name = "generic/list.html"
    segment = None
    filter_class = None
    show_only_filtered = None
    filter = None
    entry_type = None
    create_url = None
    get_stats = None
    detail = None

    def get_queryset(self):
        if self.filter_class:
            self.filter = self.filter_class(
                self.request.GET, queryset=super().get_queryset())
            if self.show_only_filtered and not self.request.GET:
                return self.model.objects.none()
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.filter_class:
            form = forms.FilterForm(self.filter.form)
            context.update({
                'filter': self.filter,
                'helper': form.helper
            })

        context.update({
            'segment': self.segment,
            'create_url': self.create_url,
            'detail': self.detail
        })
        return context


class FormViewMixin(generic.FormView):
    model = None
    fields = []
    attrs = {}
    widgets = {}
    exclude = None
    readonly_fields = []
    segment = None
    reorder_date_fields = False

    def get_read_only_fields(self, form):
        for field in self.readonly_fields:
            form.fields[field].widget.attrs['readonly'] = True
        for field in self.attrs.keys():
            form.fields[field].widget.attrs.update(self.attrs[field])
        return form

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = modelform_factory(
                self.model, fields=self.fields, exclude=self.exclude, widgets=self.widgets)
        form = super().get_form(form_class=form_class)
        form.helper = forms.FormHelper()
        form.helper.form_tag = False
        form = self.get_read_only_fields(form)
        if self.reorder_date_fields:
            form = self._reorder_date_fields(form)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'segment': self.segment
        })
        return context


class BaseDeleteView(generic.DeleteView):
    skip_confirmation = True

    def get(self, request, *args, **kwargs):
        if self.skip_confirmation:
            return self.delete(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)
