from django.shortcuts import render,HttpResponseRedirect
from .models import Flat,Owner,Address
from .forms import NewOwnerForm,NewAdreessModelForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView
from rest_framework.views import APIView
from .serializers import FlatSerializer,OwnerSerializer,AddressSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.
# #manual form validations 
# def add_new_flat(request):
#     if request.method=='POST':
#         block_name=request.POST['block_name']
#         flat_num=request.POST['flatnum']
#         #Manual validations of forms
#         if block_name!="" and flat_num!="":
#             if not  block_name in ['A','B','C','D','F']:
#                 return render(request,'flat/new_flat.html',{'error':True,'error_message':"Block Name should be A,B,C,D or F"})
#             else:
#                 Flat.objects.create(block_name=block_name,flat_num=flat_num,br_count=3,status=False)
#                 return render(request,'flat/new_flat_sucess.html',{'blk_name':block_name,'flt_no':flat_num})
#         if block_name == "":
#             return render(request,'flat/new_flat.html',{'error':True,'error_message':"Please fill Block Name filed"})
#         elif flat_num == "":
#             return render(request,'flat/new_flat.html',{'error':True,'error_message':"Please fill Flat Number filed"})

#     else:
#         return render(request,'flat/new_flat.html',{'error':False,'error_message':""})


# class based views - CreateView creating new flat
class FlatCreateView(CreateView):
    model=Flat
    fields='__all__'
    template_name='flat/add_new_flat.html' # default form is (variable name)
    success_url='/flats/flat_add_sucess/'

class FlatAddSuccessView(TemplateView):
    template_name='flat/flat_add_sucess.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['msg']="New Flat Added Successfully"
        return context

#class based views -View
class FlatView(View):
    def get(self,request):
        return render(request,'flat/new_flat.html',{'error':False,'error_message':""})
    
    
    def post(self,request):
        if request.method=='POST':
         block_name=request.POST['block_name']
        flat_num=request.POST['flatnum']
        #Manual validations of forms
        if block_name!="" and flat_num!="":
            if not  block_name in ['A','B','C','D','F']:
                return render(request,'flat/new_flat.html',{'error':True,'error_message':"Block Name should be A,B,C,D or F"})
            else:
                Flat.objects.create(block_name=block_name,flat_num=flat_num,br_count=3,status=False)
                #return render(request,'flat/new_flat_sucess.html',{'blk_name':block_name,'flt_no':flat_num})
                return HttpResponseRedirect('/flats/flat-sucess/' + block_name + '/'+ flat_num) #http://127.0.0.1:8000/flats/flat-sucess/
                #/flats/flat-sucess/C/303
               # http://127.0.0.1:8000/flats/flat-sucess/C/303
        if block_name == "":
            return render(request,'flat/new_flat.html',{'error':True,'error_message':"Please fill Block Name filed"})
        elif flat_num == "":
            return render(request,'flat/new_flat.html',{'error':True,'error_message':"Please fill Flat Number filed"})



    
#Django Forms
def add_new_owner(request):
    if request.method=='POST':
        #recieve the value from the filled form
        filled_form=NewOwnerForm(request.POST)
        #create an entry in owner table
        if filled_form.is_valid():
            Owner.objects.create(first_name=request.POST['f_name'],last_name=request.POST['l_name'],mobile=request.POST['mobile'],email=request.POST['email'])
            #send same sucess response to client
            return render(request,'flat/new_owner_sucess.html',{'first_name':request.POST['f_name'],'last_name':request.POST['l_name']})
        else:
            empty_form=NewOwnerForm()
            return render(request,'flat/new_owner.html',{'owner_form':empty_form})
    else:
        # send the some empty form(Not Html,should be Django Form) to client to create new owner
        new_owner_form=NewOwnerForm()
        return render(request,'flat/new_owner.html',{'owner_form':new_owner_form})
    
#class based views - TemplateView-Redircting Scenario
class FlatSuccessView(TemplateView):
    template_name='flat/new_flat_sucess.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['blk_name']=kwargs['block_name']
        context['flt_no']=kwargs['flat_num']
        return context
    

#class based views -TemplateView or ListView -List of Flats
class FlatListView(TemplateView):
    template_name='flat/flat_list.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['all_flats']=Flat.objects.all()

        return context

