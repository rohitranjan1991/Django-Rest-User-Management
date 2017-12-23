from django import forms

from usermgmt.models import InstaWorkUser

USER_ROLE = (
    ('admin', 'admin'),
    ('regular', 'regular')
)


class InstaWorkUserForm(forms.ModelForm):
    role = forms.ChoiceField(choices=USER_ROLE, required=True)

    class Meta:
        model = InstaWorkUser
        fields = '__all__'


class InstaWorkUserUpdateForm(forms.Form):
    first_name = forms.CharField(label='First Name', empty_value=None, max_length=100, required=False)
    last_name = forms.CharField(label='Last Name', empty_value=None, max_length=100, required=False)
    email = forms.EmailField(label='Email', empty_value=None, max_length=100, required=False)
    phone_number = forms.CharField(label='Phone Number', empty_value=None, max_length=15, required=False)
    role = forms.ChoiceField(label='Role', choices=USER_ROLE, required=False)

    def is_valid(self):
        valid = super(InstaWorkUserUpdateForm, self).is_valid()
        if self.cleaned_data['role'] == '':
            self.cleaned_data['role'] = None
        return valid