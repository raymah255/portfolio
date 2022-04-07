from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    profile_img = models.FileField(upload_to="static/profiles/", default="static/profiles/profile.jpg", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    followers = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        return self.user.username

    
    def is_profile_pic(self):
        if self.profile_img == "":
            return False
        return True
    
    def post_count(self):
        post_number = self.user.post_set.all().count()
        return post_number


def post_profile_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(post_profile_save, sender=User)




