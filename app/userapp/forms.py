from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


User = get_user_model()


class MyUserLoginForm(AuthenticationForm):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'name': 'username',
            'id': 'floatingInput',
            'type': 'text',
            'class': 'form-control rounded-4',
        }),
        self.fields["password"].widget.attrs.update({
            'name': 'password',
            'id': 'floatingPassword',
            'type': 'password',
            'class': 'form-control rounded-4',
        })

    class Meta:
        model = User
        fields = ('username', 'password')


class MyUserRegisterForm(UserCreationForm):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'name': 'username',
            'id': 'floatingInput',
            'type': 'text',
            'class': 'form-control rounded-4',
        }),
        self.fields["email"].widget.attrs.update({
            'name': 'email',
            'id': 'floatingInput',
            'type': 'email',
            'class': 'form-control rounded-4',
        }),
        self.fields["password1"].widget.attrs.update({
            'name': 'password1',
            'id': 'floatingPassword',
            'type': 'password',
            'class': 'form-control rounded-4',
        }),
        self.fields["password2"].widget.attrs.update({
            'name': 'password2',
            'id': 'floatingPassword',
            'type': 'password',
            'class': 'form-control rounded-4',
        })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
