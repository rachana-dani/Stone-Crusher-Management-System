from django.db import models
# from phone_field import PhoneField
from django.utils import timezone
from django.core.validators import RegexValidator

class StoneType(models.Model):
    stone_type = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.stone_type

class AuthorizedUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=4, validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')])

class Worker(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    date_of_joining = models.DateTimeField()
    mobile = models.DecimalField(null=False, blank=False, unique=True,max_digits=10,decimal_places=0)
    aadhar_number = models.CharField(max_length=50,validators=[RegexValidator(regex='^.{12}$', message='Length has to be 4', code='nomatch')])
    salary = models.DecimalField(decimal_places=2,max_digits=10)
    account_number = models.DecimalField(decimal_places=2,max_digits=18, blank=True)
    photo = models.ImageField(default=None)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.name

class DieselStock(models.Model):
    quantity = models.DecimalField(max_digits=10,decimal_places=2,null=True,default=0)
    quantity_remaining = models.DecimalField(max_digits=10,decimal_places=2,null=True,default=0)
    cost = models.DecimalField(max_digits=10,decimal_places=2,null=True,default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "DS_"+ str(self.id)

class Bill(models.Model):
    ch = (
        (0,"Electricity"),
        (1,"Water")
    )
    categories = models.IntegerField(choices=ch)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    pay_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ch[self.categories][1]

class AdvPay(models.Model):
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    amount_given = models.DecimalField(decimal_places=5,null=True,max_digits=10,default=0)
    amount_paid = models.DecimalField(decimal_places=5,null=True,max_digits=10,default=0)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.worker)+"_Adv"

class CustomerDetail(models.Model):
    name = models.CharField(max_length=30)
    phone_number=models.IntegerField(null=False, blank=False, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name

class Resource(models.Model):
    resource_type =  models.CharField(max_length=100)
    purchase_date = models.DateTimeField()
    purchase_cost = models.DecimalField(decimal_places=2,max_digits=10)
    rto_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.resource_type)+"_"+ str(self.rto_number)

class SaleBill(models.Model):
    date = models.DateTimeField(default=timezone.now)
    bill_num = models.CharField(max_length=10)
    customer = models.ForeignKey(CustomerDetail, on_delete=models.DO_NOTHING)
    total_amt = models.DecimalField(decimal_places=2,max_digits=10)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return str(self.bill_num)


class SaleLog(models.Model):
    v_num = models.ForeignKey(Resource,on_delete=models.CASCADE)
    stone_type = models.ForeignKey(StoneType,on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(decimal_places=2,max_digits=10)
    delivery_worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
    diesel_stock_name = models.ForeignKey(DieselStock,on_delete=models.CASCADE,null=True)
    desiel_spent = models.DecimalField(max_digits=10,decimal_places=2)
    sale_bill = models.ForeignKey(SaleBill,on_delete=models.CASCADE)  

    def __str__(self):
        return "Sale"+ str(self.id)
        
class Stock(models.Model):
    stone_type = (
        (0,"dust"),
        (6,"6mm",),
        (10,"10mm"),
        (20,"20mm"),
        (30,"30mm")
    )
    date = models.DateTimeField()
    quantity = models.DecimalField(decimal_places=2,max_digits=10)
    stone_type = models.IntegerField(choices=stone_type)

    def __str__(self):
        return str(self.id) + "stock"
    
class BlastingDetail(models.Model):
    area = models.CharField(max_length=100)
    supervisor = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
    diesel_stock_name = models.ForeignKey(DieselStock,on_delete=models.CASCADE)
    diesel_spent = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    cost = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.area + "_ID:" + str(self.id)


class ResourceMaintenance(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.DO_NOTHING)
    cost = models.DecimalField(decimal_places=2,max_digits=10)
    description = models.CharField(max_length=200)

    def __str__(self):
        return "RM_"+ str(self.id)

class FoodExp(models.Model):
    foods = (
        (0,"Grains"),
        (1,"Gas"),
        (2,"Vegetable"),
    )
    category = models.IntegerField(choices=foods)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    purchase_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.foods[self.category][1]

