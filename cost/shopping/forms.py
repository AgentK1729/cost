from django import forms

class LoginForm (forms.Form):
	username = forms.EmailField (label = "", widget=forms.TextInput(attrs={'width':'30vw', 'height':'6vh', 'font-size':'3vh',
		'placeholder':'Username', 'class':'form-control login-field'}))
	password = forms.CharField (label = "", widget=forms.PasswordInput(attrs={'width':'30vw', 'height':'6vh', 'font-size':'3vh',
		'placeholder':'Password', 'class':'form-control login-field'}))
