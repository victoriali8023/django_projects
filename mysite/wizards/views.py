

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from wizards.models import Wizard, House
from wizards.forms import HouseForm

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = House.objects.all().count();
        al = Wizard.objects.all();

        ctx = { 'make_count': mc, 'wizard_list': al };
        return render(request, 'wizards/wizard_list.html', ctx)

class HouseView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = House.objects.all();
        ctx = { 'house_list': ml };
        return render(request, 'wizards/house_list.html', ctx)

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class HouseCreate(LoginRequiredMixin, View):
    template = 'wizards/house_form.html'
    success_url = reverse_lazy('wizards:all')
    def get(self, request) :
        form = HouseForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = HouseForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        house = form.save()
        return redirect(self.success_url)

# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class HouseUpdate(LoginRequiredMixin, View):
    model = House
    success_url = reverse_lazy('wizards:all')
    template = 'wizards/house_form.html'
    def get(self, request, pk) :
        house = get_object_or_404(self.model, pk=pk)
        form = HouseForm(instance=house)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        house = get_object_or_404(self.model, pk=pk)
        form = HouseForm(request.POST, instance = house)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class HouseDelete(LoginRequiredMixin, View):
    model = House
    success_url = reverse_lazy('wizards:all')
    template = 'wizards/house_confirm_delete.html'

    def get(self, request, pk) :
        house = get_object_or_404(self.model, pk=pk)
        form = HouseForm(instance=house)
        ctx = { 'house': house }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        house = get_object_or_404(self.model, pk=pk)
        house.delete()
        return redirect(self.success_url)
# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class WizardCreate(LoginRequiredMixin,CreateView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

class WizardUpdate(LoginRequiredMixin, UpdateView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')

class WizardDelete(LoginRequiredMixin, DeleteView):
    model = Wizard
    fields = '__all__'
    success_url = reverse_lazy('wizards:all')


