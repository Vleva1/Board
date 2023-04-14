from django import forms
from django.core.exceptions import ValidationError
from board.models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'post_title',
            'post_text',
            'name_category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        post_title = cleaned_data.get('post_title')
        post_text = cleaned_data.get('post_text')
        if post_text is not None and post_text == post_title:
            raise ValidationError({
                'post_text': 'Текст статьи не должен быть идентичен заголовоку'
            })
        return cleaned_data


class RespondForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea)

    class Meta:
        fields = ['text']

















