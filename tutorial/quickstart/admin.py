from django.contrib import admin
from tutorial.quickstart.models import MeatTopping, VeggieTopping, SauceTopping, CrustType, Pizza, PizzaSize, \
SpecialtyPizza, Extra, OrderedPizza, Status, DietaryRestrictions, DietaryRestrictionsList

# class MyAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False

admin.site.register(MeatTopping)
admin.site.register(VeggieTopping)
admin.site.register(SauceTopping)
admin.site.register(CrustType)
admin.site.register(Pizza)
admin.site.register(PizzaSize)
admin.site.register(SpecialtyPizza)
admin.site.register(Extra)
admin.site.register(OrderedPizza)
admin.site.register(Status)
admin.site.register(DietaryRestrictions)
admin.site.register(DietaryRestrictionsList)


# class MyAdmin(admin.ModelAdmin):
#     def has_add_permissions(self, request):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         elif request.method == "POST":
#             if request.user.is_superuser:
#                 return True
#             else:
#                 return False