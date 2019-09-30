from django.db import models


class Author(models.Model):
    auth_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12, unique=True)
    sex = models.IntegerField()

    class Meta:
        # 设置其在数据库名称
        db_table = "author"
        # 给模型起一个可读性更强的名称
        verbose_name = "Author"
        # 指定模型的复数形式
        verbose_name_plural = "Author"

    def __str__(self):
        """这样设置我们在打印Author对象时就会返回Author.name便于阅读"""
        return self.name

class Text(models.Model):
    text_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=12)
    content = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(to="Author",on_delete=models.CASCADE,to_field='auth_id')

    class Meta:
        db_table = 'text'

    def __str__(self):
        return self.title


