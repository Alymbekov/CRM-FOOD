from django.db import models
# from model_utils.fields import StatusField
# from model_utils import Choices

class Table(models.Model):
    name_of_tables = models.PositiveIntegerField()


    def __str__(self):
        return '{}'.format(self.name_of_tables)
class Status(models.Model):
    # CHOICES = (
    # (True,"True"),
    # (False, "False")
    order = models.ForeignKey('Order',related_name="statuses",on_delete=models.CASCADE,null=True,blank=True)
    # PENDING = 0
    # DONE = 1
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Done'),
    )
    name_of_statuses = models.PositiveIntegerField(choices=STATUS_CHOICES,default=1)

    def __str__(self):
        return '%s' % self.name_of_statuses

class Order(models.Model):
    table = models.ForeignKey('Table',on_delete=models.CASCADE,related_name='tables')
    isitopen = models.PositiveIntegerField()
    date_of_order = models.DateTimeField(auto_now_add=True)
    # meal = models.ForeignKey()

    def __str__(self):
        return "{}".format(self.date_of_order)

class Department(models.Model):
    name_of_departments = models.CharField(max_length=155)


    def __str__(self):
        return self.name_of_departments


class Role(models.Model):
    name_of_role = models.CharField(max_length=155)

    def __str__(self):
        return self.name_of_role
# class Meal(model.Model):
#     name_of_meals = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.TextField()
#
#
# class MealCategories(models.Model):
#     name_of_categories = models.CharField(max_length=100)
#     departments = models.()




# Create your models here.
