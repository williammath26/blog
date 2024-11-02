from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:#adicionar isso
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
