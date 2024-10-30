from django.urls import path, include
from . import views


urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'orders', views.orders, name='list_orders'),
    path(r'orders/create', views.orders, name='create_orders'),
    
    # Expenses Catrgories model urls 
    path(r'expenses_categories', views.ExpensesCategoriesListView.as_view(), name='expenses_categories-list'),
    path(r'expenses_categories/create', views.ExpensesCategoriesCreateView.as_view(), name='expenses_categories-create'),
    path(r'expenses_categories/update/<pk>', views.ExpensesCategoriesUpdateView.as_view(), name='expenses_categories-update'),
    path(r'expenses_categories/delete/<pk>', views.ExpensesCategoriesDeleteView.as_view(), name='expenses_categories-delete'),
    
     # Expenses model urls 
    path(r'expenses', views.ExpensesListView.as_view(), name='expenses-list'),
    path(r'expenses/create', views.ExpensesCreateView.as_view(), name='expenses-create'),
    path(r'expenses/update/<pk>', views.ExpensesUpdateView.as_view(), name='expenses-update'),
    path(r'expenses/delete/<pk>', views.ExpensesDeleteView.as_view(), name='expenses-delete'),
    
    
    # Revenues Catrgories model urls 
    path(r'revenues_categories', views.RevenuesCategoriesListView.as_view(), name='revenues_categories-list'),
    path(r'revenues_categories/create', views.RevenuesCategoriesCreateView.as_view(), name='revenues_categories-create'),
    path(r'revenues_categories/update/<pk>', views.RevenuesCategoriesUpdateView.as_view(), name='revenues_categories-update'),
    path(r'revenues_categories/delete/<pk>', views.RevenuesCategoriesDeleteView.as_view(), name='revenues_categories-delete'),
    
    # Revenues model urls 
    path(r'revenues', views.RevenuesListView.as_view(), name='revenues-list'),
    path(r'revenues/create', views.RevenuesCreateView.as_view(), name='revenues-create'),
    path(r'revenues/update/<pk>', views.RevenuesUpdateView.as_view(), name='revenues-update'),
    path(r'revenues/delete/<pk>', views.RevenuesDeleteView.as_view(), name='revenues-delete'),
]