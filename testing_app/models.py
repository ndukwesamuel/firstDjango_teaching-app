from django.db import models

# Create your models here.



class CareerModle(models.Model):
    F_name = models.CharField(max_length=100)
    L_name = models.CharField(max_length=100)
    email  = models.EmailField(max_length=25, unique=True)
    p_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.F_name} {self.L_name}'

 
class postModel(models.Model):
    author = models.ForeignKey('CareerModle',on_delete=models.CASCADE, related_name = 'CareerModle')
    body = models.TextField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.author.F_name








