from .base_models import BaseModel
from django.db import models
from django.utils import timezone

from core import utils


class Country(BaseModel):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    phonecode = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        
    
class Company(BaseModel):
    name = models.CharField(max_length=100)
    unique_hash = models.CharField(max_length=100, blank=True, unique=True)
    slug = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    
    def save(self, *args, **kwargs):
        if not self.unique_hash:
            self.unique_hash = utils.generate_unique_hash()
        super(Company, self).save(*args, **kwargs)


class Currency(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=10)
    precision = models.IntegerField(default=2)
    thousand_separator = models.CharField(max_length=10, default=',')
    decimal_separator = models.CharField(max_length=10, default='.')
    swap_currency_symbol = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class ExpenseCategory(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ExpenseCategory'
        verbose_name_plural = 'ExpenseCategories'


class Unit(BaseModel):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        unique_together = ('name', 'company')


class Item(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    # created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class PaymentMethod(BaseModel):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    settings = models.CharField(max_length=100, null=True, blank=True)
    driver = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PaymentMethod'
        verbose_name_plural = 'PaymentMethods'
        unique_together = ('name', 'company')


class Payment(BaseModel):
    sequence_number = models.IntegerField(default=0)
    customer_sequence_number = models.IntegerField(default=0)
    payment_number = models.CharField(max_length=100)
    payment_date = models.DateTimeField(default=timezone.now)
    notes = models.CharField(max_length=100, null=True, blank=True)
    amount = models.FloatField(default=0)
    unique_hash = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    # created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    exchange_rate = models.FloatField(default=0)
    base_amount = models.FloatField(default=0)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)

    def __str__(self):
        return self.payment_number

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'


class Expense(BaseModel):
    unique_hash = models.CharField(max_length=100, blank=True, null=True)
    expense_date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField(default=0)
    notes = models.CharField(max_length=100, null=True, blank=True)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    # creator = models.ForeignKey('users.User', on_delete=models.CASCADE)
    base_amount = models.FloatField(default=0)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    def __str__(self):
        return self.unique_hash

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        
        
    def save(self, *args, **kwargs):
        if not self.unique_hash:
            self.unique_hash = utils.generate_unique_hash()
        super(Expense, self).save(*args, **kwargs)


class RevenueCategory(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'RevenueCategory'
        verbose_name_plural = 'RevenueCategories'
        
        
class Revenue(BaseModel):
    unique_hash = models.CharField(max_length=100, blank=True, null=True)
    revenue_date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField(default=0)
    notes = models.CharField(max_length=100, null=True, blank=True)
    expense_category = models.ForeignKey(RevenueCategory, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    # creator = models.ForeignKey('users.User', on_delete=models.CASCADE)
    base_amount = models.FloatField(default=0)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    def __str__(self):
        return self.unique_hash

    class Meta:
        verbose_name = 'Revenue'
        verbose_name_plural = 'Revenues' 
    
    def save(self, *args, **kwargs):
        if not self.unique_hash:
            self.unique_hash = utils.generate_unique_hash()
        super(Revenue, self).save(*args, **kwargs)
        
