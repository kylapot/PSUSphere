from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, Student, College, OrgMember
from studentorg.forms import OrganizationForm, StudentForm, CollegeForm, OrgMemberForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

#-- ORGANIZATION --
@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = "organization"
    template_name = 'organization_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(name__icontains=query) |
                            Q(description__icontains=query))
        return qs
    
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')


#-- STUDENT --
@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Student
    context_object_name = 'home'
    template_name = 'home.html'

template_name = "home.html"

class StudentList(ListView):
    model = Student
    context_object_name = "student"
    template_name = 'student_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(name__icontains=query) |
                            Q(description__icontains=query))
        return qs
    
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')


#-- College-------------------------------------- --
@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = College
    context_object_name = 'home'
    template_name = 'home.html'

template_name = "home.html"

class CollegeList(ListView):
    model = College
    context_object_name = "college"
    template_name = 'college_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(CollegeList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(name__icontains=query) |
                            Q(description__icontains=query))
        return qs
    
class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

#-- OrgMember-------------------------------------- --  
@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = OrgMember
    context_object_name = 'home'
    template_name = 'home.html'

template_name = "home.html"

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = "orgmember"
    template_name = 'orgmember_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrgMemberList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(name__icontains=query) |
                            Q(description__icontains=query))
        return qs
    
class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('OrgMember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')