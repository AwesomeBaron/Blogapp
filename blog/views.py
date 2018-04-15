from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail




def post_list(request):
    object_list = Post.published.all().order_by("-publish")
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = 'blog/post/list.html'
    context = {
        'posts': posts,
        'page': page,
    }
    return render(request, template, context )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    comments = post.comments.filter(approved_comment=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
    else:
        comment_form = CommentForm
    template = 'blog/post/detail.html',
    context ={
        'post': post,
        'comments': comments,
        'comment_form': comment_form}
    return render(request, template, context)


def post_share(request, post_id):
    #Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        #Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # post_url = request.build_absolute_uri(
            #     post.get_absolute_url())
            # subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            # message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            # send_mail(subject, message, 'admin@myblog.com',
            #           [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    template = 'blog/post/share.html'
    context = {
        'post': post,
        'form': form,
        'sent': sent,
    }
    return render(request, template, context)



