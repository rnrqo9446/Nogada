from django.shortcuts import render,get_object_or_404, redirect
from .models import Musical,Exhibition,Concert,Classic,Musical_Comment, Exhibition_Comment, Concert_Comment, Classic_Comment
from .forms import Musical_CommentForm, Exhibition_CommentForm, Concert_CommentForm, Classic_CommentForm


def home(request):
    musicals=Musical.objects
    return render(request, 'show/home.html',{'musicals':musicals})

def musical_home(request):
    musicals=Musical.objects
    return render(request, 'show/musical_home.html',{'musicals':musicals})

def musical_detail(request,musical_id):
    musical_detail=get_object_or_404(Musical,pk= musical_id)
    form = Musical_CommentForm()
    return render(request, 'show/musical_detail.html',{'musical':musical_detail, 'form':form,})

def musical_add_comment(request, musical_id):
    post = get_object_or_404(Musical, pk=musical_id)
    if request.method == "POST":
        form = Musical_CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('musical_detail', musical_id=post.pk)


def exhibition_home(request):
    exhibitions=Exhibition.objects
    return render(request, 'show/exhibition_home.html',{'exhibitions':exhibitions})

def exhibition_detail(request,exhibition_id):
    exhibition_detail=get_object_or_404(Exhibition,pk= exhibition_id)
    return render(request, 'show/exhibition_detail.html',{'exhibition':exhibition_detail})

def exhibition_add_comment(request, exhibition_id):
    post = get_object_or_404(Exhibition, pk=exhibition_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('exhibition_detail', exhibition_id=exhibition.pk)

def concert_home(request):
    concerts=Concert.objects
    return render(request, 'show/concert_home.html',{'concerts':concerts})

def concert_detail(request,concert_id):
    concert_detail=get_object_or_404(Concert,pk= concert_id)
    return render(request, 'show/concert_detail.html',{'concert':concert_detail})

def concert_add_comment(request, concert_id):
    post = get_object_or_404(Concert, pk=concert_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('concert_detail', concert_id=concert.pk)

def classic_home(request):
    classics=Classic.objects
    return render(request, 'show/classic_home.html',{'classics':classics})

def classic_detail(request,classic_id):
    classic_detail=get_object_or_404(Classic,pk= classic_id)
    return render(request, 'show/classic_detail.html',{'classic':classic_detail})

def classic_add_comment(request, classic_id):
    post = get_object_or_404(Classic, pk=classic_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('classic_detail', classic_id=classic.pk)