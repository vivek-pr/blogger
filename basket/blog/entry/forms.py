import itertools
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Blog_Entry
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class AddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['headline'].label = 'Article Title'
        self.fields['body_text'].label = 'Article Content'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'headline',
                'body_text',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
    class Meta:
        model = Blog_Entry
        fields = (
            'headline',
            'body_text',
        )



    def save(self,user):
        instance = super(AddForm, self).save(commit=False)

        max_length = Blog_Entry._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.headline)[:max_length]

        for x in itertools.count(1):
            if not Blog_Entry.objects.filter(slug=instance.slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
        instance.Save(user)
        return instance
