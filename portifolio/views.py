from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.
def home_views(request, *args, **kwargs):
    post = Post.objects.all()[0:6]
    context = {
        "posts": post
    }
    return render(request, "pages/home.html", context)


def blog_home(request, *args, **kwargs):
    form = PostForm()
    context = {
        "form": form
    }
    return render(request, "pages/blog/blog.html", context)


def blog_feeds_home(request, *args, **kwargs):
    form = PostForm()
    context = {
        "form": form
    }
    return render(request, "pages/blog/feeds.html", context)


def blog_detail_views(request, slug, *args, **kwargs):
    try:
        qs = Post.objects.get(slug=slug)
    except:
        raise Http404
    context = {
        "post": qs
    }
    return render(request, "pages/blog/detail.html", context)


def post_list_views(request, *args, **kwargs):
    qs = Post.objects.all()[0:12]

    post_list = [{"id": x.id, "title": x.title, "content": x.content, "publish": x.publish} for x in qs]
    data={
        "response":post_list
    }
    return JsonResponse(data)


def post_detail_views(request, slug, *args, **kwargs):
    data = {
        "slug": slug
    }
    try:
        qs = Post.objects.get(id=slug)
        qs_comment = Comment.objects.filter(post=slug)
        comment_list = [{"id": x.id, "content": x.content} for x in qs_comment]
        data["title"] = qs.title
        data["content"] = qs.content
        data["comments"] = comment_list
        data["count"] = str(len(comment_list))


    except:
        data["message"] = "Page do not found"
    return JsonResponse(data)

def create_comment_views(request, *args, **kwargs):
    user = request.user
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.user = user
        form_obj.save()
        data = {
            "response": form.data
        }
        return JsonResponse(data)
    