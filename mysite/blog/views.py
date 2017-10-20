from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .models import Resume
from .forms import Resumeform
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


########### index page ################
def index(request):
    return render(request, 'index.html', {})






def post_new(request):
    return render(request, 'post_new.html', {})




############## ADD NEW Resume or new post for form1##################
@user_passes_test(lambda u: u.is_superuser)
def post_ONE(request):

    if request.method == "POST":
        form = Resumeform(request.POST or None, request.FILES or None )
        post = form.save(commit=False)
        if form.is_valid():
           post.published_date = timezone.now()
           post.save()
           return redirect('form1detail', pk=post.pk)
    else:
        form = Resumeform()
    return render(request, 'post_ONE.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def post_TWO(request):

    if request.method == "POST":
        form = Resumeform(request.POST or None, request.FILES or None)
        post = form.save(commit=False)
        if form.is_valid():
           post.published_date = timezone.now()
           post.save()
           return redirect('form2detail', pk=post.pk)
    else:
        form = Resumeform()
    return render(request, 'post_TWO.html', {'form': form})



@user_passes_test(lambda u: u.is_superuser)
def post_THREE(request):

    if request.method == "POST":
        form = Resumeform(request.POST or None, request.FILES or None)
        post = form.save(commit=False)
        if form.is_valid():
           post.published_date = timezone.now()
           post.save()
           return redirect('form3detail', pk=post.pk)
    else:
        form = Resumeform()
    return render(request, 'post_THREE.html', {'form': form})




########## filter the resume by created date and show the name of the person ################
def resume(request):
    posts = Resume.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'resume.html', {'posts':posts})



############ detail of the person ###############
def form1detail(request, pk):
    post = Resume.objects.get(pk=pk)
    return render(request, 'form1.html', {'post': post})

def form2detail(request, pk):
    post = Resume.objects.get(pk=pk)
    return render(request, 'form2.html', {'post': post})

def form3detail(request, pk):
    post = Resume.objects.get(pk=pk)
    return render(request, 'form3.html', {'post': post})


########### Edit the Resume #############
def post_edit(request, pk):
    post = get_object_or_404(Resume, pk=pk)
    if request.method == "POST":
        form = Resumeform(request.POST, instance=post)
        post = form.save(commit=False)
        if form.is_valid():

            post.published_date = timezone.now()
            post.save()
            return redirect('form1detail', pk=post.pk)
    else:
        form = Resumeform(instance=post)
    return render(request, 'post_ONE.html', {'form': form})



####### Delete #######
def post_remove(request, pk):
    post = get_object_or_404(Resume, pk=pk)
    post.delete()
    return redirect('resume')

############ detail of the person ###############
def detail(request, pk):
    post = Resume.objects.get(pk=pk)
    return render(request, 'form1.html', {'post': post})
