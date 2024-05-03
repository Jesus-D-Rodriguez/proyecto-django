from django.shortcuts import render, redirect
from .forms import BlogPostForm
from django.utils import timezone

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')

    else:
        form = BlogPostForm(initial={'pub_date': timezone.now().strftime('%Y-%m-%d %H:%M:%S')})
    return render(request, 'new_post.html', {'form': form})
