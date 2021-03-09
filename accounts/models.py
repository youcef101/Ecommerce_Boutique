from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class UserProfile(models.Model):
    SEXE=(('Homme','Homme'),('Femme','Femme'))
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    sexe=models.CharField(null=True,max_length=8,choices=SEXE)
    phone=models.CharField(null=True,max_length=8)
    adresse=models.CharField(null=True,max_length=100)
    city=models.CharField(null=True,max_length=50)
    state=models.CharField(blank=True, max_length=20)
    zipcode=models.CharField(blank=True, max_length=4)
    country=models.CharField(null=True,max_length=50)
    image=models.ImageField(blank=True,default='person.png')
    
    def __str__(self):
        return self.user.username
    def user_name(self):
        return self.user.first_name +' '+ self.user.last_name 
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'