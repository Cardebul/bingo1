from rest_framework import serializers

from bingo.models import BingoModel


class BingoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BingoModel
        fields = ('progress',)
