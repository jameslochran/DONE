from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from polls.models import Choice, Question, Project, Friend
from polls.forms import PForm
#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django import template

register = template.Library()
#from django.template import loader
#from django.http import Http404

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

#User = get_user_model()

class ProjectView(TemplateView):
    template_name = 'polls/project.html'

    def get(self, request):
        form = PForm()
        User = get_user_model()
        queryset = Project.objects.all()
        projects = Project.objects.all().order_by('-date_created')
        myprojects = Project.objects.filter(user = request.user).order_by('-date_created')
        # friends = Friend.objects.get(current_user=request.user)
        # friends = friend.users.all()

        #User = get_user_model()
        #users = User.objects.all()
        users = User.objects.exclude(id=request.user.id)

        args = {'form': form, 'projects': projects, 'myprojects': myprojects, 'users': users}
        return render(request, self.template_name, args)



    def post(self, request):
        form = PForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['project']
            form = PForm()
            return redirect('polls:project')

        args = {'form': form,}
        return render(request, self.template_name, args)


class ProjectDetailView(generic.DetailView):
    template_name = 'polls/projectdetail.html'
    #http_method_names = ['get']
    #model = Project
    queryset = Project.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')

        return get_object_or_404(Project, id=id_)


class ProjectUpdateView(UpdateView):

    model = Project
    #template_name = 'polls/projectupdate.html'
    template_name_suffix = '_update_form'
    fields = ['project','description', 'resolution', 'startdate', 'deadline', 'budget', 'state']
    success_url = reverse_lazy('polls:project')


    def get_object(self):
        id_ = self.kwargs.get('id')
    #
        return get_object_or_404(Project, id=id_, )


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('polls:project')

    def get_object(self):
        id_ = self.kwargs.get('id')

        return get_object_or_404(Project, id=id_, )


def addfriend(request, pk):
    return redirect('polls:projects')

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'



    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
            """
        return Question.objects.filter(
                pub_date__lte=timezone.now()
                ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
