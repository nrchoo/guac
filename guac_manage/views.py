from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from guac_manage.forms import SignUpForm,CompanyForm,PackageForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from guac_manage.models import Package,Company,Developer
global prices_dict
import stripe
# Create your views here.

@login_required
def dashboard(request):
    username = None
    if request.user.is_authenticated():
        username = request.user

    return render(request,'guac_manage/dashboard.html',{'username':username })


#@login_required
def home(request):
    return render(request, 'guac_manage/home.html', {})

def create_account(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form_company = CompanyForm(request.POST)

        if form.is_valid() and form_company.is_valid():
            form.save()
            #Create Company (Have to create form)
            company = form_company.save(commit=True)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            #Create Developer
            developer = Developer.objects.create(user = user, company = company)

            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        form_company = CompanyForm()

    return render(request, 'guac_manage/create_account.html', {'form':form,'form_company':form_company })

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            #raise forms.ValidationError("Passwords don't match")
            print("Invalid login details:",username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'guac_manage/login.html')

#@login_required
def shopping(request):

    prices_dict = {'BEGINNER': 49, "INTERMEDIATE": 79, "PROFESSIONAL":99}
    prices_dict = prices_dict
    if request.method == 'POST':
        radio_choice = request.POST.get("optradio")
        package = Package.objects.create(package_type = radio_choice)
        package.get_price()

        #Need to link Company to Package Purchase
        user = None
        if request.user.is_authenticated():
            user = request.user
            print("pk",user.pk)
            print('package',package)
            user.developer.company.package = package
            user.developer.company.save()
            print("IM HERE")
            return redirect('checkout')
            #User.objects.last().developer.company.package = Package.objects.last()
    else:
        pass

    return render(request,'guac_manage/shopping.html', {'prices_dict': prices_dict})


def checkout(request):
    print("TESTING CHECKOUT")
    print("method:",request.method)
    #print("stripe_token",request.POST.get('stripeToken'))
    
    if request.method == 'POST':
        print("Checking Out Post")
        stripe.api_key = "sk_test_5ajz1E03ivnBajB7ICzjaa8F"
        # Token is created using Stripe.js or Checkout!
        # Get the payment token submitted by the form:
        token = request.POST.get('stripeToken') # Using Flask
        print("Token:", token)

        # Charge the user's card:
        charge = stripe.Charge.create(
          amount=1000,
          currency="usd",
          description="Example charge",
          source=token,
        )
    else:
        pass


    return render(request,'guac_manage/checkout.html',{})
