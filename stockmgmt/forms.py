from django import forms
from .models import *


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Category','Product_Name','Product_Code','Quantity','Product_Buy_Price','Product_Seles_Price','Alert_Level']

    def clean_category(self):
        category = self.cleaned_data.get('Category')

        if not category:
            raise forms.ValidationError('This field is required')    

          
     #   for instance in Stock.objects.all():
     #       if instance.category == category:
     #          raise forms.ValidationError(str(category) + ' is already created')
    
        return category


    def clean_item_name(self):
        item_name = self.cleaned_data.get('Product_Name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name       

class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta:
        model = Stock
        fields = ['Product_Name', 'start_date', 'end_date']   


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Category', 'Product_Code','Product_Name', 'Quantity']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issue_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity', 'receive_by']        

class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Alert_Level']        
 

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Customer_Name','Customer_Gender','Customer_Mobile','Customer_Address','Customer_Email']

class CustomerSearchForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Customer_Name'] 

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Customer_Name','Customer_Gender','Customer_Mobile','Customer_Address','Customer_Email']


class InvoiceForm(forms.ModelForm):
    invoice_date = forms.DateTimeField(required=False)
    class Meta:
        model = Invoice
        fields = ['Name', 'phone_number','invoice_number',
                'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
                'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
                'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
                'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price',
                'line_six', 'line_six_quantity', 'line_six_unit_price', 'line_six_total_price',
                'line_seven', 'line_seven_quantity', 'line_seven_unit_price', 'line_seven_total_price',
                'line_eight', 'line_eight_quantity', 'line_eight_unit_price', 'line_eight_total_price',
                'line_nine', 'line_nine_quantity', 'line_nine_unit_price', 'line_nine_total_price',
                'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price',
                'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price',
                'line_elaven', 'line_elaven_quantity', 'line_elaven_unit_price', 'line_elaven_total_price',
                'total','balance','Due_amount','Net_amount','paid', 'invoice_type'
                ]        

def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number


def clean_name(self):
        name = self.cleaned_data.get('Name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name


class InvoiceSearchForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'Name']

class InvoiceUpdateForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ['Name', 'phone_number','invoice_number',
                'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
                'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
                'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
                'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price',
                'line_six', 'line_six_quantity', 'line_six_unit_price', 'line_six_total_price',
                'line_seven', 'line_seven_quantity', 'line_seven_unit_price', 'line_seven_total_price',
                'line_eight', 'line_eight_quantity', 'line_eight_unit_price', 'line_eight_total_price',
                'line_nine', 'line_nine_quantity', 'line_nine_unit_price', 'line_nine_total_price',
                'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price',
                'line_elaven', 'line_elaven_quantity', 'line_elaven_unit_price', 'line_elaven_total_price',
                'total','balance','Due_amount','Net_amount','paid', 'invoice_type'
                ]              


class Daily_accountsForm(forms.ModelForm):
    #date = forms.DateTimeField(required=False)
    class Meta:
        model = daily_accounts
        fields = ['Payment_type','Transcation_to','Transcation_by','Debit','Credit','Balance','Expense_reason']

class daily_accountsSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta:
        model = daily_accounts
        fields = ['Transcation_to','start_date', 'end_date']  

class daily_accountsUpdateForm(forms.ModelForm):
    class Meta:
        model = daily_accounts()
        fields = ['Payment_type','Transcation_to','Transcation_by','Debit','Credit','Balance','Expense_reason']
