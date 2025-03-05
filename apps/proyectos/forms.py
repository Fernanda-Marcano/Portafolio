from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    """Form definition for Project."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    

    class Meta:
        """Meta definition for Projectform."""

        model = Project
        exclude = ('id', 'created', 'slug')
        labels = {
            'name':'Nombre', 
            'description':'Descripción', 
            'tecnology':'Tecnología', 
            'url':'URL', 
            'image':'Imagen',
        }
