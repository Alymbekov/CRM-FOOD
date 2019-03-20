from django.contrib import admin
from crm_food.models import (
                         Table,Order,
                         Department,
                         Role,Status
                      )


admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Status)

# Register your models here.
