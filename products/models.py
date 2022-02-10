from unicodedata import category
from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', null=True ,on_delete=models.CASCADE) #null=True means 비어있으면 안됨
    class Meta:
        db_table = 'categories'

class images(models.Model):
    image_url = models.CharField(max_length=300)
    drink = models.ForeignKey('Drinks', null=True ,on_delete=models.CASCADE)
    class Meta:
        db_table = 'images'

class Drinks(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(max_length=100)
    category = models.ForeignKey('Category', null = True ,on_delete=models.CASCADE)
    class Meta:
        db_table = 'drinks'

class Allergy_drink(models.Model):
    allergy_id = models.IntegerField()
    drink = models.ForeignKey('Drinks',on_delete=models.CASCADE)
    class Meta:
        db_table = 'allergy_drinks'
    #얘는 drinks와 allergy 의 중간테이블 

class allergy(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table = 'allergies'
    #다대다 관계일때 FK 비어있어도 돼서 null=True 안해줘도 됨

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=5)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=5)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=5)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=5)
    protein_g = models.DecimalField(max_digits=10, decimal_places=5)
    drink = models.ForeignKey('Drinks',on_delete=models.CASCADE)
    size = models.ForeignKey('Sizes', on_delete=models.CASCADE)
    class Meta:
        db_table = 'nutritions'

class Sizes(models.Model):
    name = models.CharField(max_length=45)
    size_mi = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)
    class Meta:
        db_table = 'sizes'

# # categories(다) - (일)menu :  one-to-many : Menu 메뉴에 음료/푸드/상품 등 카테고리
# # drinks(다) - (일)categories : one-to-many
# # images (다) - drinks(일) : one-to-many
# drinks(다) - (다) allergy : many-to-many / allergy_drink 중간테이블
# drinks(다) - (다)sizes  : many-to-many / nutritions 중간테이블 
# NULL은 포인터가 가져올 값이 없는 상태