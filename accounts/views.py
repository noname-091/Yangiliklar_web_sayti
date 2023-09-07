from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForms
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForms
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'