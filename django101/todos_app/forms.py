from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if 'class' in field.widget.attrs:
                value = field.widget.attrs['class'] + ' form-control'
            else:
                value = 'form-control'
            field.widget.attrs['class'] = value
