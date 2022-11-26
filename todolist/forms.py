
from  django import forms



class TodoForm(forms.Form):
    text=forms.CharField(widget=forms.TextInput(attrs={
          "class" :"form-control", "placeholder":"Enter todo e.g. Wash my car", "aria-label":"Todo",
        "aria-describedby":"add-btn"
    }))




