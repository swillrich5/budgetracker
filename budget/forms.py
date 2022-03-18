from django.forms import ModelForm
from .models import Budget

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['transaction_type', 'category', 'description', 'amount', 'payment_method', 'transaction_date']