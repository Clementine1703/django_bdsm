from django import forms


class CallForm(forms.Form):
    name = forms.CharField(label='Введите имя', max_length=50, required=True,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control mb-3', 'id': 'inputAddress', 'name': 'name', }),
                           disabled=False,
                           error_messages={'required': "Пожалуйста, введите ваше имя"})
    number = forms.CharField(label='Введите номер', max_length=12, required=True,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control mb-4', 'id': 'inputAddress2', 'name': 'number', }),
                             disabled=False,
                             error_messages={'required': "Пожалуйста, введите ваш номер"})
    checkbox = forms.BooleanField(label='',
                                  help_text='мы не сохраняем ваши личные данные',
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'gridCheck'}),)
    is_bot = forms.CharField(max_length=50, required=False,
                             widget=forms.TextInput(
                                 attrs={'style': 'display:none;', }),
                             disabled=False,)
