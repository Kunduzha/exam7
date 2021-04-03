from webapp.models import Choice, Poll
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, TemplateView, RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode


from webapp.forms import ChoiceForms




class Answer(ListView):
    template_name = 'poll/poll_view.html'
    context_object_name = 'answers'
    model = Choice
    ordering = ['-created_at']




# class AddAnswer(CreateView):
#
#     model = Choice
#     template_name = 'answer/add.html'
#     form_class = ChoiceForms
#
#     def form_valid(self, form):
#         poll = get_object_or_404(Poll, pk = self.kwargs.get('pk'))
#         answer = form.save(commit=False)
#         answer.poll = poll
#         answer.save()
#         return redirect('poll_more', pk=poll.pk)


class AddAnswer(CreateView):
    template_name = 'answer/add.html'
    form_class = ChoiceForms
    model = Choice

    def get_success_url(self):
        return reverse(
            'poll_more',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        poll = get_object_or_404(Poll, id=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)

class AnswerUpdate(UpdateView):
    model = Choice
    template_name = 'answer/update.html'
    form_class = ChoiceForms
    context_object_name = 'answer'

    def get_success_url(self):
        return reverse('poll_more', kwargs={'pk': self.object.poll.pk})


class DeleteAnswer(DeleteView):
    model = Choice
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('poll_more', kwargs={'pk': self.object.poll.pk})



