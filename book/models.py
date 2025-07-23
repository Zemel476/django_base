from django.db import models

# Create your models here.
# id 模型会自动帮我们生成
class BookInfo(models.Model):
    name = models.CharField(max_length=100)


class PeopleInfo(models.Model):
    name = models.CharField(max_length=100)
    gender = models.IntegerField(max_length=1)
    # 设置外键，反向查询
    book = models.ForeignKey(BookInfo, related_name="book_info", on_delete=models.CASCADE)