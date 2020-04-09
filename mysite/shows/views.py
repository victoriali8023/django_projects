

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from shows.models import Show, Type
from shows.forms import TypeForm

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Type.objects.all().count();
        al = Show.objects.all();

        ctx = { 'make_count': mc, 'show_list': al };
        return render(request, 'shows/show_list.html', ctx)

class TypeView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Type.objects.all();
        ctx = { 'type_list': ml };
        return render(request, 'shows/type_list.html', ctx)

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class TypeCreate(LoginRequiredMixin, View):
    template = 'shows/type_form.html'
    success_url = reverse_lazy('shows:all')
    def get(self, request) :
        form = TypeForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = TypeForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        breed = form.save()
        return redirect(self.success_url)

# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class TypeUpdate(LoginRequiredMixin, View):
    model = Type
    success_url = reverse_lazy('shows:all')
    template = 'shows/type_form.html'
    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = TypeForm(instance=breed)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = TypeForm(request.POST, instance = breed)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class TypeDelete(LoginRequiredMixin, View):
    model = Type
    success_url = reverse_lazy('shows:all')
    template = 'shows/type_confirm_delete.html'

    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = TypeForm(instance=breed)
        ctx = { 'breed': breed }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)
# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class ShowCreate(LoginRequiredMixin,CreateView):
    model = Show
    fields = '__all__'
    success_url = reverse_lazy('shows:all')

class ShowUpdate(LoginRequiredMixin, UpdateView):
    model = Show
    fields = '__all__'
    success_url = reverse_lazy('shows:all')

class ShowDelete(LoginRequiredMixin, DeleteView):
    model = Show
    fields = '__all__'
    success_url = reverse_lazy('shows:all')


