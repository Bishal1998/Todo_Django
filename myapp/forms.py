from django import forms
from myapp.models import TodoTask

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = ['id', 'title', 'task']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                  'task':forms.Textarea(attrs={'class':'form-control'}),}
    
