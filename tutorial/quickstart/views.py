from django.contrib.auth import login
from django.contrib.auth.models import User, Group, UserManager
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.defaultfilters import pprint
from django.template.defaulttags import comment
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, api_view, list_route
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from tutorial.quickstart.serializers import NewUserSerializer, NewGroupSerializer, \
    MeatSerializer, VeggieSerializer, CrustSerializer, SauceSerializer, SizeSerializer, \
    PizzaSerializer, SpecialtyPizzaSerializer, ExtraSerializer, \
    OrderedPizzaSerializer, StatusSerializer, OrderedPizzaPostSerializer, CreateUserSerializer, DietSerializer, \
    DietListSerializer, DietPostSerializer

from .serializers import UserSerializer, GroupSerializer
from .permissions import delete_permissions, post_permissions, no_permissions, patch_permissions
from django.http import HttpResponse
from tutorial.quickstart.models import MeatTopping, VeggieTopping, CrustType, SauceTopping, PizzaSize, Pizza, \
    SpecialtyPizza, Extra, OrderedPizza, Status, DietaryRestrictions, DietaryRestrictionsList

import datetime


def hello(request):
    return HttpResponse("noing")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be  %s.  " % (offset, dt)
    return HttpResponse(html)


class OrderedPizzaViewSet(viewsets.ModelViewSet):
    queryset = OrderedPizza.objects.all()
    serializer_class = OrderedPizzaSerializer
    permission_classes = ()
    http_method_names = ['get', 'head', 'post', 'delete']

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderedPizzaPostSerializer
        return OrderedPizzaSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user.id
        return OrderedPizza.objects.filter(user=user)


class SpecialtyPizzaViewSet(viewsets.ModelViewSet):
    queryset = SpecialtyPizza.objects.all()
    serializer_class = SpecialtyPizzaSerializer
    permission_classes = (delete_permissions, no_permissions)
    http_method_names = ['get', 'head']


class SizeViewSet(viewsets.ModelViewSet):
    queryset = PizzaSize.objects.all()
    serializer_class = SizeSerializer
    permission_classes = (delete_permissions, no_permissions, post_permissions)
    http_method_names = ['get', 'head']


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (delete_permissions, no_permissions)
    http_method_names = ['get', 'head']


class SauceViewSet(viewsets.ModelViewSet):
    queryset = SauceTopping.objects.all()
    serializer_class = SauceSerializer
    permission_classes = (delete_permissions, no_permissions)
    http_method_names = ['get', 'head']

    # def get_serializer_class(self):
    #     if self.request.user.is_superuser:
    #         return SauceSerializer
    #     return SauceSerializer


class CrustViewSet(viewsets.ModelViewSet):
    queryset = CrustType.objects.all()
    serializer_class = CrustSerializer
    permission_classes = (delete_permissions, no_permissions)
    http_method_names = ['get', 'head']


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (delete_permissions, no_permissions)
    http_method_names = ['get', 'head']


class VeggieViewSet(viewsets.ModelViewSet):
    queryset = VeggieTopping.objects.all()
    serializer_class = VeggieSerializer
    permission_classes = (delete_permissions, no_permissions)
    http_method_names = ['get', 'head']


class MeatViewSet(viewsets.ModelViewSet):
    queryset = MeatTopping.objects.all()
    serializer_class = MeatSerializer
    permission_classes = (delete_permissions, no_permissions)
    http_method_names = ['get', 'head']


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
    permission_classes = (delete_permissions, no_permissions)
    http_method_names = ['get', 'head']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    serializer = UserSerializer(comment, partial=True)
    permission_classes = [IsAuthenticated, ]
    # permission_classes = (delete_permissions, post_permissions, patch_permissions)
    http_method_names = ['get', 'patch']

    @list_route(['GET', 'HEAD'], permission_classes=[patch_permissions])
    def current_user(self, request):

        return Response(UserSerializer(request.user).data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (delete_permissions, post_permissions)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return GroupSerializer
        return NewGroupSerializer


class AddUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (delete_permissions, post_permissions)


class DietaryListViewSet(viewsets.ModelViewSet):
    queryset = DietaryRestrictionsList.objects.all()
    serializer_class = DietListSerializer
    permission_classes = (delete_permissions, post_permissions)


class DietaryViewSet(viewsets.ModelViewSet):
    queryset = DietaryRestrictions.objects.all()
    serializer_class = DietSerializer
    permission_classes = ()
    http_method_names = ['get', 'head', 'post', 'delete']

    def get_serializer_class(self):
        if self.action == 'create':
            return DietPostSerializer
        return DietSerializer

    def get_queryset(self):
        """
        This view should return a list of all the objects
        for the currently authenticated user.
        """
        user = self.request.user.id
        return DietaryRestrictions.objects.filter(user=user)
