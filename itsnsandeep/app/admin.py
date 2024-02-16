from django.contrib import admin
from .models import Category,Tags,Blogs,Contact,Banner
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


admin.site.register(Banner,AdminBanner)
admin.site.register(Category,AdminCategory)
admin.site.register(Tags,AdminTags)
admin.site.register(Blogs,AdminBlogs)
admin.site.register(Contact,AdminContact)