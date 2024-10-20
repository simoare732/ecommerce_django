from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import login
from .forms import *
from listings.models import Category


def home_signup(request):
    return render(request, 'users/home_signup.html')


class User_Signup_View(CreateView):
    model = User
    form_class = User_Signup_Form
    template_name = 'users/user_signup.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['user_type'] = 'utente'
        return ctx

    def form_valid(self , form):
        user = form.save()
        login(self.request, user)
        # The reverse is useful to generate the URL of login page
        return redirect(reverse('users:login'))


class Seller_Signup_View(CreateView):
    model = User
    form_class = Seller_Signup_Form
    template_name = 'users/user_signup.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['user_type'] = 'venditore'
        return ctx

    def form_valid(self , form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('users:login'))


# to show information of a user/seller
class detail_profile_user(DetailView):
    model = Registered_User
    template_name = 'users/profile_user.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        return ctx

class detail_profile_seller(DetailView):
    model = Seller
    template_name = 'users/profile_seller.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        return ctx

class detail_profile_admin(DetailView):
    model = User
    template_name = 'users/profile_admin.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        return ctx


class update_profile_user(UpdateView):
    model = Registered_User
    form_class = user_update_form
    template_name = 'users/update_profile_user.html'

    def get_success_url(self):
        pk = self.get_context_data()['object'].pk
        return reverse('users:profile_user', kwargs={'pk': pk})

class update_profile_seller(UpdateView):
    model = Seller
    form_class = seller_update_form
    #fields = '__all__'
    template_name = 'users/update_profile_seller.html'


    def get_success_url(self):
        pk = self.get_context_data()['object'].pk
        return reverse('users:profile_seller', kwargs={'pk': pk})

class update_profile_admin(UpdateView):
    model = User
    form_class = admin_update_form
    template_name = 'users/update_profile_admin.html'

    def get_success_url(self):
        pk = self.get_context_data()['object'].pk
        return reverse('users:profile_admin', kwargs={'pk': pk})