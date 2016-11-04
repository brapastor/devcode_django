from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import View, DetailView
from .forms import ExtraDataForms
from django.core.mail import EmailMessage
from .models import User
from pract.apps.discuss.models import Question
def LogOut(request):
    logout(request)
    return redirect('/')


class ExtraDataView(View):
    def get(self,request, *args, **kwargs):
        if request.user.status or request.user.email:
            return redirect('/')
        else:
            return render(request, 'extra_data.html')

    def post(self,request,*args,**kwargs):
        form = ExtraDataForms(request.POST)

        if form.is_valid():
            request.user.username = request.POST['username']
            request.user.email = request.POST['email']
            request.user.status = True
            request.user.save()
            # send_email(request)
            return redirect('/')

        else:
            error_username = form['username'].errors.as_text()
            error_email = form['email'].errors.as_text()
            ctx = {'error_username': error_username, 'error_email':error_email}
            return render(request, 'extra_data.html', ctx)


def send_email(request):
    msg =  EmailMessage(subject='Bienvenida',
                        from_email='Brayan PAstr <brapasto@gmail.com>',
                        to=[request.user.email])

    msg.template.name = 'welcome'
    msg.template_content = {
        'std_content00': '<h1> Hola %s Bienvenido a Michudes' % request.user
    }
    msg.send()

class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = User
    context_object_name = 'user'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        #  Mandamos mas contexto a la vista
        # Pasamos el contexto que nosotros queramos
        context = super(UserDetailView, self).get_context_data(**kwargs)
        questions = Question.objects.filter(user= context['object']).order_by('created')
        tags = [question.tag.all() for question in questions]
        context['ques_tags'] = zip(questions,tags)

        facebook = context['object'].social_auth.filter(provider='facebook')
        if facebook:
            context['facebook'] = facebook[0].extra_data['id']

        twitter = context['object'].social_auth.filter(provider= 'twitter')
        if twitter:
            context['twitter'] =  twitter[0].extra_data['access_token']['screen_name']

        return context


