from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Poll, AnswerForPoll, Choice
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


class ResultsView(generic.DetailView):
    model = AnswerForPoll
    template_name = 'poll/poll_answer.html'

def vote(request, poll_id):
    question = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'poll/poll_view.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))