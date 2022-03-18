from djmoney.models.fields import MoneyField
from django.db import models
import datetime

# Create your models here.

TRANSACTION_TYPES = (
    ('debit', 'Debit'),
    ('credit', 'Credit')
)

CATEGORIES = (
    ('allow', 'Allowance'),
    ('car', 'Car Expense'),
    ('cloth', 'Clothing'),
    ('ent', 'Entertainment'),
    ('fit', 'Fitness'),
    ('gro', 'Groceries'),
    ('home', 'Home Goods'),
    ('inc', 'Income'),
    ('ins', 'Insurance'),
    ('med', 'Medical'),
    ('misc', 'Miscellaneous'),
    ('mrt', 'Mortgage'),
    ('ref', 'Refund'),
    ('util', 'Utilities'),
)

PAYMENT_METHOD = (
    ('amex', 'American Express'),
    ('cash', 'Cash'),
    ('wfv', 'Wells Fargo Visa'),
    ('wfx', 'Wells Fargo Transfer'),
    ('cdv', 'Chase Disney Visa'),
)

class Budget(models.Model):
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPES)
    category =  models.CharField(max_length=100, choices=CATEGORIES)
    description = models.CharField(max_length=200)
    amount = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD)
    transaction_date = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.description