from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
User = get_user_model()






class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug =  models.SlugField(max_length=225, unique_for_date='publish', blank=True, null=True)
    image = models.FileField(upload_to="static/images",  default='static/images/default.jpg', max_length=250, blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    content = RichTextField()
    like = models.ManyToManyField(User, related_name="likes", blank=True)
    status = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
    

    def is_like(self, request):
        self.request = request.user
        if request not in self.like.all():
            return True
        return False
    
    def post_count(self):
        post_number = self.user.post_set.all().count()
        return post_number

    


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.content[1:10]

    class Meta:
        ordering = ["-id"]
    
    def children(self):
        return Comment.objects.filter(parent=self)
    
    def comments(self):
        return Comment.objects.filter(post=self.id)
    
    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
    
  
def pre_save_slug(instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_slug, sender=Post)

class Notifacation(models.Model):
    notification_type = models.IntegerField()
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_to', null=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_from', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="notification_post", blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="notification_comment", blank=True, null=True)
    user_has_seen   = models.BooleanField(default=False)

    class Meta:
        ordering=("-id", )


# def notifaction_save(sender, instance, created, *args, **kwargs):
#     if created:
#         Notifacation.objects.create(notification_type=1, to_user=instance.user, from_user=instance.user, post=instance)
# post_save.connect(notifaction_save, sender=Post)




    
    
