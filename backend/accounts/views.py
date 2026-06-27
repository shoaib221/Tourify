



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from residence.models import *
from .serializers import *
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError


class Test(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            return Response( { 'message': 'Authentic User' }, status=status.HTTP_200_OK )
        else:
            return Response( { 'message': 'Please Authenticate' } , status=status.HTTP_200_OK )
    
    def post(self, request):
        if request.user.is_authenticated:
            request.data['message'] = 'Post authenticated'
            return Response( request.data, status=status.HTTP_200_OK )
        else:
            return Response( { 'message': 'Post unauth' } , status=status.HTTP_200_OK )
    
    def put(self, request):
        if request.user.is_authenticated:

            return Response( { 'message': ' Put authenticated ' }, status=status.HTTP_200_OK )
        else:
            return Response( { 'message': 'Put unauth' } , status=status.HTTP_200_OK )


###########################################  accounts  ###########################################



class MyRegister(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'message': 'Already Registered'
            }
            return Response( context , status=status.HTTP_200_OK)
        else:
            serializer = UserDetailSerializer()
            qs = Country.objects.all()
            country_serializer = CountrySerializer(qs, many=True)
            context = {
                'user_detail': serializer.data,
                'country': country_serializer.data
            }
            return Response(context , status=status.HTTP_200_OK )

    def post(self, request):

        if request.user.is_authenticated:
            context = {
                'message': 'Already Registered'
            }
            return Response( context , status=status.HTTP_200_OK)
        
        else:

            serializer = UserDetailSerializer(data=request.data)
            #print(request.data)
            #print(serializer.data)

            if serializer.is_valid():
                
                user_detail = UserDetail()
                user_detail.username = serializer.validated_data['mail']
                user_detail.country = serializer.validated_data['country']
                user_detail.nid = serializer.validated_data['nid']
                user_detail.mobile = serializer.validated_data['mobile']
                user_detail.mail = serializer.validated_data['mail']
                user_detail.password = make_password( serializer.validated_data['password'] )

                #print(serializer.validated_data)
                #print(serializer.data)
                #print(user_detail.password)

                try:
                    user_detail.full_clean()
                    user_detail.save()
                    context = {
                        'message': 'successfully registered',
                        'serializer': serializer.data
                    }
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except ValidationError as ve:
                    context = {
                        'errors': ve.message_dict,
                        'serializer': serializer.data
                    }
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                context={
                    'errors': serializer.errors,
                    'serializer': serializer.data
                }
                return Response(context , status=status.HTTP_400_BAD_REQUEST)
            

class MyLogin(APIView):

    def post(self, request):
        
        if request.user.is_authenticated:
            context = {
                'message': 'Already logged in'
            }
            return Response( context , status=status.HTTP_200_OK)
        
        else:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                mail = serializer.validated_data['mail']
                password = serializer.validated_data['password']
                user = UserDetail.objects.get(mail=mail)
                if user is None:
                    
                    context = {
                        'message': 'No such user, Regester',
                        'serializer': serializer.data
                    }
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
                
                elif check_password(password, user.password):
                    login(request, user)
                    context = {
                        'message': 'Successfully logged in',
                    }
                    return Response(context, status=status.HTTP_200_OK)

                else:
                    context = {
                        'message': 'Incorrect Password',
                        'serializer': serializer.data
                    }
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
            else:
                context = {
                    'errors': serializer.errors,
                    'serializer': serializer.data
                }
                return Response( context , status=status.HTTP_200_OK)


    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'message': 'Already logged in'
            }
            return Response( context , status=status.HTTP_200_OK)
        else:
            #print(request.data)
            #print(request.user)
            serializer = LoginSerializer()
            return Response(serializer.data, status=status.HTTP_200_OK)


class MyLogout(APIView):
        
        def get(self, request):

            if request.user.is_authenticated:
                logout(request)
                context = {
                    'message': 'Successfully logged out'
                }
                return Response(context, status=status.HTTP_200_OK)
            else:
                context = {
                    'message': 'Already logged out'
                }
                return Response(context, status=status.HTTP_200_OK)
            

class MyProfile(APIView):

    def get( self, request ):
        if request.user.is_authenticated:
            user_detail = UserDetail.objects.get(username=request.user.username)
            serializer = MyProfileSerializer(user_detail)
            context = {'user_detail': serializer.data}
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_200_OK)
        

class ShowProfileDetail(APIView):

    def get(self, request, user_id):

        if request.user.is_authenticated:
            user_detail = UserDetail.objects.get(id=user_id)
            if user_detail is None:
                return Response( { "message": "No such user" } ,status=status.HTTP_400_BAD_REQUEST)
            serializer = MyProfileSerializer(user_detail)
            context = {'user_detail': serializer.data}
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_200_OK)











