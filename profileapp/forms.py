from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    model = Profile
    fields = ['image', 'nickname', 'message']