from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import ClanekForm, RegistraceForm, PrihlaseniForm, PostavaForm
from .models import Clanek, Postava


# Create your views here.
def clanek_list(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'bloxov/clanek_list.html', {'clanky': clanky, 'postavy': postavy})


def clanek_detail(request, pk):
    clanek = get_object_or_404(Clanek, pk=pk)
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'bloxov/clanek_detail.html', {'clanek': clanek, 'postavy': postavy})


def clanek_new(request):
    postavy = Postava.objects.order_by('prijmeni')
    IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
    if request.method == "POST":
        form = ClanekForm(request, request.POST, request.FILES)
        if form.is_valid:
            clanek = form.save()
            clanek.obrazek = request.FILES['obrazek']
            file_type = clanek.obrazek.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                print("Wrong type:", file_type)
            clanek.autor = request.user
            clanek.publikovano = timezone.now()
            clanek.save()
            return redirect('clanek_detail', pk=clanek.pk)
    else:
        form = ClanekForm()
    return render(request, 'bloxov/clanek_edit.html', {'form': form, 'postavy': postavy})


def clanek_delete(request, pk):
    clanek = get_object_or_404(Clanek, pk=pk)
    clanek.delete()


def bazos(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'bloxov/bazos_list.html', {'clanky': clanky, 'postavy': postavy})


def internet(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'bloxov/internet_list.html', {'clanky': clanky, 'postavy': postavy})


def instablox(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'bloxov/instablox_list.html', {'clanky': clanky, 'postavy': postavy})


def bloxnews(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'bloxov/blox_list.html', {'clanky': clanky, 'postavy': postavy})


def uredka(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'bloxov/uredka_list.html', {'clanky': clanky, 'postavy': postavy})


@login_required
def special(request):
    return render(request, 'bloxov/clanek_list.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


def registr(request):
    if request.method == "POST":
        form = RegistraceForm(request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password1')
        if form.is_valid:
            osoba = form.save()
            uziv = authenticate(username=name, password=passw)
            osoba.save()
            login(request, uziv)
            return redirect('/')
    else:
        form = RegistraceForm()
    return render(request, 'bloxov/signup_screen.html', {'form': form})


def prihlas(request):
    if request.method == 'POST':
        form = PrihlaseniForm(request, request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password')
        if form.is_valid:
            osoba = authenticate(username=name, password=passw)
            login(request, osoba)
            return redirect('/')
    else:
        form = PrihlaseniForm()
    return render(request, 'bloxov/login_screen.html', {'form': form})


def profil(request):
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'bloxov/profil.html', {'postavy': postavy})


def postava_new(request):
    postavy = Postava.objects.order_by('prijmeni')
    if request.method == "POST":
        form = PostavaForm(request.POST)
        if form.is_valid():
            postava = form.save(commit=False)
            postava.majitel = request.user
            postava.vytvoreno = timezone.now()
            postava.cele_jmeno = postava.full_jmeno()
            postava.save()
            return redirect('postava_detail', pk=postava.pk)
    else:
        form = PostavaForm()
    return render(request, 'bloxov/postava_new.html', {'form': form, 'postavy': postavy})


def postava_detail(request, pk):
    postava = get_object_or_404(Postava, pk=pk)
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'bloxov/postava_detail.html', {'postava': postava, 'postavy': postavy})


def postava_delete(request, pk):
    postava = get_object_or_404(Postava, pk=pk)
    postava.delete()


class DeleteThing(DeleteView):
    model = Clanek
    success_url = reverse_lazy('author-list')
