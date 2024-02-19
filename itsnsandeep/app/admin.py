from django.contrib import admin
from .models import Category,Tags,Blogs,Contact,Banner,Portfolio,About
# Register your models here.


class AdminBanner(admin.ModelAdmin):
    list_display=['Id','Title','Description' ,'Image']

class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name']


class AdminTags(admin.ModelAdmin):
    list_display = ['tag_name']


class AdminBlogs(admin.ModelAdmin):
    list_display = ['category','First_title','Second_title','Image1','Body','Name','Create_at','Sluglink']

class AdminContact(admin.ModelAdmin):
    list_display=('Id','Name','Email' ,'Message')


class AdminPortfolio(admin.ModelAdmin):
    list_display = ['Port_Title','Port_Description','Portfolio_Image']


class AdminAbout(admin.ModelAdmin):
    list_display = ['About_Title','About_Long_Desc','About_Image']




admin.site.register(Banner,AdminBanner)
admin.site.register(Category,AdminCategory)
# admin.site.register(Tags,AdminTags)
admin.site.register(Blogs,AdminBlogs)
admin.site.register(Contact,AdminContact)
admin.site.register(Portfolio,AdminPortfolio)
admin.site.register(About,AdminAbout)

