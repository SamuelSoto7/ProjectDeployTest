from django.urls import path
from users.views import BeneficiaryUpdateView
from . import views
from .views import NewDonation, TransactionListView,ScholarshipListView,DonationsListView, ContactView 
from .views import InstitutionListView

app_name = 'scholarships'

urlpatterns = [path("showmenu/", views.ShowMenu.as_view(), name="showmenu"), 
               path("newapplication/", views.NewApplication.as_view(), name="newapplication"),
               path("lookapplications/", views.LookApplication.as_view(), name="lookapplication"),
               path("insertScholarship/", views.InsertScholarship.as_view(), name="insertScolarship"),
                path('beneficiaries/<int:pk>/update/', views.BeneficiaryUpdateView.as_view(), name='beneficiary_profile_update'),
                path('naturaldonor/<int:pk>/update/', views.NaturalDonorUpdateView.as_view(), name='natural_donor_profile_update'),
                path('legaldonor/<int:pk>/update/', views.LegalDonorUpdateView.as_view(), name='legal_donor_profile_update'),
                path('institution/<int:pk>/update/', views.InstitutionUpdateView.as_view(), name='institution_profile_update'),
                path("soli_Activa/", views.ActiveSolicitud.as_view(), name="soli_Activa"),
                path("editSolicitudActiva/", views.EditSolicitud.as_view(), name='editSolicitudActiva'),
                path("newdonation/", NewDonation.as_view(), name='newdonation'),
                path("lookbeneficiaries/", views.LookBeneficiaries.as_view(), name='look_beneficiaries'),
                path("lookdonors/", views.LookDonors.as_view(), name='look_donors'),
                path('aliados/', InstitutionListView.as_view(), name='aliados'),
                path("lookInstitutios/", views.LookInstitutions.as_view(), name='look_institutions'),
                path("filtersemester/<int:id>/", views.FilterSemester.as_view(), name='filtersemester'),
                path("filterinstitution/<int:id>/", views.FilterInstitution.as_view(), name='filterinstitution'),
                path("filterprogram/<str:program_name>/", views.FilterProgram.as_view(), name='filterprogram'),
                path("filtercity/<str:city>/", views.FilterCity.as_view(), name='filtercity'),
                path("filtertype/<str:typeI>/", views.FilterTypeI.as_view(), name='filtertype'),
                path("searchIns",views.SrchView.as_view(),name='searchIns'),
                path("searchBen",views.SrchBenView.as_view(),name='searchBen'),
                path('filtervalue/<int:min_value>/<int:max_value>/', views.FilterInterval.as_view(), name='filtervalue'),
                path('showdetailsBen/<int:id>/', views.ShowDetailsBen.as_view(), name='showdetailsbeneficiary'),
                path('showdetailsIns/<int:id>/', views.ShowDetailsIns.as_view(), name='showdetailsinstitucion'),
                path('transactions/', TransactionListView.as_view(), name='transaction-list'),
                path('donations/', DonationsListView.as_view(), name='donationslist'),
                path('payments/<int:id>/', views.Payments.as_view(), name='payments'),
                path('paymentsBen/<int:id>/', views.PaymentsBen.as_view(), name='paymentsBen'),
                path('paymentpaypal/<int:id>/', views.PaymentsPaypal.as_view(), name='paymentpaypal'),
                path('paymentcard/<int:id>/', views.PaymentsCard.as_view(), name='paymentcard'),
                path('paymentpse/<int:id>/', views.PaymentsPse.as_view(), name='paymentpse'),
                path('pay1/<int:id>/', views.Pay1.as_view(), name='pay1'),
                path('pay2/<int:id>/', views.Pay2.as_view(), name='pay2'),
                path('pay3/<int:id>/', views.Pay3.as_view(), name='pay3'),
                path('donationIns/<int:id>/', views.DonationIns.as_view() , name='donationIns'),
                path('donationSch/<int:id>/', views.DonationSch.as_view() , name='donationSch'),
                path('typeSch/<int:id>/<int:x>/', views.TypeSch.as_view() , name='typeSch'),
                path('scholarships/', ScholarshipListView.as_view(), name='scholarships'),

                path('contact/', ContactView.as_view(), name='contact_view'),

                path("lookdonationsmade/", views.LookDonationHistory.as_view(), name="lookdonationsmade"),
               ]