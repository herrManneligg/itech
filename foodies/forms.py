from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from betterforms.multiform import MultiModelForm
from foodies.models import Meal, Category, UserProfile, Ingredient, Request
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
    # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class MealForm(forms.ModelForm):
    title = forms.CharField(max_length=Meal.TITLE_MAX_LENGTH,
                            help_text="Please enter the title of the meal.")
    price = forms.FloatField(help_text="Please enter the price for this meal")
    url = forms.URLField(max_length=Meal.URL_MAX_LENGTH, help_text="Please enter the URL of the meal page.")
    category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'), help_text="Please select the category for this meal")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def label_from_instance(self, obj):
        return "%s" %(obj)

    class Meta:
        model = Meal
        #exclude = ('category',)
        fields = ('title', 'url', 'price', 'category')

class IngredientsForm(forms.ModelForm):
    name = forms.CharField(required=True, help_text="Please enter one ingredient")
    vegetable = forms.CharField(required=False, help_text="Please enter the vegetables")
    typeofmeat = forms.CharField(required=False, help_text="Please enter the type of meat")
    meal = MealForm

    class Meta:
        model = Ingredient
        fields = ('name', 'vegetable', 'typeofmeat',)

# This form takes the IngredientsForm and the MealForm at the same time for being handled in views
class mealIngredientMultiForm(MultiModelForm):
    form_classes = {
        'meal': MealForm,
        'ingredients': IngredientsForm,
    }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("This email already exists")
       return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('username', 'email','password',)

class UserProfileForm(forms.ModelForm):
    isCooker = forms.BooleanField(initial=False, required=False, label='Are you a cooker?')
    isDinner = forms.BooleanField(initial=False, required=False, label='Are you a dinner?')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True

    class Meta:
        model = UserProfile
        fields = ('name', 'isCooker', 'isDinner')

class UserUpdateForm(forms.ModelForm):
    password = None

    # def clean(self):
    #    email = self.cleaned_data.get('email')
    #    if User.objects.filter(email=email).exists():
    #         raise ValidationError("This email already exists")
    #    return self.cleaned_data
    

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True


    class Meta:
        model = User
        exclude = ['username', 'password']
        fields = ('email',)


class UserProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True

    class Meta:
        model = UserProfile
        fields = ('name', 'picture', 'address', 'phone', 'personalDescription', 'isCooker', 'isDinner')

class RequestAMealForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('title', 'date', 'name', 'email', 'content', 'message')
