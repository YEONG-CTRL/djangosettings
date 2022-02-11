from django.db import models

# Create your models here.
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus' #테이블 이름 만들어주는 것 

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE) #foreign키가 되는 컬럼이라도 _id해주지 않음 
    #왜냐면 장고가 알아서 붙여줌 - 두번붙여지지 않게

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name     = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) 

    class Meta:
        db_table = 'products'