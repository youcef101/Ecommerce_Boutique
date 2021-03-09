from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user_name','sexe','phone','adresse','city','country','image_tag']
    

admin.site.register(UserProfile,UserProfileAdmin)