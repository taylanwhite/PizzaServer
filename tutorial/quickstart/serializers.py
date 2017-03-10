from django.contrib.auth.models import User, Group, UserManager
from django.forms import ModelForm
from rest_framework import serializers
from tutorial.quickstart.models import MeatTopping, VeggieTopping, SauceTopping, CrustType, PizzaSize, Pizza, \
    SpecialtyPizza, Extra, OrderedPizza, Status, \
 \
    DietaryRestrictions, DietaryRestrictionsList


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
    #
    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #
    #     return instance
        # class Meta:
        #     model = User
        #     fields = ('id', 'username', 'first_name', 'last_name', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'id')


class TestSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize
        fields = "__all__"


class CrustSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrustType
        fields = "__all__"


class SauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SauceTopping
        fields = "__all__"


class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeatTopping
        fields = "__all__"


class VeggieSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeggieTopping
        fields = "__all__"


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = "__all__"


class NewUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    # username = serializers.CharField()


class NewGroupSerializer(serializers.Serializer):
    name = serializers.CharField()


class PizzaSerializer(serializers.ModelSerializer):
    veggieToppings = VeggieSerializer(many=True, read_only=True)
    meatToppings = MeatSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    sauceToppings = SauceSerializer(many=True, read_only=True)
    crustType = CrustSerializer(many=True, read_only=True)
    extra = ExtraSerializer(many=True, read_only=True)

    class Meta:
        model = Pizza
        fields = "__all__"


class SpecialtyPizzaSerializer(serializers.ModelSerializer):
    veggieToppings = VeggieSerializer(many=True, read_only=True)
    meatToppings = MeatSerializer(many=True, read_only=True)
    sauceToppings = SauceSerializer(many=True, read_only=True)

    class Meta:
        model = SpecialtyPizza
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    # employee = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Status
        fields = "__all__"


class OrderedPizzaSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    status = StatusSerializer(many=True, read_only=True)
    veggieToppings = VeggieSerializer(many=True, read_only=True)
    meatToppings = MeatSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    sauceToppings = SauceSerializer(many=True, read_only=True)
    crustType = CrustSerializer(many=True, read_only=True)
    extra = ExtraSerializer(many=True, read_only=True)

    class Meta:
        model = OrderedPizza
        fields = "__all__"


class OrderedPizzaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedPizza
        fields = "__all__"


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class DietListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryRestrictionsList
        fields = "__all__"


class DietSerializer(serializers.ModelSerializer):
    dietaryRestrictionsList = DietListSerializer(many=True, read_only=True)

    class Meta:
        model = DietaryRestrictions
        fields = "__all__"


class DietPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryRestrictions
        fields = "__all__"
