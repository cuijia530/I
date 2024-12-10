from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)   # 字符字段被表示为 CharField
    pub_date = models.DateTimeField('date published')  # 日期时间字段被表示为 DateTimeField 

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    