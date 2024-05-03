from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'pub_date']
