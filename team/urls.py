from django.urls import path, include
from .views import *
urlpatterns = [
    path('MemberDashboard/', MemberDashboard, name='MemberDashboard'),
    path('AddTeamMember/', AddTeamMember, name='AddTeamMember'),
    path('TeamMembers/', TeamMembers, name='TeamMembers'),
    path('TeamMembers/<slug:slug>/', MemberProfiles, name='MemberProfile'),
    path('MemberEvaluation/', MemberEvaluations, name='MemberEvaluations'),
    path('evaluation/', Evaluation, name='Evaluation'),


    # path('loginUser/', loginUser, name='loginUser'),
    # path('verify/<auth_token>', verify, name='verify'),
    # path('error', error_page, name='error')
] 