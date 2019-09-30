from django.db import models

# Create your models here.

class Product(models.Model):
    pro_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=11)
    price = models.FloatField()
    describe = models.CharField(max_length=11)
    created = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        db_table= 'product'
        # 按照创建时间升序排列
        ordering = ('created',)

