from django.db import models

# Create your models here.
class testmodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    group_id = models.IntegerField(verbose_name='그룹 id', null=False, default=0)
    title = models.CharField(max_length=128, null=False, default='')
    content = models.TextField(null=False, default='')

    class Meta:
        db_table = 'test_table'
        verbose_name = '테스트'