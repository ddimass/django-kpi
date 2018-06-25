from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Org
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, ListView):
    model = Org

    def get_queryset(self):
        if self.request.user.is_staff:
            return Org.objects.all()
        return Org.objects.filter(user=self.request.user)



class AddView(LoginRequiredMixin, CreateView):
    model = Org
    fields = ['name']
    success_url = "/org/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
