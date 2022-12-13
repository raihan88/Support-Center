from django.urls import path
# from . import views
from .views import (HomeView, 
    QA_DetailView,
    AskQuestionView, 
    UpdatePostView,
    DeletePostView, 
    AddCommentView,
    AddQuestionView,
    PendingQuestionView,
    AnswerQuestionView)

urlpatterns = [ 
    path('',HomeView.as_view(), name = 'home'), 
    path('qa/<int:pk>',QA_DetailView.as_view(), name = 'qa_detail'),
    path('ask_question/', AskQuestionView.as_view(), name = 'ask_question'), 
    path('edit_question/<int:pk>', UpdatePostView.as_view(), name = 'edit_question'), 
    path('qa/<int:pk>/delete', DeletePostView.as_view(), name = 'delete_question'), 
    path('qa/<int:pk>/add_comment',AddCommentView.as_view(), name = 'add_comment'),
    path('add_question/', AddQuestionView.as_view(), name = 'add_question'), 
    path('pending_questions/',PendingQuestionView.as_view(), name = 'pending_questions'), 
    path('answer_question/<int:pk>', AnswerQuestionView.as_view(), name = 'answer_question'), 


    
]