# class based views - APIView -List of Flats in JSON content
class FlatListReactView(APIView):
    
    def get(self,request,flat_id):
        serialized_flat=FlatSerializer()
        try:
            some_flat=Flat.objects.get(id=flat_id)
            serialized_flat=FlatSerializer(some_flat)
            return Response(serialized_flat.data)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,flat_id):
        serialzed_flat=FlatSerializer(data=request.data)
        if serialzed_flat.is_valid(raise_exception=True):
            serialzed_flat.save()
            return Response(serialzed_flat.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialzed_flat.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,flat_id):
        some_flat=Flat.objects.get(id=flat_id)
        serialized_flat=FlatSerializer(some_flat,data=request.data)
        if serialized_flat.is_valid():
            serialized_flat.save()
            return Response(serialized_flat.data,status=status.HTTP_200_OK)
        else:
            return Response(serialized_flat.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,flat_id):
        some_flat=Flat.objects.get(id=flat_id)
        some_flat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#class based views -TemplateView or DetailView -Details of a Flat
class FlatDetailView(TemplateView):
    template_name='flat/flat_details.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #print(kwargs) #o/p:pk
        pk=kwargs['pk']
        res=Flat.objects.filter(id=pk)
        if len(res)>0:
            context['flat_info']=res[0]
        else:
            context['flat_info']='No Flat Found'
        return context
    

# class based views -ListView -List of Owners
class OwnerListView(ListView):
    template_name='flat/owners_list.html'
    model=Owner
    context_object_name='all_owners'

    def get_queryset(self):
        base_results=super().get_queryset()
        #base_result=base_results.filter(address=None)
        base_results=base_results.exclude(address=None) # address != None
        return base_results

class OwnerReactListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Owner.objects.all()
    serializer_class=OwnerSerializer

    def get(self,request,*pargs,**kwargs):
        return self.list(request,*pargs,**kwargs)
    
    def post(self,request,*pargs,**kwargs):
        return self.create(request,*pargs,**kwargs)

class AddressListView(ListView):
    template_name='flat/all_address.html'
    model=Address
    context_object_name='all_address'

# Generic APIView for all addresses in JSON content
class AddressReactListView(generics.ListCreateAPIView):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer

class OwnerDetailView(DetailView):
    template_name='flat/owner_details.html'  # default object or owner (variable name)
    model=Owner

# class OwnerReactView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Owner.objects.all()
#     serializer_class=OwnerSerializer
#     lookup_field='pk'

#     def get(self,request,pk, *pargs,**kwargs):
#         return self.retrieve(request,*pargs,**kwargs)
    
#     def put(self,request,pk ,*pargs,**kwargs):
#         return self.update(request,*pargs,**kwargs)
    
#     def delete(self,request,pk ,*pargs,**kwargs):
#         return self.destroy(request,*pargs,**kwargs)

#viewSet for Owner
class OwnerViewsetView(viewsets.ViewSet):
    def list(self,request):
        owners=Owner.objects.all()
        serialized_owner=OwnerSerializer(owners,many=True)
        return Response(serialized_owner.data)
    
    def create(self,request):
        serialized_owner=OwnerSerializer(data=request.data)
        if serialized_owner.is_valid():
            serialized_owner.save()
            return Response(serialized_owner.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_owner.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request,pk):
        owner=Owner.objects.get(id=pk)
        serialized_owner=OwnerSerializer(owner)
        return Response(serialized_owner.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk):
        some_owner=Owner.objects.get(id=pk)
        serialized_owner=OwnerSerializer(some_owner,data=request.data)
        if serialized_owner.is_valid():
            serialized_owner.save()
            return Response(serialized_owner.data,status=status.HTTP_200_OK)
        else:
            return Response(serialized_owner.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk):
        some_owner=Owner.objects.get(id=pk)
        some_owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#model Forms
def add_new_address(request):
    if request.method=='POST':
        filled_form=NewAdreessModelForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return render(request,'flat/new_address_sucess.html')
    else:
        new_address_form=NewAdreessModelForm()
        return render(request,'flat/new_address.html',{'address_form':new_address_form})

# class based view - FormView for creating new address
class AddressFormView(FormView):
    #Html form
    #Django Form
    #Model Form
    form_class=NewAdreessModelForm
    template_name='flat/add_address.html'  # default form is (variable name)
    success_url='/flats/new-address-sucess/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class AddressSuccessView(TemplateView):
    template_name='flat/address_sucess.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['msg']="New Address Added Successfully"
        return context
    
class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer
    lookup_field='id'  

#update address in Model Forms
def update_address(request,addr_id):
    if request.method=='POST':
        existing_address=Address.objects.get(id=addr_id)
        filled_form=NewAdreessModelForm(request.POST,instance=existing_address)
        if filled_form.is_valid():
            filled_form.save()
            return render(request,'flat/update_address_sucess.html')
    else:
        existing_address=Address.objects.get(id=addr_id)
        model_form_for_existing_address=NewAdreessModelForm(instance=existing_address)
        return render(request,'flat/update_address.html',{'my_form':model_form_for_existing_address})
