from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models


class Pizza(models.Model):
    meatToppings = models.ManyToManyField('MeatTopping', default='MeatTopping')
    veggieToppings = models.ManyToManyField('VeggieTopping', default='VeggieTopping')
    size = models.ManyToManyField('PizzaSize', default='PizzaSize')
    sauceToppings = models.ManyToManyField('SauceTopping', default='SauceToppings')
    crustType = models.ManyToManyField('CrustType', default='CrustType')
    extra = models.ManyToManyField('Extra', default='Extra')


class PizzaSize(models.Model):
    size = models.CharField('size', max_length=50, default='size')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return "{} (${})".format(self.size, self.price)


class MeatTopping(models.Model):
    blank = True
    null = True
    name = models.CharField('meatToppings', max_length=50, default='meatTopping')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return "{} (${})".format(self.name, self.price)


class VeggieTopping(models.Model):
    blank = True
    null = True
    name = models.CharField('veggieToppings', max_length=50, default='veggieTopping')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return "{} (${})".format(self.name, self.price)


class SauceTopping(models.Model):
    name = models.CharField('Name', default='Name', max_length=50)

    def __str__(self):
        return self.name


class CrustType(models.Model):
    name = models.CharField('name', default='name', max_length=50)

    def __str__(self):
        return self.name


class SpecialtyPizza(models.Model):
    name = models.CharField('name', default='name', max_length=50)
    meatToppings = models.ManyToManyField('MeatTopping', default='MeatTopping', blank=True)
    veggieToppings = models.ManyToManyField('VeggieTopping', default='VeggieTopping', blank=True)
    sauceToppings = models.ManyToManyField('SauceTopping', default='SauceToppings')
    PriceSmall = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    PriceMedium = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    PriceLarge = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    PriceXLarge = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return "{}".format(self.name)


class Extra(models.Model):
    name = models.CharField('extra', max_length=50, default='extra')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return "{}".format(self.name)


class Status(models.Model):
    status = models.CharField('status', max_length=100, default='status:')

    def __str__(self):
        return "{}".format(self.status)


class OrderedPizza(models.Model):
    user = models.ForeignKey(User, null=True)
    status = models.ManyToManyField('Status', default='Status', blank=True)
    meatToppings = models.ManyToManyField('MeatTopping', default='MeatTopping', blank=True)
    veggieToppings = models.ManyToManyField('VeggieTopping', default='VeggieTopping', blank=True)
    size = models.ManyToManyField('PizzaSize', default='PizzaSize')
    sauceToppings = models.ManyToManyField('SauceTopping', default='SauceToppings')
    crustType = models.ManyToManyField('CrustType', default='CrustType')
    extra = models.ManyToManyField('Extra', default='Extra', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    name = models.CharField('extra', max_length=50, default='extra')

    def __str__(self):
        return "{}".format(self.user)


class DietaryRestrictionsList(models.Model):
    name = models.CharField('name', default='name', max_length=50)
    meatToppings = models.ManyToManyField('MeatTopping', default='MeatTopping', blank=True)
    veggieToppings = models.ManyToManyField('VeggieTopping', default='VeggieTopping', blank=True)
    sauceToppings = models.ManyToManyField('SauceTopping', default='SauceToppings', blank=True)
    crustType = models.ManyToManyField('CrustType', default='CrustType', blank=True)
    extra = models.ManyToManyField('Extra', default='Extra', blank=True)


    def __str__(self):
        return "{}".format(self.name)


class DietaryRestrictions(models.Model):
    user = models.ForeignKey(User, null=True)
    dietaryRestrictionsList = models.ManyToManyField('DietaryRestrictionsList', default='DietaryRestrictionsList', blank=True)

    def __str__(self):
        return "{}".format(self.user)
