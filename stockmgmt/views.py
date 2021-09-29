from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from django.contrib import messages
from .models import Stock
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    title = 'Welcome: BD Pocket Bazar Inventory Management System'
    context = {
        "title": title,
    }
    return render(request, "home.html", context)
    # return redirect('/list_items')


@login_required
def list_items(request):
    title = 'List of Items'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':

        queryset = Stock.objects.filter(Product_Name__icontains=form['Product_Name'].value(),
                                        last_updated__range=[form['start_date'].value(),
                                                             form['end_date'].value(
                                        )
        ]
        )

        if form['export_to_CSV'].value() == True:

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'PRODUCT CODE',
                            'PRODUCT NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:

                writer.writerow(
                    [stock.Category, stock.Product_Code, stock.Product_Name, stock.Quantity])
            return response

        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request, "list_items.html", context)


@login_required
def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Saved Successfully')
        return redirect('/list_items')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)


@login_required
def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully ')
            return redirect('/list_items')

    context = {
        'form': form
    }
    return render(request, 'add_items.html', context)


@login_required
def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully ')
        return redirect('/list_items')
    return render(request, 'delete_items.html')


def stock_detail(request, pk):
    queryset = Stock.objects.get(id=pk)
    context = {
        "title": queryset.Product_Name,
        "queryset": queryset,
    }
    return render(request, "stock_details.html", context)


def receive_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.Quantity += instance.receive_quantity
        instance.save()
        messages.success(request, "Received SUCCESSFULLY. " + str(
            instance.Quantity) + " " + str(instance.Product_Name)+"s now in Store")

        return redirect('/stock_details' + str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": 'Reaceive ' + str(queryset.Product_Name),
        "instance": queryset,
        "form": form,
        "username": 'Receive By: ' + str(request.user),
    }
    return render(request, "add_items.html", context)


def reorder_level(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Alert level for " + str(instance.Product_Name) +
                         " is updated to " + str(instance.Alert_Level))

        return redirect("/list_items")
    context = {
        "instance": queryset,
        "form": form,
    }
    return render(request, "add_items.html", context)


@login_required
def list_customer(request):
    title = 'List of customer'
    form = CustomerSearchForm(request.POST or None)
    queryset = Customer.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':

        queryset = Customer.objects.filter(
            Customer_Name__icontains=form['Customer_Name'].value())

        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request, "list_customer.html", context)


@login_required
def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Saved Successfully')
        return redirect('/list_customer')
    context = {
        "form": form,
        "title": "Add cutomer",
    }
    return render(request, "add_customer.html", context)


@login_required
def update_customer(request, pk):
    queryset = Customer.objects.get(id=pk)
    form = CustomerUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully ')
            return redirect('/list_customer')

    context = {
        'form': form
    }
    return render(request, 'add_customer.html', context)


@login_required
def delete_customer(request, pk):
    queryset = Customer.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully ')
        return redirect('/list_customer')
    return render(request, 'delete_customer.html')


def customer_detail(request, pk):
    queryset = Customer.objects.get(id=pk)
    context = {
        "title": queryset.Customer_Name,
        "queryset": queryset,
    }
    return render(request, "customer_details.html", context)


def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_invoice')
    context = {
        "form": form,
        "title": "New Invoice",
    }
    return render(request, "add_invoice.html", context)


@login_required
def list_invoice(request):
    title = 'List of Invoice'
    form = InvoiceSearchForm(request.POST or None)
    queryset = Invoice.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':

        queryset = Invoice.objects.filter(invoice_number__icontains=form['invoice_number'].value(),
                                          Name__icontains=form['Name'].value()
                                          )

        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request, "list_invoice.html", context)


@login_required
def update_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully ')
            return redirect('/list_invoice')

    context = {
        'form': form
    }
    return render(request, 'add_invoice.html', context)


@login_required
def delete_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully ')
        return redirect('/list_invoice')
    return render(request, 'delete_invoice.html')


def invoice_detail(request, pk):
    queryset = Invoice.objects.get(id=pk)
    context = {
        "title": queryset.Name,
        "queryset": queryset,
    }
    return render(request, "invoice_details.html", context)


def add_daily_accounts(request):
    form = Daily_accountsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_daily_accounts')
    context = {
        "form": form,
        "title": "Daily Accounts",
    }
    return render(request, "add_daily_accounts.html", context)


@login_required
def list_daily_accounts(request):
    title = 'LIST OF Daily Expense'
    form = daily_accountsSearchForm(request.POST or None)
    queryset = daily_accounts.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':

        queryset = daily_accounts.objects.filter(Transcation_to__icontains=form['Transcation_to'].value(),
                                                 date__range=[form['start_date'].value(),
                                                              form['end_date'].value()
        ]

        )

        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request, "list_daily_accounts.html", context)


def daily_accounts_details(request, pk):
    queryset = daily_accounts.objects.get(id=pk)
    context = {
        "title": queryset.Balance,
        "queryset": queryset,
    }
    return render(request, "daily_accounts_details.html", context)


@login_required
def update_daily_accounts(request, pk):
    queryset = dailly_accounts.objects.get(id=pk)
    form = daily_accountsUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = daily_accountsUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully ')
            return redirect('/list_daily_accounts')

    context = {
        'form': form
    }
    return render(request, 'add_daily_accounts.html', context)


@login_required
def delete_daily_accounts(request, pk):
    queryset = daily_accounts.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully ')
        return redirect('/list_daily_accounts')
    return render(request, 'delete_daily_accounts.html')