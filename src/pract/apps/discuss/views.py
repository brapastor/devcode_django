from django.shortcuts import render
from django.views.generic import ListView,  CreateView, DetailView
from .models import Question, Tag, Answer
from .forms import CreateQuestionForm
from braces.views import LoginRequiredMixin

class QuestionListView(ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'

    def get_context_data(self, **kwargs):
        context =  super(QuestionListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class QuestionCreateView(LoginRequiredMixin,CreateView):

    model = Question
    template_name = 'question_form.html'
    # fields = '__all__'
    form_class = CreateQuestionForm
    success_url = '/'
    login_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuestionCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(QuestionCreateView, self).form_invalid(form)

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'

    def get_answers(self,question):
        answers = Answer.objects.filter(question=question)
        return answers

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['answers'] = self.get_answers(context['object'])
        # context['answers'] = Answer.objects.filter(question=context['object'])
        return context


    def post(self,request,*args, **kwargs):
        answer = Answer()
        #tomamos el usuario que esta registrado
        answer.user = request.user
        # Texto que me mandan por el formulario
        answer.description = request.POST['description']
        # ENVIAMOS el objeto de la pregunta en la que se esta respondiendo
        answer.question = Question.objects.get(slug= kwargs['slug'])
        answer.save()
        answers = self.get_answers(answer.question)
        return render(request, 'question_detail.html', {'question': answer.question, 'answers':answers})
