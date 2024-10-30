import django_tables2 as tables
from . import models

ACTIONS_BUTTONS_TEMPLATE = """
    <a href="{{record.get_absolute_url}}"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>
    <a href="{{record.get_delete_url}}"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a>
"""

DEFAULT_TABLE_ATTRS = {
    "id": "datatables-orders",
    "class": "table table-responsive table-striped dataTable no-footer dtr-inline",
    "width": "100%",
    "aria - describedby": "datatables-orders_info",
    "style": "width: 100%;"
}


class ExpensesCategoriesTable(tables.Table):
    actions = tables.TemplateColumn(ACTIONS_BUTTONS_TEMPLATE)

    class Meta:
        model = models.ExpenseCategory
        attrs = DEFAULT_TABLE_ATTRS
        fields = ('id', 'name', 'description', 'actions')
        

class RevenuesCategoriesTable(tables.Table):
    actions = tables.TemplateColumn(ACTIONS_BUTTONS_TEMPLATE)

    class Meta:
        model = models.RevenueCategory
        attrs = DEFAULT_TABLE_ATTRS
        fields = ('id', 'name', 'description', 'actions')
        

class ExpensesTable(tables.Table):
    actions = tables.TemplateColumn(ACTIONS_BUTTONS_TEMPLATE)

    class Meta:
        model = models.Expense
        attrs = DEFAULT_TABLE_ATTRS
        fields = ('id', 'expense_date', 'amount', 'expense_category', 
                  'company', 'base_amount', 'payment_method', 'actions')
        
        
class RevenuesTable(tables.Table):
    actions = tables.TemplateColumn(ACTIONS_BUTTONS_TEMPLATE)

    class Meta:
        model = models.Revenue
        attrs = DEFAULT_TABLE_ATTRS
        fields = ('id', 'revenue_date', 'amount', 'revenue_category', 
                  'company', 'base_amount', 'payment_method', 'actions')