from django import forms

from .models import Post

class KakikomiForm(forms.Form):
     name = forms.CharField(
          label='お名前', max_length=50,
          required=False
     )
     email = forms.EmailField(
          label='メールアドレス', required=False
     )
     text = forms.CharField(label='アレルギー', widget=forms.Textarea, help_text='※任意'
     )

class PostForm(forms.ModelForm):
     class Meta:
          model = Post
          fields = ('title', 'text',)
