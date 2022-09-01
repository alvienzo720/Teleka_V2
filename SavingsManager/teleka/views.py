from django.shortcuts import render, redirect 

from .models import *

from django.views import View

from django.contrib.auth.views import LoginView

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy, reverse

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin # used for add / edit

from django.contrib import messages # used for delete


class CustomLoginView(LoginView):
    template_name = 'teleka/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(Self):
        return reverse_lazy('dashboard')


class RegisterPage(FormView):
    template_name = 'teleka/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(RegisterPage, self).get(*args, **kwargs)


class DashboardView(LoginRequiredMixin,ListView):
    model = Member
    model = User
    context_object_name = 'dashboard'
    template_name = 'teleka/dashboard.html'
    
    
    def get_success_url(Self):
        return reverse_lazy('dashboard')


class CreateMember(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Member
    fields = '__all__'
    template_name = 'teleka/createMember.html'
    success_url = reverse_lazy('view-members')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateMember, self).form_valid(form)
    
    success_message = "Member Created Successfully !"

class ViewMembers(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model= User
    model = Member
    context_object_name = 'members'
    template_name = 'teleka/viewMembers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = context['members'].filter(user=self.request.user)

        
        return context


class MemberUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model= User
    model = Member
    fields = [
       "firstname", "lastname", "id_type", "id_number", "gender", "date_of_birth",
       "district", "county", "subcounty", "parish", "village", "account_number",
       "opening_balance", "email", "phone", "next_of_keen_first_name", 
       "next_of_keen_last_name", "next_of_keen_phone", "next_of_keen_relationship",
       "status"
    ]
    template_name = 'teleka/createMember.html'
    success_url = reverse_lazy('view-members')
    success_message = "Member Updated successfully !"


class MemberDelete(LoginRequiredMixin, DeleteView):
    model = Member
    context_object_name = 'members'
    success_url = reverse_lazy('view-members')
    template_name = 'teleka/memberConfrim.html'

    def get_success_url(self):
        messages.success(self.request, "Member Deleted Succesfully !")
        return reverse('view-members')

class MemberDetails(LoginRequiredMixin, DetailView):
    model = Member
    context_object_name = 'member'
    template_name = 'teleka/memberDetails.html'





