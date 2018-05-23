from django import forms
from home.models import Blog, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# a model form is a form that is BOUND to a particular model, as opposed to an un-bound form to any model.
class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    blog = forms.CharField(widget=SummernoteWidget())
    public = forms.BooleanField(label='Publish?', initial=True, required=False, widget=forms.RadioSelect(choices=[(1, 'Yes'), (0, 'No')]))

    class Meta:
        model = Blog
        fields = ('title', 'blog', 'public')

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': '6', 'cols': '80', 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('comment',)

