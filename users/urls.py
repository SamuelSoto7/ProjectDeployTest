from django.urls import path
from . import views
from .views import UserListView, AllUserListView
from .views import InstitutionVerifyView
from .views import InstitutionRejectVerificationView

app_name = 'users'

urlpatterns = [path("signupBen/", views.SignUpBen.as_view(), name="signupb"), 
               path("signupDon/", views.SignUpDon.as_view(), name="signupd"),
               path("signupLegalDon/", views.SignUpLegalDon.as_view(), name="signupld"),  
               path("signupIns/", views.SignUpIns.as_view(), name="signupi"),
               path("signupAdm/", views.SignUpAdmin.as_view(), name="signupAdm"),
               path("sigin/", views.SigIn.as_view(),name="sigin"), 
               path("menu/", views.SigIn.as_view(),name="menu"), 
                path('beneficiaries/<int:pk>/update/', views.BeneficiaryUpdateView.as_view(), name='beneficiary_update'),
                path('naturaldonors/<int:pk>/update/', views.NaturalDonorUpdateView.as_view(), name='natural_donor_update'),
                path('legaldonors/<int:pk>/update/', views.LegalDonorUpdateView.as_view(), name='legal_donor_update'),
                path('institutions/<int:pk>/update/', views.InstitutionUpdateView.as_view(), name='institution_update'),
                path('institutions/', UserListView.as_view(), name='user_list'),
                path('users/institutions/<int:pk>/verify/', InstitutionVerifyView.as_view(), name='verify_institution'),
                path('users/institutions/<int:pk>/reject-verification/', InstitutionRejectVerificationView.as_view(), name='reject_verification'),
                path('users/<int:pk>/activar/', views.ActiveUserView.as_view(), name='active_user'),
                path('users/<int:pk>/inactivar/', views.InactiveUserView.as_view(), name='inactive_user'),
                path('users/', AllUserListView.as_view(), name='showUsers'),
                path('users/showDetails/<int:id>/', views.ShowDetailsUsers.as_view(), name='showdetailsusers'),]   
                