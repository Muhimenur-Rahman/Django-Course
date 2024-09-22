from django import forms
from django.core import validators


class contact_forms(forms.Form):
    name = forms.CharField(label="Full Name", help_text="Total length must be within 70 characters",
                           required=False, widget=forms.Textarea(attrs={'placeholder' : "Enter Your Name",}))
    file = forms.FileField()
    email = forms.EmailField(label="email")
    age = forms.IntegerField()
    Age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    choice = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=choice,widget=forms.RadioSelect)
    meal = [('C','Chicken'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)
    check = forms.BooleanField()


class student_forms(forms.Form):
    name = forms.CharField(label="User Name", help_text="Must contain atleast 10 characters",
                           widget=forms.TextInput(attrs={'placeholder' : "Enter Your Name"}))
    email = forms.EmailField(label="Email",
                           widget=forms.EmailInput(attrs={'placeholder' : "Enter Your Email"}))
    def clean_name(self):
        val_name = self.cleaned_data['name']
        if len(val_name)<10 : 
            raise forms.ValidationError("Enter a name with atleast 10 characters")
        return val_name
    def clean_email(self):
        val_email = self.cleaned_data['email']
        if '.com' not in val_email: 
            raise forms.ValidationError("Email must have .com in it")
        return val_email

    # def clean(self):
    #     cleaned_data = super().clean()
    #     val_name = self.cleaned_data['name']
    #     val_email = self.cleaned_data['email']
    #     if len(val_name)<10 : 
    #         raise forms.ValidationError("Enter a name with atleast 10 characters")
    #     if '.com' not in val_email: 
    #         raise forms.ValidationError("Email must have .com in it")

def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("enter text atleast 10 chars")
class another_forms(forms.Form):
    name = forms.CharField(label="Username",
                           validators=[validators.MinLengthValidator(10,message="At Least 10 chars")])
    email = forms.CharField(label="Email", 
                            validators=[validators.EmailValidator(message="Enter a valid email")])
    text = forms.CharField(widget=forms.TextInput,validators=[len_check])
    age = forms.IntegerField(validators=[validators.MinValueValidator(10,message="age must be atleast 10"),
                                         validators.MaxValueValidator(50,message="age must be maximum 50")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['.pdf','png'],
                                                                         message='File extension should be .pdf or .png')])
    

class password_forms(forms.Form):
    name = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        con_pass= self.cleaned_data['confirm_password']
        if val_pass != con_pass : 
            raise forms.ValidationError("Password did not match")
        

