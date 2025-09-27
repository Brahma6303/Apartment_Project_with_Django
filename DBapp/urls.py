from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
#router.register('owners',views.OwnerViewsetView,basename='all_owners')
router.register('owners',views.OwnerGenericViewsetView,basename='all_owners')

addr_router=DefaultRouter()
addr_router.register('addresses',views.AddressModelViewsetView,basename='all_addresses')

urlpatterns = [
    
    #path('add/',views.add_new_flat), # function based views
    path('add/',views.FlatView.as_view()), # class based views
    path('new/',views.FlatCreateView.as_view()), #class based view - CreateView
    path('flat_add_sucess/',views.FlatAddSuccessView.as_view()),
    path('addowner/',views.add_new_owner),
    path('flat-sucess/<str:block_name>/<str:flat_num>',views.FlatSuccessView.as_view()),#dynamic html page Templateview(redircting scenario
    #path('viewall/',views.FlatListView.as_view()), #TemplateView or ListView
    path('get/<str:flat_id>/',views.FlatListReactView.as_view()),#APIView
   # path('owners/',views.OwnerListView.as_view()),# ListView the all owners
    #path('owners/',views.OwnerReactListView.as_view()),# Mixins the all owners in JSON content
    #path('owners/<int:pk>/',views.OwnerReactView.as_view()),# Retrieve mixin the owner details in JSON content
    #path('owners/<int:pk>',views.OwnerDetailView.as_view()),# DetailView the owner details
    #path('addresses/',views.AddressListView.as_view()),
    path('view/<int:pk>',views.FlatDetailView.as_view()), #TemplateView or DetailView
    #path('addresses/',views.AddressReactListView.as_view()), # Generic APIView for all addresses in JSON content,
    #path('addresses/<int:id>/',views.AddressDetailView.as_view()), # Generic APIView for single address in JSON content
    path('address/new/',views.AddressFormView.as_view()), #class based view - FormView for creating new address
    path('new-address-sucess/',views.AddressSuccessView.as_view()), # TempalteView redircting to FormView
    path('updateAddress/<int:addr_id>/',views.update_address),

    path('',include(router.urls)),
    path('',include(addr_router.urls)),
]