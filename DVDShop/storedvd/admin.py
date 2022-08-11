from django.contrib import admin

from .models import Section, Product, Order, Discount, OrderLine

admin.site.register(Section)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Order)
admin.site.register(OrderLine)
