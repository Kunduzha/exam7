from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Poll
from webapp.forms import PollForms


class IndexPoll(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    paginate_by = 5
    paginate_orphans = 3

    def get_queryset(self):
        return Poll.objects.all().order_by('-created_at')

class PollView(DetailView):
    model = Poll
    template_name = 'poll/poll_view.html'



class AddPoll(CreateView):
    template_name = 'poll/create.html'
    model = Poll
    form_class = PollForms

    def get_success_url(self):
        return reverse('main_page')

class PollUpdate(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForms
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_more', kwargs={'pk': self.object.pk})

class DeletePoll(DeleteView):
    template_name = 'poll/delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('main_page')