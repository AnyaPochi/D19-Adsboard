from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy
class Post(models.Model):

    POSITIONS = [
        ('Tanks', 'Танки'),
        ('Hills', 'Хилы'),
        ('DD', 'ДД'),
        ('Sellers', 'Торговцы'),
        ('Gildmasters', 'Гилдмастеры'),
        ('Kwestgiver', 'Квестгиверы'),
        ('Blacksmith', 'Кузнецы'),
        ('Tanner', 'Кожевники'),
        ('Potion master', 'Зельевары'),
        ('Spell master', 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(User, help_text=_('автор'), on_delete=models.CASCADE)
    category = models.CharField(max_length=30, help_text=_('тип'),choices=POSITIONS, default='Tanks')
    time_in = models.DateTimeField(auto_now_add=True)

    title = models.CharField(
        max_length=255,
        help_text=('заголовок'),
        unique=True,
    )
    description = models.TextField(help_text=_('текст'))
    file = models.FileField(upload_to='files/', null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    file2 = models.FileField(upload_to='files/', null=True, blank=True)
    image2 = models.ImageField(upload_to='image/', null=True, blank=True)


    def __str__(self):
        return f'{self.title()}: {self.description[:10]}'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])
class Respond(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)



class Postrespond(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    respond_id = models.ForeignKey(Respond, on_delete=models.CASCADE)




