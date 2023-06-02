from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView

from classroom.models import Teacher
from classroom.forms import ContactForm

# Create your views here.
# def home_view(request):
#     return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:thank_you")

class TeacherListView(ListView):
    # model_list.html
    model = Teacher

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    
    # success url?
    # success_url = "/classroom/thank_you/"
    success_url = reverse_lazy("classroom:thank_you")
    # swhatto do iwth form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherDetailView(DetailView):
    # RETURN only one model entry PK
    # model_detail.html
    model = Teacher
    # PK -> {{teacher}}