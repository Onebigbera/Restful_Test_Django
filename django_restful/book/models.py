from django.db import models

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    describe = models.CharField(max_length=11)
    created = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'book'
        # 设置按照时间的升序排列
        ordering = ['created']

