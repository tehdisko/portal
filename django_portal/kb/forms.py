from django import forms
from .models import Article
# from pagedown.widgets import PagedownWidget
# from mdeditor.fields import MDTextField
# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# from markdownx.fields import MarkdownxFormField
class ArticleCreateForm(forms.ModelForm):
#	text = forms.CharField(widget=SummernoteWidget())
    #text = forms.CharField(widget=MarkdownxFormField())
    #text = forms.CharField(widget=PagedownWidget())
    text = forms.CharField(
    required=False, 
    label='Text',
    widget=forms.Textarea(
        attrs={
            "id": "id_text",
            }
        )
    )	
    class Meta:
        model = Article
        fields = ['title', 
                'tags', 
                'category', 
                'description',
                'text', 
                ]


class RawArticleCreateForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    tags = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your tags"}))
    text = forms.CharField(
    required=True, 
    label='',
    widget=forms.Textarea(
        attrs={
            "class": "new-class name two",
            "id": "my-id-for-text-area",
            "cols": 20,
            "rows": 20,
            "placeholder":"Your text"
            }
        )
    )	


class RawLoginForm(forms.Form):
		username 	= forms.CharField(label='Username', widget=forms.TextInput(attrs={"type":"text","id": "username"}))
		password	= forms.CharField(label='Password', widget=forms.TextInput(attrs={"type":"password","id": "password"}))
		
