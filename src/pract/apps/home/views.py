from django.shortcuts import render
from django.views.generic import ListView
from pract.apps.discuss.models import Question

from pract.apps.users.models import User

class IndexView(ListView):
    template_name = 'index.html'
    # model = Question
    queryset = Question.objects.all()[:5]
    context_object_name = 'home_list'

    def get_queryset(self):
        tags = [ question.tag.all() for question in self.queryset ]
        return zip(self.queryset, tags)

    def get_context_data(self, **kwargs):
        context =  super(IndexView, self).get_context_data(**kwargs)
        context['total_question'] = Question.objects.count()
        context['total_users'] = User.objects.exclude(is_superuser=True).count()
        return context
