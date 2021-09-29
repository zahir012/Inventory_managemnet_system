from django.db import models

# Create your models here.

gender_choice = (
                ('Male', 'Male'),
                ('Female', 'Female'),
                ('Other', 'Other'),
)


class Customer(models.Model):
    Customer_Name = models.CharField(max_length=50, blank=True, null=True)
    Customer_Gender = models.CharField(
        max_length=50, blank=True, null=True, choices=gender_choice)
    Customer_Mobile = models.CharField(max_length=40, blank=True, null=True)
    Customer_Address = models.CharField(max_length=30, blank=True, null=True)
    Customer_Email = models.EmailField(max_length=20, blank=True, null=True)
    Customer_Due = models.IntegerField(blank=True, null=True)
    Receipt_Type = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.Customer_Name


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    Product_Code = models.CharField(max_length=50, blank=False, null=True)
    Product_Name = models.CharField(max_length=50, blank=True, null=True)
    Quantity = models.IntegerField(default='0', blank=True, null=True)
    Product_Buy_Price = models.IntegerField(default='0', blank=True, null=True)
    Product_Seles_Price = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    Alert_Level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False,null=True)

    #export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.Product_Name

class Invoice(models.Model):
    comments = models.TextField(max_length=3000, default='', blank=True, null=True)
    invoice_number = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    Name = models.CharField(max_length=20,blank=True,null=True)
    
    line_one = models.CharField('Line 1', max_length=120, default='', blank=True, null=True)
    line_one_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_one_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_one_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_two = models.CharField('Line 2', max_length=120, default='', blank=True, null=True)
    line_two_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_two_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_two_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_three = models.CharField('Line 3', max_length=120, default='', blank=True, null=True)
    line_three_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_three_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_three_total_price = models.IntegerField('Line Total (tk', default=0, blank=True, null=True)

    line_four = models.CharField('Line 4', max_length=120, default='', blank=True, null=True)
    line_four_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_four_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_four_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_five = models.CharField('Line 5', max_length=120, default='', blank=True, null=True)
    line_five_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_five_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_five_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    ine_six = models.CharField('Line 6', max_length=120, default='', blank=True, null=True)
    line_one_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_one_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_one_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_seveen = models.CharField('Line 7', max_length=120, default='', blank=True, null=True)
    line_two_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_two_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_two_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_eight = models.CharField('Line 8', max_length=120, default='', blank=True, null=True)
    line_three_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_three_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_three_total_price = models.IntegerField('Line Total (tk', default=0, blank=True, null=True)

    line_nine = models.CharField('Line 9', max_length=120, default='', blank=True, null=True)
    line_four_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_four_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_four_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_ten = models.CharField('Line 10', max_length=120, default='', blank=True, null=True)
    line_five_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_five_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_five_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)
    line_six = models.CharField('Line 6', max_length=120, default='', blank=True, null=True)
    line_six_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_six_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_six_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_seven = models.CharField('Line 7', max_length=120, default='', blank=True, null=True)
    line_seven_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_seven_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_seven_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_eight = models.CharField('Line 8', max_length=120, default='', blank=True, null=True)
    line_eight_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_eight_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_eight_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_nine = models.CharField('Line 9', max_length=120, default='', blank=True, null=True)
    line_nine_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_nine_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_nine_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_ten = models.CharField('Line 10', max_length=120, default='', blank=True, null=True)
    line_ten_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_ten_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_ten_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    line_elaven = models.CharField('line 11', max_length=120, default='', blank=True, null=True)
    line_elaven_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_elaven_unit_price = models.IntegerField('Unit Price (tk)', default=0, blank=True, null=True)
    line_elaven_total_price = models.IntegerField('Line Total (tk)', default=0, blank=True, null=True)

    phone_number = models.CharField(max_length=120, default='', blank=True, null=True)
    total = models.IntegerField(default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    Due_amount = models.IntegerField(default='0',blank=True,null=True)
    Net_amount = models.IntegerField(default='0',blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
            ('Receipt', 'Receipt'),
            ('Proforma Invoice', 'Proforma Invoice'),
            ('Invoice', 'Invoice'),
        )
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

    def __str__(self):
        return self.invoice_number


class daily_accounts(models.Model):

    date = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True,null=True)
    type_payment_choice = (

        ('Cash','Cash'),
        ('Receipt','Receipt'),
        ('Cheque','cheque'),
        ('Balance Transfer','Balance Transfer'),

    )

    Payment_type = models.CharField(max_length=20,default='',blank=True,null=True,choices=type_payment_choice)
    Transcation_to = models.CharField(max_length=30, blank=False,null=True)
    Transcation_by = models.CharField(max_length=30,blank=False,null=True)
    Expense_reason = models.TextField(max_length=250,blank=False,null=True)
    Debit = models.IntegerField(default='0',blank=True,null=True)  
    Credit = models.IntegerField(default='0',blank=False,null=True)
    Balance = models.IntegerField(default='0',blank=False,null=True)

    def __str__(self):
        return self.Balance