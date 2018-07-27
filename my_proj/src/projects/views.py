from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from .models import Project, Item
from . import forms
from projects.forms import ProjectForm

class IndexView(generic.ListView):
    template_name = 'projects/index.html'

    def get(self, request):
        form = ProjectForm
        return render(request, self.template_name)

    # def get_queryset(self):
    #     """
    #     Return the last five published projects (not including those set to be
    #     published in the future).
    #         """
    #     return Project.objects.filter(
    #             pub_date__lte=timezone.now()
    #             ).order_by('-pub_date')[:5]

class CreateView(generic.CreateView):
    model = Project
    template_name = 'projects/create.html'
    http_method_names = ['post']
    pass

    #def get(self, request, *args, **kwargs):
        #user = self.request.user
        #project = self.request.project
        # if "user_form" not in kwargs:
        #     kwargs["user_form"] = forms.UserForm(instance=user)
        # if "project_form" not in kwargs:
        #     kwargs["project_form"] = forms.ProjectForm(instance=project.user)
        #return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     #user = self.request.user
    #     #user_form = forms.UserForm(request.POST, instance=user)
    #     project_form = forms.ProjectForm(request.POST,
    #                                      request.FILES,
    #                                      instance=user.project)
    #     if not (user_form.is_valid() and project_form.is_valid()):
    #         messages.error(request, "There was a problem with the form. "
    #                        "Please check the details.")
    #         user_form = forms.UserForm(instance=user)
    #         project_form = forms.ProjectForm(instance=user.project)
    #         return super().get(request,
    #                            user_form=user_form,
    #                            project_form=project_form)
    #     # Both forms are fine. Time to save!
    #     user_form.save()
    #     project = project_form.save(commit=False)
    #     project.user = user
    #     project.save()
    #     messages.success(request, "Project details saved!")
    #     return redirect("projects:index")





class DetailView(generic.DetailView):
     model = Project
     template_name = 'project/detail.html'
     pass
#     def get_queryset(self):
#         """
#         Excludes any projects that aren't published yet.
#         """
#         return Project.objects.filter(pub_date__lte=timezone.now())


# class ResultsView(generic.DetailView):
#     #model = Question
#     template_name = 'project/results.html'
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
