from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.models import companies


class CompanyView(LoginRequiredMixin, ListView):
    model = companies
    template_name = 'aplicatie2/Companies_index.html'

    def get_context_data(self, *args, **kwargs):
        data = super(CompanyView, self).get_context_data(*args, **kwargs)
        data['companies'] = self.model.objects.filter(active=1)
        return data

class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = companies
    fields = ['name', 'company_type', 'website', 'active']
    template_name = 'aplicatie2/Companies_form.html'

    def get_success_url(self):
        return reverse('companies:listare')

class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = companies
    fields = ['name', 'company_type', 'website', 'active']
    template_name = 'aplicatie2/Companies_form.html'

    def get_success_url(self):
        return reverse('companies:listare')

def delete_company(request, pk):
    companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:listare')

def activate_company(request, pk):
    companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:listare')

class CompanyInactiveView(LoginRequiredMixin, ListView):
    model = companies
    template_name = 'aplicatie2/Companies_index.html'

    def get_context_data(self, *args, **kwargs):
        data = super(CompanyInactiveView, self).get_context_data(*args, **kwargs)
        data['companies'] = self.model.objects.filter(active=0)
        return data