# class Test(views.View):

#     def get(self, request):
#         if request.user.is_authenticated:   
              
#             return render(request, "test.html")
#         else:
#             return redirect(request, "test.html" )
        
#     def post(self, request):
#         if request.user.is_authenticated:        
#             return render(request, "test.html")
#         else:
#             return redirect(request, "test.html" )
        
#     def put(self, request):
#         if request.user.is_authenticated:        
#             return render(request, "test.html")
#         else:
#             return redirect(request, "test.html" )


# class MyHome(views.View):
#     template_name = "home.html"
    
#     def get(self, request):
#         if request.user.is_authenticated:
#             return render(request, self.template_name)
#         else:
#             return redirect('/accounts/login/')


# class MyRegister(views.View):
#     template_name = "register.html"
#     form_temp = CreateUserForm

#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('/accounts/home/')
#         else:
#             form = self.form_temp()
#             print("hello from my register get")
#             return render(request, "register.html", { "form": form })

#     def post(self, request):

#         form = self.form_temp(request.POST, request.FILES)
#         if request.user.is_authenticated:
#             return redirect('/accounts/home/')
#         else:
#             if form.is_valid() :
#                 username = form.cleaned_data['mail']
#                 password = form.cleaned_data['password']
#                 confirm_password = form.cleaned_data['confirm_password']
#                 mail = form.cleaned_data['mail']
#                 mobile = form.cleaned_data['mobile']
#                 nid = form.cleaned_data['nid']
#                 country = form.cleaned_data['country']

#                 if password != confirm_password:
#                     form.add_error("__all__", 'Passwords not matching')
#                 elif UserDetail.objects.filter(mail=mail).exists():
#                     form.add_error("mail", 'Email Address Taken')
#                 elif UserDetail.objects.filter(username=username).exists():
#                     form.add_error("username", 'Username Taken')
#                 elif UserDetail.objects.filter(mobile=mobile).exists():
#                     form.add_error("mobile", 'Mobile Numbet Taken')
#                 elif UserDetail.objects.filter(nid=nid).exists():
#                     form.add_error("nid", 'NID already taken')
#                 else:
#                     current_user_detail = UserDetail()
#                     current_user_detail.username = username
#                     current_user_detail.mail = mail
#                     current_user_detail.mobile = mobile
#                     current_user_detail.nid = nid
#                     current_user_detail.country = country
#                     current_user_detail.password = make_password( password )
#                     try:
#                         current_user_detail.full_clean()
#                         current_user_detail.save()
#                         login(request, current_user_detail )
#                         return redirect('/accounts/home/')
#                     except ValidationError as e:
#                         for k in e:
#                             form.add_error(k, e[k])
#                         return render(request, self.template_name, {'form': form })
                
#                 return render(request, self.template_name, {'form': form })
#             else:
#                 return render(request, self.template_name, {'form': form })
            


# class MyProfile(views.View):
#     template_name = 'profile.html'

#     def get(self, request):
#         if request.user.is_authenticated:
#             user_detail = UserDetail.objects.get( username=request.user.username )
#             context = {'user_detail': user_detail}
#             return render(request, self.template_name, context)
#         else:
#             messages.info(request, 'Log in first')
#             return redirect('/accounts/')
        
#     def post(self, request):
#         if request.user.is_authenticated:
#             user_detail = UserDetail.objects.get( username=request.user.username )
#             context = {'user_detail': user_detail}
#             return render(request, self.template_name, context)
#         else:
#             messages.info(request, 'Log in first')
#             return redirect('/accounts/')


# class MyLogin(views.View):
#     template_name = "login.html"
#     form_class = LoginForm

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('/accounts/home/')
#         else:
#             form = self.form_class(request.POST or None)
#             if form.is_valid():
#                 username = form.cleaned_data["username"]
#                 password = form.cleaned_data["password"]
#                 current_user = authenticate(request, username=username, password=password)
#                 # print(type(current_user))
#                 if current_user is None:
#                     form.add_error("__all__", 'Invalid username or password')
#                     return render(request, self.template_name, {"form": form})
#                 else:
#                     login(request, current_user)
#                     return redirect('/accounts/home/')
#             else:
#                 return render(request, self.template_name, {"form": form})

#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('/accounts/home/')
#         else:
#             form = self.form_class()
#             print("hello from my login get")
#             return render(request, "login.html", {"form": form})
        
# class ForgotPassword(views.View):
    
#     def get(self, request):
#         return render(request, 'forgot_password.html')
    
#     def post(self, request):
#         aha=0


# class MyLogout(views.View):
        
#         def get(self, request):

#             if request.user.is_authenticated:
#                 logout(request)
#                 return redirect('/accounts/')
#             else:
#                 return redirect('/accounts/')
            

