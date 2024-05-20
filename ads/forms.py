from django import forms
from django.core.exceptions import ValidationError

from .models import Post
from django.contrib.auth.models import User
from django import forms as d_forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class PostForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'author']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        title = cleaned_data.get("title")

        if title == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class BasicSignupForm(SignupForm):
    first_name = d_forms.CharField(required=True,label = "Имя")
    last_name = d_forms.CharField(required=True,label = "Фамилия")
    email = d_forms.EmailField(label = "Email")
    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )


    # def save(self, request):
    #     user = super(BasicSignupForm, self).save(request)
    #     basic_group = Group.objects.get(name='common')
    #     basic_group.user_set.add(user)
    #
    #
    #     html_content_hello = render_to_string(
    #         'hello_letter.html',
    #         {'link': settings.SITE_URL,
    #         }
    #     )
    #     msg = EmailMultiAlternatives(
    #         subject='Регистрация на портале',
    #         body='',
    #         from_email=settings.DEFAULT_FROM_EMAIL,
    #         to= [user.email]
    #     )
    #
    #     msg.attach_alternative(html_content_hello, 'text/html')
    #     msg.send()
    #     return user
# from django import forms
# from .models import Image
#
#
# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('title', 'image')