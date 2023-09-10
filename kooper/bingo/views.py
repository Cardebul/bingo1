import json
from typing import Any, Dict
from django import http

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import DataForm, DataFormThree, TestForm
from .models import BingoModel, DataModel, DataModelThree, BingoModelThree, MainMod
from .utils import calc


class CreateMatrixView(LoginRequiredMixin, CreateView):
    model = DataModel
    form_class = DataForm
    template_name = 'bingo/form.html'
    success_url = reverse_lazy('bingo:index')

    def dispatch(self, request, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            if MainMod.objects.get(user=request.user).mod:
                return super().dispatch(request, *args, **kwargs)
            return redirect('bingo:create2')
        except MainMod.DoesNotExist:
            return redirect('bingo:main')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        bingo, _ = BingoModel.objects.get_or_create(user=user)
        form.instance.bingo = bingo
        new = form.cleaned_data
        try:
            old = DataModel.objects.get(user=user)
        except DataModel.DoesNotExist:
            old = False

        if old:
            for i in range(1, 26):
                field = f'field{i}'
                if getattr(old, field) != new[field]:
                    setattr(bingo, field, False)
            bingo.save()
        DataModel.objects.update_or_create(
                user=user,
                defaults=form.cleaned_data,
                bingo=bingo
        )
        return redirect(self.success_url)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        try:
            data = DataModel.objects.get(user=user)
        except DataModel.DoesNotExist:
            data = False
        if data:
            initial = {}
            for i in range(1, 26):
                field = f'field{i}'
                obj = getattr(data, field)
                initial[field] = obj
            kwargs['initial'] = initial
        return kwargs



@login_required
def push_view(request):
    try:
        if not MainMod.objects.get(user=request.user).mod:
            return redirect('bingo:index2')
    except MainMod.DoesNotExist:
        return redirect('bingo:main')
    try:
        bingo = BingoModel.objects.get(user=request.user)
    except BingoModel.DoesNotExist:
        return redirect('bingo:create')
    if request.method == 'POST':
        data = json.loads(request.body)
        number = data['number']
        field = f'field{number}'
        val = getattr(bingo, field)
        if val:
            setattr(bingo, field, False)
        else:
            setattr(bingo, field, True)
        bingo.save()
    template = 'bingo/list.html'
    data = DataModel.objects.get(user=request.user)
    context = {'list': data, 'bingo': bingo}
    return render(request, template, context)


def calc_progress(request):
    bingo, flag = calc(BingoModel.objects.get(user=request.user), 5)
    bingo.save()
    return JsonResponse({'data': bingo.progress, 'flag': flag})


class CreateMatrixViewThree(LoginRequiredMixin, CreateView):
    model = DataModelThree
    form_class = DataFormThree
    template_name = 'bingo/form.html'
    success_url = reverse_lazy('bingo:index2')

    def dispatch(self, request, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            if not MainMod.objects.get(user=request.user).mod:
                return super().dispatch(request, *args, **kwargs)
            return redirect('bingo:create')
        except MainMod.DoesNotExist:
            return redirect('bingo:main')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        bingo, _ = BingoModelThree.objects.get_or_create(user=user)
        form.instance.bingo = bingo
        new = form.cleaned_data
        try:
            old = DataModelThree.objects.get(user=user)
        except DataModelThree.DoesNotExist:
            old = False

        if old:
            for i in range(1, 10):
                field = f'field{i}'
                if getattr(old, field) != new[field]:
                    setattr(bingo, field, False)
            bingo.save()
        DataModelThree.objects.update_or_create(
                user=user,
                defaults=form.cleaned_data,
                bingo=bingo
        )
        return redirect(self.success_url)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        try:
            data = DataModelThree.objects.get(user=user)
        except DataModelThree.DoesNotExist:
            data = False
        if data:
            initial = {}
            for i in range(1, 10):
                field = f'field{i}'
                obj = getattr(data, field)
                initial[field] = obj
            kwargs['initial'] = initial
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mod'] = 3
        return context


@login_required
def push_view2(request):
    try:
        if MainMod.objects.get(user=request.user).mod:
            return redirect('bingo:index')
    except MainMod.DoesNotExist:
        return redirect('bingo:main')
    try:
        bingo = BingoModelThree.objects.get(user=request.user)
    except BingoModelThree.DoesNotExist:
        return redirect('bingo:create2')
    if request.method == 'POST':
        data = json.loads(request.body)
        number = data['number']
        field = f'field{number}'
        val = getattr(bingo, field)
        if val:
            setattr(bingo, field, False)
        else:
            setattr(bingo, field, True)
        bingo.save()
    template = 'bingo/list2.html'
    data = DataModelThree.objects.get(user=request.user)
    context = {'list': data, 'bingo': bingo}
    return render(request, template, context)


def calc_progress2(request):
    bingo, flag = calc(BingoModelThree.objects.get(user=request.user), 3)
    bingo.save()
    return JsonResponse({'data': bingo.progress, 'flag': flag})


@login_required
def main(request):
    user = request.user
    mod_instance, created = MainMod.objects.update_or_create(user=user)

    if request.method == 'POST':
        form = TestForm(request.POST, instance=mod_instance)
        if form.is_valid():
            form.save()
            return redirect('bingo:index')
    else:
        form = TestForm(instance=mod_instance)

    return render(request, 'bingo/main.html', {'form': form})
