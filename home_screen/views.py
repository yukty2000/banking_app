from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView
from .models import Transfer
from user.models import Profile
from django.contrib import messages

# Create your views here.


def home(request):
	context = {
		'title' : 'Banking App',
	}
	return render(request,'home_screen/home.html',context);

def viewList(request):
	context = {
		'title' : 'Customers List',
		'customers' : User.objects.all(),
	}
	return render(request,'home_screen/viewList.html',context);


class CustomerListView(ListView):
	model = User
	template_name = 'home_screen/viewList.html'
	context_object_name = 'customers'

class CustomerDetailView(DetailView):
	model = User
	template_name = 'home_screen/user_detail.html'

def transfer(request,pk):
	sender = User.objects.filter(id=pk).first()

	context = {
		'title' : 'Transfer money',
		'customers' : User.objects.all(),
		'amount_list' : [n for n in range(5000,min(45000,int(sender.profile.balance)),5000)],
		'current_user' : sender ,
	}
	if(request.POST):
		#name = request.POST.get("receiver","")
		#first_name = name[0:name.find(' ')+1]
		receiver = User.objects.filter(id=request.POST.get("receiver","")).first()
		amount = request.POST.get("amount","")
		amount = int(amount)
		transfer_obj = Transfer(amount=amount,sender=sender,receiver=receiver)
		Profile.objects.filter(user_id=sender.id).update(balance=sender.profile.balance-amount)
		Profile.objects.filter(user_id=receiver.id).update(balance=receiver.profile.balance+amount)
		transfer_obj.save()
		messages.success(request,f'Amount Rs.{amount} transferred from {sender.get_full_name()} to {receiver.get_full_name()}')

		return redirect('view-list')

	return render(request,'home_screen/transfer.html',context);
