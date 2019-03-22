from django.db import models
# from model_utils.fields import StatusField
# from model_utils import Choices

class Table(models.Model):
    name_of_tables = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name_of_tables)

class Status(models.Model):
    # CHOICES = (
    # (True,"True"),
    # (False, "False")
    # order = models.ForeignKey('Order',related_name="statuses",on_delete=models.CASCADE,null=True,blank=True)
    # PENDING = 0
    # DONE = 1
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Done'),
    )
    name_of_statuses = models.PositiveIntegerField(choices=STATUS_CHOICES,default=1,max_length=255)

    def __str__(self):
        return '%s' % self.name_of_statuses


class Department(models.Model):
    name_of_departments = models.CharField(max_length=155)


    def __str__(self):
        return self.name_of_departments


class Role(models.Model):
    name_of_role = models.CharField(max_length=155)

    def __str__(self):
        return self.name_of_role


class Order(models.Model):
    #meals = models.ManyToManyField('Meal',related_name="orders",blank=True)
    table = models.ForeignKey('Table',on_delete=models.SET_NULL,related_name='orders',null=True,blank=True)
    status = models.ForeignKey('Status',related_name="orders",on_delete=models.CASCADE,null=True,blank=True)
    isitopen = models.PositiveIntegerField()
    date_of_order = models.DateTimeField(auto_now_add=True)
    order_items = models.ForeignKey('OrderItem',related_name="orders",on_delete=models.CASCADE,null=True,blank=True)
    # meal = models.ForeignKey()

    def __str__(self):
        return "{} {} {}".format(self.date_of_order,self.table,self.status)


class OrderItem(models.Model):

    meals = models.ForeignKey('Meal',related_name='orders_item',on_delete=models.SET_NULL,null=True,blank=True)
    count = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return '%s %s' % (self.meals,self.count)

class Meal(models.Model):

    name_of_meals = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.PositiveSmallIntegerField(default=1)
    description = models.TextField()
    category = models.ForeignKey('MealCategory',on_delete=models.CASCADE,related_name="meals",null=True,blank=True)


    def __str__(self):
        return self.name_of_meals

#
class MealCategory(models.Model):
    CHOICES = (
        (1,"Первые блюда"),
        (2,"Вторые блюда"),
        (3,"Напитки"),
        (4,"Десерты"),
        (5,"Алкоголь"),
    )
    name_of_categories = models.PositiveIntegerField(choices=CHOICES,default=1)
    departments = models.ForeignKey('Department',on_delete=models.SET_NULL,related_name="mealcategories",null=True,blank=True)


    def __str__(self):
        return '%s' % self.name_of_categories


class ServicePercentage:
    name = models.PositiveIntegerField()


    def __str__(self):

        return self.name


class Checks(models.Model):

    orders = models.OneToOneField('Order',on_delete=models.CASCADE)
    date_of_check = models.DateTimeField(auto_now_add=True)
    service_fee = models.PositiveSmallIntegerField(default=1)
    total_sum = models.FloatField()

    def __str__(self):
        return "{} {} {} {}".format(self.orders,self.date_of_check,self.service_fee,self.total_sum)
# Create your models here.
