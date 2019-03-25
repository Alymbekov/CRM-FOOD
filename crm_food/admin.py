from django.contrib import admin
from crm_food.models import (
                         Checks,
                         Table,
                         Order,
                         Department,
                         Status,
                         Role,
                         Meal,
                         MealCategory,
                         OrderItem,
                         ServicePercentage,
                      )


admin.site.register(Table)
admin.site.register(ServicePercentage)
admin.site.register(Checks)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Status)
admin.site.register(Meal)
admin.site.register(MealCategory)

# Register your models here.
