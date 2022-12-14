from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Post, Category, Comment


class PostForm(ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
    )
    category.widget.attrs.update({"class": "form-control"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].label = "Категория"
        self.fields["content"].label = "Содержимое"

    class Meta:
        model = Post
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }
        fields = "__all__"
        exclude = [
            "user",
            "active",
            "is_deleted",
            "created_at",
            "updated_at",
            "objects",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }
