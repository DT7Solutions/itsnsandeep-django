from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Banner(models.Model):
        Id = models.IntegerField(primary_key = True)
        Title = models.CharField(max_length=25,default="heading")
        Description = models.CharField(max_length=100)
        Image = models.ImageField(upload_to='uploads/')
        def __str__(self):
            return self.Title
        

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name
    
   
class Tags(models.Model):
    tag_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.tag_name   

class Blogs(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.CharField(max_length=300,default="",null=True)
    First_title = models.CharField(max_length=500,default="",null=True)
    Second_title = models.CharField(max_length=500,default="",null=True)
    Image1 = models.ImageField(upload_to='uploads/')
    Body = RichTextField()
    Name = models.CharField(max_length=50)
    Create_at = models.DateTimeField(default=datetime.now())
    Sluglink =models.SlugField(max_length=200, unique=True,blank=True,null=True)


    def __str__(self):
        return self.First_title
     
    
class Contact(models.Model):
        Id = models.IntegerField(primary_key = True)
        Name = models.CharField(max_length=30,default="heading")
        Email=models.EmailField()
        Message = models.CharField(max_length=200)

        def __str__(self):
            return self.Name
