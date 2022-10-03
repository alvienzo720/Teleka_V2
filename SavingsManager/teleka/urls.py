from django.urls import path

from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('creat-member/',CreateMember.as_view(),name='create-member'),
    path('view-members/',ViewMembers.as_view(),name='view-members'),
    path('member-update/<int:pk>/', MemberUpdate.as_view(), name='member-update'),
    path('member-delete/<int:pk>/', MemberDelete.as_view(), name='member-delete'),
    path('member/<int:pk>/', MemberDetails.as_view(), name='member'),
    path('create-deposit/',CreateDeposit.as_view(),name='create-deposit'),
    path('view-deposits/',ViewDeposit.as_view(),name='view-deposits'),

    ]


