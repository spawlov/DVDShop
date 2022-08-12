from django.contrib import admin

from .models import Section, Product, Order, Discount, OrderLine


class PriceFilter(admin.SimpleListFilter):
    title = 'Цена'
    parameter_name = 'price'
    step_price = 100

    def lookups(self, request, model_admin):
        max_price = Product.objects.order_by('price').last()
        filters = []
        if max_price:
            max_price = (max_price.price // self.step_price) \
                        * self.step_price + self.step_price
            price = self.step_price
            while price <= max_price:
                filters.append(
                    (price, f'{price - self.step_price + 1} - {price}')
                )
                price += self.step_price
        return filters

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        price = int(self.value())
        return queryset.filter(
            price__gte=(price - self.step_price + 1), price__lte=price
        )


class AdminProduct(admin.ModelAdmin):
    search_fields = ['title']
    list_display = [
        'title',
        'section',
        'price',
        'date',
    ]
    list_filter = [
        'section',
        PriceFilter,
    ]
    list_per_page = 10
    actions_on_bottom = True


admin.site.register(Section)
admin.site.register(Product, AdminProduct)
admin.site.register(Discount)
admin.site.register(Order)
admin.site.register(OrderLine)
