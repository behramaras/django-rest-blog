from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from favourite.models import Favourite


class FavouriteListCreateAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"

    def validate(self, attrs):
        query_set = Favourite.objects.filter(post=attrs["post"],user=attrs["user"])
        if query_set.exists():
            raise serializers.ValidationError("Halihazırda favorilerde.")
        return attrs

class FavouriteAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('content',)
