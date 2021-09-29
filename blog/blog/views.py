import logging

from django.shortcuts import render

from posts.forms import RegistrationForm

logger = logging.getLogger(__name__)


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data)
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})