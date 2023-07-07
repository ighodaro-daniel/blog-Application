from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question= models.CharField(max_length=50)
    pub_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.question
    
    

class Choice(models.Model) :
    question_choice = models.ForeignKey(Question,on_delete= models.CASCADE)  
    text = models.TextField(max_length=600) 
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.text