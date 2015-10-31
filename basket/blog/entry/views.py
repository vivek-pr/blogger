from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog_Entry
from .forms import AddForm,UserForm
from django.contrib.auth import authenticate
from datetime import date, timedelta


def entry(request, slug):
    post = get_object_or_404(Blog_Entry, slug=slug)
    d = date.today() - timedelta(days=1)
    value=Blog_Entry.objects.filter(approved=True).filter(visited_date__gte=d)
    post.update()
    return render(request, 'detail_blog.html', {
        'post': post,'value':value
    })

def add(request):
    if "user" in request.session:
        if request.method == 'POST':
            form = AddForm(request.POST)
            if form.is_valid():
                entry = form.save()
                d = date.today() - timedelta(days=1)
                value=Blog_Entry.objects.filter(approved=True).filter(visited_date__gte=d)
                return render(request,'blog_log.html',{'value':value})
        else:
            form = AddForm()

        return render(request, 'entry.html', {
            'form': form,
        })
    else:
        return render(request,'authorsignin.html',{'form':UserForm()})



def blog(request):
    if request.method=='POST':
        form=UserForm(data=request.POST)

        user = authenticate(username=form.data['username'], password=form.data['password'])
        if user is not None:
            request.session['user']=form.data['username']
            return render(request,'entry.html',{'form': AddForm(),})
        else:
            print('user invalid')
            message='You are not authorized to write please read articles'
            return render(request,'authorsignin.html',{'form':UserForm(),'message':message})




    #title_detail=Blog_Form.objects.get()
    d = date.today() - timedelta(days=1)
    value=Blog_Entry.objects.filter(approved=True).filter(visited_date__gte=d)
    return render(request,'blog_log.html',{'value':value})


def about(request):
    return render(request,'about.html',{})