# class ShowProfileDetail(views.View):
#     def get(self, request, user_id):
#         user_detail = UserDetail.objects.get(pk=user_id)
#         return render(request, "profile.html", { 'user_detail': user_detail})



# ############################ update profile ############################

# from .forms import UpdateMobileForm, UpdateMailForm, UpdateNameForm


# class ChangePassword(views.View):
#     template_name = 'change_password.html'
#     form_class = PasswordChangeForm

#     def get(self, request):
#         if request.user.is_authenticated:
#             user = request.user
#             form = self.form_class()
#             return render(request, self.template_name, {'form': form})
#         else:
#             messages.info(request, 'You must log in first')
#             return redirect('/accounts/')

#     def post(self, request):

#         if request.user.is_authenticated:
#             user = request.user
#             form = self.form_class(request.POST or None)

#             if form.is_valid():
#                 username = user.username
#                 password = form.cleaned_data['current_password']
#                 new_pass = form.cleaned_data['new_password']
#                 confirm_pass = form.cleaned_data['confirm_password']
#                 auth_user = authenticate(
#                     request, username=username, password=password)
#                 if auth_user is not None:
#                     if new_pass == confirm_pass:
#                         auth_user.set_password(new_pass)
#                         print('cppost')
#                         auth_user.save()
#                         login(request, auth_user)
#                         return redirect('/home/')
#                     else:
#                         messages.info(request, 'Passwords not matching')
#                         return redirect('/change_password/')
#                 else:
#                     messages.info(request, 'Permission denied')
#                     return redirect('/underground/')
#             else:
#                 return render(request, self.template_name, {'form': form})
#         else:
#             messages.info(request, 'You must log in first')
#             return redirect('/')


# from .forms import UpdateNameForm

# class UpdateName(views.View):
    

#     def get(self, request):
#         if request.user.is_authenticated:
#             form = UpdateNameForm()
#             return render(request, 'update_name.html', {'form': form})
#         else:
#             messages.info(request, 'You must log in first')
#             return redirect('/accounts/')
    
#     def post(self, request):

#         if request.user.is_authenticated:
#             form = UpdateNameForm(request.POST or None)
            
#             if form.is_valid():
#                 name = form.cleaned_data['name']
#                 user_detail = UserDetail.objects.get(username=request.user.username)
#                 user_detail.name = name
#                 user_detail.save()
#                 return redirect( "/accounts/my_profile/" )
#             else:
#                 return render(request, 'update_name.html', {'form': form})
            
#         else:
#             messages.info(request, 'You must log in first')
#             return redirect('/accounts/')
        
# from .forms import UpdateMailForm

# class UpdateEmail(views.View):
    

#     def get(self, request):
#         if request.user.is_authenticated:
#             form = UpdateMailForm()
#             return render(request, 'update_mail.html', {'form': form})
#         else:
#             messages.info(request, 'You must log in first')
#             return redirect('/accounts/')
    
#     def post(self, request):

#         if request.user.is_authenticated:
#             form = UpdateNameForm(request.POST or None)
            
#             if form.is_valid():
#                 mail = form.cleaned_data['mail']
#                 user_detail = UserDetail.objects.get(username=request.user.username)
#                 user_detail.mail = mail
#                 try:
#                     user_detail.save()
#                     return redirect( "/accounts/my_profile/" )
#                 except:
#                     form.add_error('mail', 'Email Address Taken')
#                     return render(request, 'update_mail.html', {'form': form})
#             else:
#                 return render(request, 'update_name.html', {'form': form})
            
#         else:
#             messages.info(request, 'You must log in first')
#             return redirect('/accounts/')

# from .forms import UpdateMobileForm



# class UpdateMobile(views.View):
    
#     def get(self, request):
#         if request.user.is_authenticated:
#             form = UpdateMobileForm()
#             return render(request, 'update_mobile.html', {'form': form})
#         else:
#             messages.info(request, 'You must log in first')
#             return redirect('/accounts/')
    
#     def post(self, request):

#         if request.user.is_authenticated:
#             form = UpdateMobileForm(request.POST or None)
            
#             if form.is_valid():
#                 mobile = form.cleaned_data['mobile']
#                 user_detail = UserDetail.objects.get(username=request.user.username)
#                 user_detail.mobile = mobile
#                 try:
#                     user_detail.save()
#                     return redirect( "/accounts/my_profile/" )
#                 except:
#                     form.add_error('mobile', 'Mobile Number Taken')
#                     return render(request, 'update_mobile.html', {'form': form})
#             else:
#                 return render(request, 'update_mobile.html', {'form': form})
            
#         else:
#             messages.info(request, 'You must log in first')
#             return redirect('/accounts/')




###################################### Orders ######################################




