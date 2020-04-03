from django import forms
from . import models

class CreateArticles(forms.ModelForm):
  class Meta:
    model=models.Articles
    fields=['title','subject','body','slug','thumb']