from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TaxForm
from .models import Tax


# Create your views here.
def home(request):
    submitted = False
    if request.method == "POST":
        form = TaxForm(request.POST)
        if form.is_valid():
            form.save()
            tax = Tax.objects.latest('income', 'loan')
            if 1000 <= tax.income or tax.income <= 9680:
                taxes = int(0.1 * tax.income) -960
                netincome = tax.income - taxes - tax.loan

            elif tax.income <= 18800:
                taxes = int(0.15 * tax.income) -960
                netincome = tax.income - taxes - tax.loan

            elif tax.income <= 27920:
                taxes = int(0.2 * tax.income) -960
                netincome = tax.income - taxes - tax.loan


            elif tax.income <= 37040:
                taxes = int(0.25 * tax.income) -960
                netincome = tax.income - taxes - tax.loan

            elif tax.income > 37040:
                taxes = int(0.3 * tax.income) - 960
                netincome = tax.income - taxes - tax.loan

            return render(request, 'result.html', {'tax':tax, 'netincome':netincome, 'taxes':taxes})
        else:
            form = TaxForm
            if 'submitted' in request.GET:
                submitted = True
    form = TaxForm
    return render(request, 'home.html', {'form': form, 'submitted': submitted})

def result(request):
    tax = Tax.ojects.all
    return render(request, 'result.html', {'tax': tax})