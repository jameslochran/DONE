from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project/', views.ProjectView.as_view(), name='project'),
    path('project/<int:id>/', views.ProjectDetailView.as_view(), name='projectdetail'),
    path('project/<int:id>/update/', views.ProjectUpdateView.as_view(), name='project_update_form'),
    path('project/<int:id>/delete/', views.ProjectDeleteView.as_view(), name='project_confirm_delete'),
    #path('connect/<int:pk/', views.addfriend, name='add_friend'),
    #path('remove/<int:pk/', views.removefriend, name='remove_friend'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
