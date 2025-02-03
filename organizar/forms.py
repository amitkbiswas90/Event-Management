from django import forms
from organizar.models import Event, Category, Participant
from django.core.validators import EmailValidator


class CustomFormMixin:
    base_style = (
        'border-2 px-3 py-2 text-gray-700 bg-white rounded-md '
        'focus:outline-none focus:ring-2 focus:ring-blue-300 focus:border-blue-500 '
        'placeholder-gray-400/70 transition-all duration-200'
    )

    def apply_custom_styles(self):
        for field_name, field in self.fields.items():
                
                if isinstance(field.widget, forms.EmailInput):
                    field.widget.attrs.update({
                    'class': self.base_style,
                    'placeholder': "your.email@example.com" 
                })
            
                elif isinstance(field.widget, forms.TextInput):
                    field.widget.attrs.update({
                        'class': self.base_style,
                        'placeholder': f"Enter {field.label.lower()}"
                    })

                elif isinstance(field.widget, forms.Textarea):
                    field.widget.attrs.update({
                        'class': f'{self.base_style} resize-y min-h-[100px] w-full',
                        'rows': 3,
                        'placeholder': f"Describe {field.label.lower()}"
                    })

                elif isinstance(field.widget, forms.SelectDateWidget):
                    field.widget.attrs.update({
                        'class':self.base_style
                    })

                elif isinstance(field.widget, forms.TimeInput):
                    field.widget.attrs.update({
                        'class': self.base_style,
                        'type': 'time'
                    })

                elif isinstance(field.widget, forms.Select):
                    field.widget.attrs.update({
                        'class': f'{self.base_style} pr-8 bg-white appearance-none'
                    })

                elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                    field.widget.attrs.update({
                        'class': 'flex flex-wrap gap-4 [&>li]:!list-none [&_input]:mr-2'
                    })

                else:
                    field.widget.attrs.update({'class': self.base_style})

            



class CategoryForm(CustomFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Category Name',
            'description': 'Description'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_custom_styles()  


class ParticipantForm(CustomFormMixin, forms.ModelForm):
    events = forms.ModelMultipleChoiceField(
        queryset=Event.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Events"
    )

    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_custom_styles()  


class EventForm(CustomFormMixin, forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a Category",
        required=True,
        widget=forms.Select(attrs={
            'class': '!pr-8 appearance-none bg-select-chevron bg-no-repeat bg-right-2'
        })
    )

    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'date': forms.SelectDateWidget(years=range(2025, 2050)),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'name': 'Event Name',
            'description': 'Event Description',
            'date': 'Event Date',
            'time': 'Start Time',
            'location': 'Venue Location'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_custom_styles()  
