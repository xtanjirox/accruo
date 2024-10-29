from django.urls import path
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
]