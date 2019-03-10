# from django.db import models
#
#
# class Table(models.Model):
#     name_of_tables = models.PositiveIntegerField()
#
#
#     def __str__(self):
#         return self.name_of_tables
#
#
# class Order(models.Model):
#     tables = models.ForeignKey()
#     status = models.BooleanField()
#     isitopen = models.PositiveIntegerField()
#     date_of_order = models.DateTimeField()
#     meals = models.ForeignKey()
#
#
# class Department(model.Models):
#     name_of_departments = models.CharField(max_length=155)
#
#
#     def __str__(self):
#         return self.name_of_departments
#
#
# class Role(models.Model):
#     name_of_tables = models.CharField(max_length=155)
#
#
# class Meal(model.Model):
#     name_of_meals = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.TextField()
#
#
# class MealCategories(models.Model):
#     name_of_categories = models.CharField(max_length=100)
#     departments = models.()
#
#
#
#
# # Create your models here.
