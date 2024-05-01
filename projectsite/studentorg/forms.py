from django.forms import ModelForm
from django import forms
from .models import Organization, Student, College, OrgMember

#-- ORGANIZATION --

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

#-- STUDENT --

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

#-- COLLEGE --

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = '__all__'

#-- ORGANIZATION MEMBER --
class OrgMemberForm(ModelForm):
    class Meta:
        model = OrgMember
        fields = '__all__'