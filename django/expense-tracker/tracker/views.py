from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    if request.method == "POST":
        description = request.POST.get('description', '').strip()
        amount_str = request.POST.get('amount', '').strip()

        if not description or not amount_str:
            messages.error(request, "Please provide both description and amount")
            return redirect('/')

        try:
            amount = float(amount_str)
        except ValueError:
            messages.error(request, "Invalid amount")
            return redirect('/')


        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
        expense_type = "CREDIT"
        if float(amount) < 0:
            expense_type = "DEBIT"

        if float(amount) == 0:
            messages.success(request, "Amount cannot be zero") 
            return redirect('/')

        tracking_history = TrackingHistory.objects.create(amount = amount,
            expense_type = expense_type,
            current_balance = current_balance,
            description = description)
        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()
        print(description,amount)
        return redirect('/')
    
    current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
    income = 0
    expense = 0
    
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == "CREDIT":
            income += tracking_history.amount
        else:
            expense += tracking_history.amount

    context = {'income' : income,
                'expense' : expense , 
                'transactions' : TrackingHistory.objects.all() , 'current_balance' : current_balance}
    return render(request, 'index.html' , context)
    
def delete_transaction(request, id):
    tracking_history = TrackingHistory.objects.filter(id = id)

    if tracking_history.exists():
        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
        tracking_history = tracking_history[0]
        
        current_balance.current_balance = current_balance.current_balance - tracking_history.amount

        current_balance.save()


    tracking_history.delete()
    return redirect('/')
