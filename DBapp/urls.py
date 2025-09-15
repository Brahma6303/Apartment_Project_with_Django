from django.urls import path

from . import views

urlpatterns = [
    
    #path('add/',views.add_new_flat), # function based views
    path('add/',views.FlatView.as_view()), # class based views
    path('addowner/',views.add_new_owner),
    path('flat-sucess/<str:block_name>/<str:flat_num>',views.FlatSuccessView.as_view()),#dynamic html page Templateview(redircting scenario
    path('viewall/',views.FlatListView.as_view()), #TemplateView or ListView
    path('owners/',views.OwnerListView.as_view()),# ListView the all owners
    path('address/',views.AddressListView.as_view()),
    path('view/<int:pk>',views.FlatDetailView.as_view()), #TemplateView or DetailView
    path('addAddress/',views.add_new_address),
    path('updateAddress/<int:addr_id>/',views.update_address)
]