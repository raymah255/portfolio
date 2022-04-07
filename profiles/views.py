from django.http import Http404
from .models import Profile
from django.shortcuts import redirect, render



from .forms import ProfileForm

# Create your views here.

def profile_views(request, username, *args, **kwargs):
    user = request.user
    profile = user.profile
    user_data = {"first_name": user.first_name, "last_name": user.last_name, "email_address": user.email, "location": profile.location}
    form = ProfileForm(initial=user_data)

    if not request.user.is_authenticated:
        return redirect("/accouts/login")
    
    else:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES or None, instance=profile, initial=user_data)
            if form.is_valid():
                form_obj= form.save(commit=False)
                first_name = form.cleaned_data.get("first_name")
                last_name = form.cleaned_data.get("last_name")
                email_address = form.cleaned_data.get("email_address")
                user.first_name = first_name
                user.last_name = last_name
                user.email = email_address
                user.save()
                form_obj.save()
                return redirect("/profile/"+username)
    context ={
        "form": form
    }
    return render(request, "pages/profile.html", context)


def my_profile_views(request, username, *args, **kwargs):
    profile_qs = Profile.objects.filter(user__username = username)
    if not request.user.is_authenticated:
        return redirect("/accounts/login")
    else:
        if not profile_qs.exists():
            return Http404
        profile = profile_qs.first()
        context = {
            "profile": profile
        }
    return render(request, "pages/myprofile.html", context)