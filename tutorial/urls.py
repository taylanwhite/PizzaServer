from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views
from django.contrib import admin
from tutorial.quickstart.views import hello, current_datetime, hours_ahead
from rest_framework.authtoken import views as view
from tutorial.quickstart.views import UserViewSet, GroupViewSet


# Extra, CustomerInfo, CompleteOrder, OrderedExtras, OrderedPizza
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'meatToppings', views.MeatViewSet, 'meatToppings')
router.register(r'veggieToppings', views.VeggieViewSet, 'veggieToppings')
router.register(r'crust', views.CrustViewSet, 'crust')
router.register(r'sauce', views.SauceViewSet, 'sauce')
router.register(r'pizzaSize', views.SizeViewSet, 'pizzaSize')
# router.register(r'pizza', views.PizzaViewSet, 'pizza')
router.register(r'specialtyPizza', views.SpecialtyPizzaViewSet, 'specialtyPizza')
router.register(r'extra', views.ExtraViewSet, 'extra')
router.register(r'orderedPizzas', views.OrderedPizzaViewSet, 'orderedPizzas')
router.register(r'status', views.StatusViewSet, 'status')
router.register(r'newUser', views.AddUserViewSet, 'newUser')
router.register(r'userDietaryRestriction', views.DietaryViewSet, 'userDietaryRestriction')
router.register(r'dietList', views.DietaryListViewSet, 'dietList')

settings_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
})

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', view.obtain_auth_token),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),

    # ...
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # ...

]


