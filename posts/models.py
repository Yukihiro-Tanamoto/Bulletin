from django.db import models

# Create your models here.
from django.utils import timezone

# Create your models here.

#models.Modelを書くのはお決まり
class Posts(models.Model):

    #Metaとかobjectとかはおまじない
    class Meta(object):
        #作成されるテーブル名を指定
        db_table = 'posts'

    #カラム名=データの形式(管理画面に表示される名前,その他の制約)
    text = models.CharField(verbose_name='本文', max_length=255)
    created_at = models.DateField(verbose_name='作成日', default=timezone.now)

    #管理画面に表示されるように設定(おまじない)
    def __str__(self):
        return self.text, self.created_at
# from django.conf import settings
# from django.db import models
# from django.utils import timezone


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title