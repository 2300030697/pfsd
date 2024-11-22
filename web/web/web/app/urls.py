from django.urls import path
from . import views
from .views import working_view, chatbot_view

urlpatterns = [
    path('', views.base, name='base'),  # Root path to base view
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('contactus/', views.contactus_view, name='contactus'),
    path('getstarted/', views.getstarted_view, name='getstarted'),
    path('getstarted/german/', views.german_view, name='german'),
    path('getstarted/french/', views.french_view, name='french'),
    path('getstarted/english/', views.english_view, name='english'),
    path('getstarted/spanish/', views.spanish_view, name='spanish'),
    path('getstarted/italian/', views.italian_view, name='italian'),
    path('working/', working_view, name='working'),
    path('chatbot/', chatbot_view, name='chatbot'),

    # German quizzes
    path('getstarted/german/gaquiz/', views.ga_quiz, name='ga_quiz'),
    path('getstarted/german/gbquiz/', views.gb_quiz, name='gb_quiz'),
    path('getstarted/german/gc/', views.gc, name='gc'),
    path('getstarted/german/gd/', views.gd, name='gd'),

    # French quizzes
    path('getstarted/french/fa/', views.fa, name='fa'),
    path('getstarted/french/fb/', views.fb, name='fb'),
    path('getstarted/french/fc/', views.fc, name='fc'),
    path('getstarted/french/fd/', views.fd, name='fd'),

    # Spanish quizzes
    path('getstarted/spanish/sa/', views.sa, name='sa'),
    path('getstarted/spanish/sb/', views.sb, name='sb'),
    path('getstarted/spanish/sc/', views.sc, name='sc'),
    path('getstarted/spanish/sd/', views.sd, name='sd'),

    # Italian quizzes
    path('getstarted/italian/ia/', views.ia, name='ia'),
    path('getstarted/italian/ib/', views.ib, name='ib'),
    path('getstarted/italian/ic/', views.ic, name='ic'),
    path('getstarted/italian/id/', views.id, name='id'),

    # English quizzes
    path('getstarted/english/ea/', views.ea, name='ea'),
    path('getstarted/english/eb/', views.eb, name='eb'),
    path('getstarted/english/ec/', views.ec, name='ec'),
    path('getstarted/english/ed/', views.ed, name='ed'),
]
