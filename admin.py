from django.contrib import admin

# Register your models here.
from .models import Employee, Salary, Timesheet,Leave, Status, Profiles, Hospi,Hospit,Canteen_Product,Orders,OrderUpdate

# Register your models here.
admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Timesheet)
admin.site.register(Leave)
admin.site.register(Status)
admin.site.register(Profiles)
admin.site.register(Hospit)
admin.site.register(Canteen_Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

