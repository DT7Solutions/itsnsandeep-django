from django.urls import path
from .views import index,blogs,blog_details,ceo_and_business_personal_branding,celebprenenur_transformation,educational_institutions,corporate_solutions_personal_branding


urlpatterns = [
    path('',index,name='index'),
    path('blogs/',blogs,name='blogs'),
    path('blog-details/<str:slug>',blog_details, name='blog_details'),
    path('ceo-and-business-personal-branding/',ceo_and_business_personal_branding, name="ceo_and_business_personal_branding"),
    path('celebprenenur-transformation/',celebprenenur_transformation,name="celebprenenur_transformation"),
    path('educational-institutions/',educational_institutions,name="educational_institutions"),
    path('corporate-solutions-personal-branding/',corporate_solutions_personal_branding,name="corporate_solutions_personal_branding"),
]