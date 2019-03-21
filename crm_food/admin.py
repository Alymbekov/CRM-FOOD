from django.contrib import admin
from crm_food.models import (
                         Table,
                         Order,
                         Department,
                         Status,
                         Role,
                         Meal,
                         MealCategory,
                      )


admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Status)
admin.site.register(Meal)
admin.site.register(MealCategory)

# Register your models here.
