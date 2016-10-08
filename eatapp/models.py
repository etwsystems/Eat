from django.db import models

# Create your models here.

class Customer(models.Model):
    customerno = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    totalspent = models.DecimalField(max_digits=7, decimal_places=2)
    password = models.CharField(max_length=15)


    def __str__ (self):
       return self.name


class Restaurants(models.Model):
    resno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    resdescription = models.TextField()
    last_modified_date = models.DateField()
    rescode = models.CharField(max_length=100)
    respassword = models.CharField(max_length=100)

    def __str__ (self):
       return self.name 

class Categories(models.Model):
    categoriesno = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    resno = models.ForeignKey(Restaurants, on_delete=models.CASCADE)

    def __str__ (self):
       return self.category 

def upload_location(instance, filename):
  return "%s/%s" %(instance.itemno, filename)

class Menus(models.Model):
   itemno = models.IntegerField(primary_key=True)
   itemname = models.CharField(max_length=100)
   resno = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
   itemdescription = models.TextField(null=True)
   itemimage = models.ImageField(upload_to=upload_location, blank=True, null=True, width_field="", height_field="",)
   itemprice = models.DecimalField(max_digits=6, decimal_places=2)
   categoriesno = models.ForeignKey(Categories, on_delete=models.CASCADE)

   def __str__ (self):
       return self.itemname 



class Orders(models.Model):
    orderno = models.IntegerField(primary_key=True)
    orderdate = models.DateField()
    customerno = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orderamount = models.DecimalField(max_digits=6, decimal_places=2)
    orderend = models.CharField(max_length=100)
    resno = models.ForeignKey(Restaurants, on_delete=models.CASCADE)

    def __str__ (self):
       return self.orderno 

class OrderDetails(models.Model):
    orderdetailsno = models.IntegerField(primary_key=True)
    orderno = models.ForeignKey(Orders, on_delete=models.CASCADE)
    itemno = models.ForeignKey(Menus)
    quantity = models.DecimalField(max_digits=50, decimal_places=2)
    resno = models.ForeignKey(Restaurants,on_delete= models.CASCADE)

    def __str__ (self):
       return self.orderdetailsno 



