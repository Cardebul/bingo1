from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class DataModel(models.Model):
    for i in range(1, 26):
        locals()[f'field{i}'] = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name='пользователь',
                                unique=True)
    bingo = models.OneToOneField('BingoModel', on_delete=models.CASCADE,
                                 unique=True)

    def __str__(self):
        return f"DataModel ({self.pk})"


class BingoModel(models.Model):
    for i in range(1, 26):
        locals()[f'field{i}'] = models.BooleanField(default=False)
    old_progress = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                unique=True)


class DataModelThree(models.Model):
    for i in range(1, 10):
        locals()[f'field{i}'] = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name='пользователь',
                                unique=True)
    bingo = models.OneToOneField('BingoModelThree', on_delete=models.CASCADE,
                                 unique=True)

    def __str__(self):
        return f"BingoModelThree ({self.pk})"


class BingoModelThree(models.Model):
    for i in range(1, 10):
        locals()[f'field{i}'] = models.BooleanField(default=False)
    old_progress = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                unique=True)


class MainMod(models.Model):
    """False 3x3  True 5x5"""
    mod = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                unique=True, related_name='mod')