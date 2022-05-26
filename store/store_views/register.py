from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Register(View):
    def get(self, request):
        return render(request,'register.html')

    def post(self, request):
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            contact = request.POST.get('contact')
            email = request.POST.get('email')
            password = request.POST.get('password')
            # Value after error fill old data
            value ={
                'first_name':first_name,
                'last_name':last_name,
                'contact':contact,
                'email':email,
            }
            customer = Customer(first_name=first_name, last_name=last_name, contact=contact, email=email, password=password)
            # Form validate
            error_massage = None
            if (not first_name):
                error_massage = "First Nmae Required !!"
            elif len(first_name) <4:
                error_massage = "First Name Must be 4 char long or more !!"
            elif not last_name:
                error_massage = "Last Name Required !!"
            elif len(last_name) <4:
                error_massage = "First Name Must be 4 char long or more !!"
            elif not contact:
                error_massage = "contact Name Required !!"
            elif len(contact) <10:
                error_massage = "contact Number Must be 10 char Long !!"
            elif len(password) <6:
                error_massage = "Password Must be 6 Long !!"
            elif len(email) <5:
                error_massage = "Email Must be 5 char Long !!"
            elif customer.is_Exists():
                error_massage = "Email Addresh Allready Registered.."
            # End validate
            # Saving
            if not error_massage:
                customer.password = make_password(customer.password)
                customer.register()
                return redirect('homepage')
            else:
                data={
                    'error':error_massage,
                    'values':value
                }
                return render(request,'register.html', data)

        return render(request,'register.html')
