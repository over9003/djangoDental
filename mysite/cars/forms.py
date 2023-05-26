from django import forms
from cars.models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label="Email" )
#     review = forms.CharField(label="Plase write your review here",
#                              widget=forms.Textarea(attrs={'class': 'myform', 'rows':'2', 'cols':'2'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = ['first_name', 'last_name', 'stars']
        fields = "__all__"
        
        labels = {
            'first_name': "YOUR FIRST NAME",
            'last_name': "YOUR LAST NAME",
            'stars': "Rating"
        }
        
        error_messages = {
            'stars': {
                'min_value': "YO! min value is 1",
                'max_value': "HO! max value is 5",
            }
        }