from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseBadRequest
from models import Foodie
from forms import FoodieForm, UnsubscribeForm


def signup(request):
    """
    Basic Signup.  Also used as index page
    :param request: Http request
    :return: HttpResponse
    """
    alert = "";
    if request.method == "POST":
        form = FoodieForm(request.POST)
        if form.is_valid():
            form.save()
            alert = "Successfully signed up.  Thanks!"
    else:
        form = FoodieForm()
    unform = UnsubscribeForm()
    return render_to_response("signup-unsubscribe.html", {"form": form, "unform": unform, "alert": alert},
                              context_instance=RequestContext(request))


def unsubscribe(request):
    if request.method != "POST":
        return HttpResponseBadRequest("")
    alert = ""
    form = FoodieForm()
    unform = UnsubscribeForm(request.POST)
    if unform.is_valid():
        qs = Foodie.objects.filter(email__iexact=unform.cleaned_data["email"])
        if len(qs) > 0:
            qs.delete()
            alert = "Email " + unform.cleaned_data["email"] + " has been successfully removed."
        else:
            alert = "Email " + unform.cleaned_data["email"] + " not found in database.  Probably already un-subscribed."
    return render_to_response("signup-unsubscribe.html", {"form": form, "unform": unform, "alert": alert},
                              context_instance=RequestContext(request))