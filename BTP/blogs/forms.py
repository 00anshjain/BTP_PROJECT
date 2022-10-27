from django.db.models.fields import Field
from django.forms import ModelForm
from .models import Blog, Review
from django import forms


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "featured_image",
            "description",
            "tags",
        ]

        widgets = {"tags": forms.CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        for name, fields in self.fields.items():
            fields.widget.attrs.update({"class": "input"})

        # self.fields["title"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add Title"}
        # )
        # self.fields["description"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add Description"}
        # )


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, fields in self.fields.items():
            fields.widget.attrs.update({"class": "input"})