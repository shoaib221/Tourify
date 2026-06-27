

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from residence.models import *
from .serializers import *
from accounts.serializers import *
from accounts.models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError



#######################################  house  #############################################

class MyHouse(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            qs = House.objects.filter( user_detail__username=request.user.username )
            serializer = HouseSerializer(qs, many=True)
            context = {
                'houses': serializer.data
            }

            return Response( context , status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_200_OK)
        

class AddHouse(APIView) :

    def get(self, request):
        if request.user.is_authenticated:
            serializer = HouseSerializer()

            user_detail = UserDetail.objects.get(username=request.user.username)
            cities = City.objects.filter( country = user_detail.country )
            cs = CitySerializer(cities, many=True)
            context = {
                'serializer': serializer.data,
                'cities': cs.data
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_200_OK)
    
    def post(self, request):
        if request.user.is_authenticated:
            serializer = HouseSerializer(data=request.data)

            if serializer.is_valid():
                
                user_detail = UserDetail.objects.get(username=request.user.username)

                house = House()
                house.user_detail = user_detail
                house.name = serializer.validated_data['name']
                house.address = serializer.validated_data['address']
                house.city = serializer.validated_data['city']
                house.description = serializer.validated_data['description']
                house.country = house.city.country


                try:
                    house.full_clean()
                    house.save()
                    context = {
                        'message': 'successfully created',
                        'serializer': serializer.data
                    }
                    return Response(context , status=status.HTTP_201_CREATED)
                except ValidationError as e:
                    context = {
                        'errors': e.message_dict,
                        'serializer': serializer.data
                    }
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                context = {
                    'errors': serializer.errors,
                    'serializer': serializer.data
                }
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_200_OK)



class HouseDetail(APIView):

    def get(self, request, house_id):

        if request.user.is_authenticated:
            try:
                house = House.objects.get(id=house_id)
            except:
                context = {
                    'message': 'No such house of this id',
                    'house_id': house_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            serializer = HouseSerializer(house)

            rooms = Room.objects.filter( house=house )

            rooms_data = []

            for room in rooms:
                rooms_data.append( room.id )

            context = {
                'house_id': house_id,
                'house': serializer.data,
                'rooms_id': rooms_data
            }

            house_bookings = Booking.objects.filter( house=house )

            house_srz = BookingSerializer(house_bookings, many=True)

            context['bookings']=house_srz.data

            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_200_OK)



#########################     Room          #########################################

class AddRoom(APIView):

    def get(self, request, house_id):

        if request.user.is_authenticated:
            

            user_detail = UserDetail.objects.get(username=request.user.username)
            try:
                house = House.objects.get( id=house_id )
            except:
                context = {
                    'message': 'No such house of this id',
                    'house_id': house_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            if house.user_detail != user_detail:
                context = {
                    'message': 'You are not the owner of this house',
                    'house_id': house_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            serializer = RoomSerializer()

            context = {
                'serializer': serializer.data,
            }

            return Response(context, status=status.HTTP_200_OK)

        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_200_OK)
        
    def post(self, request, house_id):

        if request.user.is_authenticated:
            

            user_detail = UserDetail.objects.get(username=request.user.username)
            try:
                house = House.objects.get( id=house_id )
            except:
                context = {
                    'message': 'No such house of this id',
                    'house_id': house_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            if house.user_detail != user_detail:
                context = {
                    'message': 'You are not the owner of this house',
                    'house_id': house_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            print(request.data)
            serializer = RoomSerializer( data=request.data )

            

            if serializer.is_valid():
                room = Room()
                room.name = serializer.validated_data['name']
                room.house = house
                room.beds = serializer.validated_data['beds']
                room.has_ac = serializer.validated_data['has_ac']
                room.price = serializer.validated_data['price']
                room.description = serializer.validated_data['description']
                
                try:
                    room.full_clean()
                    room.save()
                    context = {
                        'message': 'successfully created',
                        'serializer': serializer.data
                    }
                    return Response(context , status=status.HTTP_201_CREATED)
                except ValidationError as ve :
                    context = {
                        'errors': ve.message_dict,
                        'serializer': serializer.data
                    }
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
            else:
                context = {
                    'errors': serializer.errors,
                    'serializer': serializer.data
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)

        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_200_OK)


class RoomDetail(APIView):
    
    def get(self, request, room_id):
            
        if request.user.is_authenticated:
            try:
                room = Room.objects.get(id=room_id)
            except:
                context = {
                    'message': 'No such room of this id',
                    'room_id': room_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            room_serializer = RoomSerializer(room)

            unavails = RoomUnavailable.objects.filter( room=room )

            unavails_data = UnavailabilityDetailSerializer(unavails, many=True)

            room_bookings= RoomBooking.objects.filter( room=room )

            room_srz = RoomBookingSerializer(room_bookings, many=True)

            

            context = {
                'room': room_serializer.data,
                'unavails': unavails_data.data
            }

            if( room.house.user_detail.username == request.user.username ):
                context['room_bookings'] = room_srz.data

            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)



###########################   Unavailability   #########################################

class CreateUnavailability(APIView):
    
    def get(self, request, room_id):

        if request.user.is_authenticated:
            try:
                room = Room.objects.get(id=room_id)
            except:
                context = {
                    'message': 'No such room of this id',
                    'room_id': room_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            user_detail = UserDetail.objects.get(username=request.user.username)

            if( room.house.user_detail != user_detail ):
                context = {
                    'message': 'You are not the owner of this room',
                    'house_id': room_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)

            serializer = UnavailabilitySerializer()
            context = {
                'serializer': serializer.data
            }

            return Response(context, status=status.HTTP_200_OK) 
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
    def post( self, request, room_id ):
        if request.user.is_authenticated:
            try:
                room = Room.objects.get(id=room_id)
            except:
                context = {
                    'message': 'No such room of this id',
                    'room_id': room_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            user_detail = UserDetail.objects.get(username=request.user.username)

            if( room.house.user_detail != user_detail ):
                context = {
                    'message': 'You are not the owner of this room',
                    'house_id': room_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)

            serializer = UnavailabilitySerializer(data=request.data)

            if serializer.is_valid():
                unavail = RoomUnavailable()
                unavail.house = room.house
                unavail.room = room
                unavail.from_day = serializer.validated_data['from_day']
                unavail.to_day = serializer.validated_data['to_day']
                unavail.booked = False

                try:
                    unavail.full_clean()
                    unavail.save()
                    context = {
                        'message': 'successfully created',
                        'serializer': serializer.data
                    }
                    return Response(context , status=status.HTTP_201_CREATED)
                except ValidationError as ve :
                    context = {
                        'errors': ve.message_dict,
                        'serializer': serializer.data
                    }
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
            else:
                context = {
                    'errors': serializer.errors,
                    'serializer': serializer.data
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class DeleteUnavailability(APIView):
    
    def get(self, request, id):

        if request.user.is_authenticated:
            try:
                unavail = RoomUnavailable.objects.get(id=id)
            except:
                context = {
                    'message': 'No such unavailability of this id',
                    'id': id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            user_detail = UserDetail.objects.get(username=request.user.username)

            if( unavail.house.user_detail != user_detail ):
                context = {
                    'message': 'You are not the owner of this room',
                    'id': id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            if not unavail.booked:
                unavail.delete()
            
            context = {
                'message': 'success',
            }
            return Response(context, status=status.HTTP_200_OK) 
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


###############################   Search   ###########################################

class SearchRoom(APIView):
    
    def get(self, request):
            
        if request.user.is_authenticated:
            serializer = SearchRoomSerializer()
            context = {
                'serializer': serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        if request.user.is_authenticated:
            serializer = SearchRoomSerializer(data=request.data)
            if serializer.is_valid():
                city = serializer.validated_data['city']
                from_day = serializer.validated_data['from_day']
                to_day = serializer.validated_data['to_day']

                qs = RoomUnavailable.objects.all()
                qs = qs.filter(house__city=city)
                qs = qs.filter(from_day__lte=to_day, to_day__gte=from_day)

                unavail = set()
                for x in qs:
                    unavail.add(x.room.id)

                ase = Room.objects.all()
                ase = ase.filter(house__city=city)

                ans = []
                for x in ase:
                    if x.id not in unavail:
                        ans.append( x )
                
                rooms_serializer = RoomSerializer(ans, many=True)

                context = {
                    'rooms': rooms_serializer.data
                }
                return Response(context, status=status.HTTP_200_OK)
            else:
                context = {
                    'errors': serializer.errors,
                    'serializer': serializer.data
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)



##########################   cart   #############################################

class AddToCart(APIView):
    
    def get(self, request):
        if request.user.is_authenticated:
            serializer = AddCart()
            context = {
                'serializer': serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        if request.user.is_authenticated:
            serializer = AddCart(data=request.data)
            if serializer.is_valid():
                room_id = serializer.validated_data['room_id']
                room = Room.objects.get(id=room_id)
                user_detail = UserDetail.objects.get(username=request.user.username)
                cart = Cart()
                cart.user_detail = user_detail
                cart.room = room
                cart.house = room.house
                cart.book_from = serializer.validated_data['book_from']
                cart.book_to = serializer.validated_data['book_to']
                number_of_days = (cart.book_to - cart.book_from).days
                cart.price = room.price * number_of_days

                try:
                    cart.full_clean()
                    cart.save()
                    context = {
                        'message': 'successfully added to cart',
                        'serializer': serializer.data
                    }
                    return Response(context , status=status.HTTP_201_CREATED)
                except ValidationError as ve :
                    context = {
                        'errors': ve.message_dict,
                        'serializer': serializer.data
                    }
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
            else:
                context = {
                    'errors': serializer.errors,
                    'serializer': serializer.data
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class MyCart(APIView):
    
    def get(self, request):

        if request.user.is_authenticated:
            user_detail = UserDetail.objects.get(username=request.user.username)
            qs = Cart.objects.filter( user_detail=user_detail )
            serializer = CartSerializer(qs, many=True)
            context = {
                'carts': serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


###############################   Booking   ###########################################
import datetime

class BookRooms(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            user_detail = UserDetail.objects.get(username=request.user.username)
            qs = Cart.objects.filter( user_detail=user_detail )

            if( len(qs)<1 ):
                context = { 'message': 'Cart is empty' }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            
            houses = set()
            for x in qs:
                houses.add( x.house.id )

            if( len(houses)>1 ):
                context = { 'message': 'Cannot book rooms from different houses' }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            
            booking01 = Booking()
            booking01.guest = user_detail
            booking01.house = qs[0].house
            booking01.booking_time = datetime.datetime.now()
            booking01.total_price = 0

            rooms= []

            try:
                booking01.full_clean()
                booking01.save()

                for x in qs:
                    room_booking01 = RoomBooking( booking= booking01, room=x.room, start_date=x.book_from, end_date=x.book_to, price=x.price )
                    room_booking01.full_clean()
                    booking01.total_price += room_booking01.price
                    rooms.append( room_booking01 )
            except ValidationError as ve :
                context = {
                    'errors': ve.message_dict,
                }
                booking01.delete()
                return Response(context, status=status.HTTP_400_BAD_REQUEST)    
            
            booking01.save()
            for x in rooms:
                unavail = RoomUnavailable( room=x.room, house=x.room.house, from_day=x.start_date, to_day=x.end_date, booked=True )
                unavail.save()
                x.save()

            for x in qs:
                x.delete()

        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class HouseBookings(APIView):

    def get(self, request, house_id):
        if request.user.is_authenticated:
            
            house = House.objects.get(id=house_id)
            if house is None :
                context = {
                    'message': 'No such house of this id',
                    'house_id': house_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            user_detail = UserDetail.objects.get(username=request.user.username)

            if( house.user_detail != user_detail ):
                context = {
                    'message': 'You are not the owner of this house',
                    'house_id': house_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            qs = Booking.objects.filter( house=house )
            
            context = []

            for x in qs:
                row={}
                serializer = BookingSerializer(x)
                row['booking'] = serializer.data
                rooms = RoomBooking.objects.filter( booking=x )
                rooms_serializer = RoomBookingSerializer(rooms, many=True)
                row['room_bookings'] = rooms_serializer.data
                context.append( row )

            
            return Response(context, status=status.HTTP_200_OK) 
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)    


class RoomBookings(APIView):

    def get(self, request, room_id):
        if request.user.is_authenticated:
            
            room = Room.objects.get(id=room)
            if room is None :
                context = {
                    'message': 'No such house of this id',
                    'house_id': room_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            user_detail = UserDetail.objects.get(username=request.user.username)

            if( room.house.user_detail != user_detail ):
                context = {
                    'message': 'You are not the owner of this house',
                    'house_id': room_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            qs = Booking.objects.filter( house=room.house )
            
            context = []

            for x in qs:
                row={}
                serializer = BookingSerializer(x)
                row['booking'] = serializer.data
                rooms = RoomBooking.objects.filter( booking=x )
                rooms_serializer = RoomBookingSerializer(rooms, many=True)
                row['room_bookings'] = rooms_serializer.data
                context.append( row )

            
            return Response(context, status=status.HTTP_200_OK) 
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        


class MyBookings(APIView):



    def get(self, request):
        if request.user.is_authenticated:
            
            user_detail = UserDetail.objects.get(username=request.user.username)
            qs = Booking.objects.filter( guest=user_detail )
            
            context = {}

            booking_srz = BookingSerializer(qs, many=True)

            context[ 'bookings' ]=booking_srz.data
            
            return Response(context, status=status.HTTP_200_OK) 
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


		
class BookingDetail(APIView):

    def get(self, request, booking_id):
        if request.user.is_authenticated:
            
            user_detail = UserDetail.objects.get(username=request.user.username)
            try:
                booking = Booking.objects.get( id=booking_id )
            except:
                context = {
                    'message': 'No such booking of this id',
                    'booking_id': booking_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            if booking.guest != user_detail or booking.house.user_detail != user_detail :
                context = {
                    'message': 'You are associated with this booking',
                    'booking_id': booking_id
                }
                return Response( context ,status=status.HTTP_400_BAD_REQUEST)
            
            context = {}

            booking_srz = BookingSerializer(booking)

            context[ 'booking' ]=booking_srz.data

            rooms = RoomBooking.objects.filter( booking=booking )

            rooms_srz = RoomBookingSerializer(rooms, many=True)

            context[ 'room_bookings' ]=rooms_srz.data
            
            return Response(context, status=status.HTTP_200_OK) 
        else:
            context = {
                'message': 'Log in first'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)






# from ctypes import sizeof
# from datetime import date
# import datetime
# from pyexpat.errors import messages
# from django.forms import ValidationError
# from django.shortcuts import render, redirect
# from django import views
# from .models import *
# from .forms import HouseForm, RoomForm
# from accounts.models import UserDetail


# ##########################################      House     #####################################################


# class MyHouse(views.View):
# 	template_name = 'my_house.html'
	
# 	def get(self, request):
# 		return render(request, self.template_name, {})

# 		if request.user.is_authenticated:
# 			qs = House.objects.filter( user_detail__username=request.user.username )
# 			context = { 'qs': qs }
# 			return render(request, self.template_name, context)
# 		else:
# 			messages.info(request, 'Log in First')
# 			return redirect('/accounts/')


# class AddHouse(views.View):
# 	form_class = HouseForm
# 	template_name = 'add_house.html'
	
# 	def get(self, request):
# 		if request.user.is_authenticated:
# 			form = self.form_class()
# 			return render(request, self.template_name, {'form': form})
# 		else:
# 			return redirect("/accounts/login/")
	
# 	def post(self, request):
# 		if request.user.is_authenticated:
# 			form = self.form_class(request.POST, request.FILES)
# 			if form.is_valid():
# 				ob = form.save(commit=False)
# 				ob.user_detail = UserDetail.objects.get(username=request.user.username)
# 				ob.country = ob.city.country
# 				try:
# 					ob.save()
# 					return redirect( "/residence/my_house/" )
# 				except ValidationError as e:
# 					for kk in e.message_dict:
# 						form.add_error(kk, e.message_dict[kk])
# 					return render(request, self.template_name, {'form': form})
# 			else:
# 				return render(request, self.template_name, {'form': form})
# 		else:
# 			return redirect("/accounts/")


# class HouseDetail(views.View):
# 	template_name = 'house_detail.html'
	
# 	def get(self, request, id):
# 		house = House.objects.get(id=id)
# 		rooms = Room.objects.filter(house_id=id)
# 		orders = Booking.objects.none()
# 		if request.user.is_authenticated and house.user_detail.username == request.user.username:
# 			orders = Booking.objects.filter(house_id=house)
# 		print(id)
# 		print(house.address)
# 		context = {'house': house, 'rooms': rooms, 'orders': orders }
# 		return render(request, self.template_name, context  )


# ##################################       Rooms       ##############################################################


# class AddRoom(views.View):
# 	template_name = 'add_room.html'
# 	form_class = RoomForm
	
# 	def get(self, request, id):
# 		if request.user.is_authenticated:
# 			house = House.objects.get(id=id)
# 			if house.user_detail.username == request.user.username:
# 				form = self.form_class()
# 				return render(request, self.template_name, {'form': form})
# 			else:
# 				messages.info(request, 'Permission denied')
# 				redirect('/accounts/')
# 		else:
# 			messages.info(request, 'Log in First')
# 			return redirect('/accounts/')
	
# 	def post(self, request, id):
# 		if request.user.is_authenticated:
# 			house = House.objects.get(id=id)
# 			if house.user_detail.username == request.user.username:
# 				form = self.form_class(request.POST, request.FILES)
# 				if form.is_valid():
# 					ob = form.save(commit=False)
# 					ob.house = house
# 					try:
# 						ob.full_clean()
# 						ob.save()
# 						return redirect('/residence/house/{}/'.format(house.id))
# 					except ValidationError as ve:
# 						for kk in ve.message_dict:
# 							form.add_error(kk, ve.message_dict[kk])
# 						return render(request, self.template_name, {'form': form})
# 				else:
# 					messages.info('Invalid Credentials')
# 					return render(request, self.template_name, {'form': form})
# 			else:
# 				messages.info(request, 'Permission denied')
# 				return redirect('/accounts/')
# 		else:
# 			messages.info(request, 'Log in First')
# 			return redirect('/accounts/')


# class RoomDetail(views.View):
# 	template_name = 'room_detail.html'
	
# 	def get(self, request, id):

# 		if request.user.is_authenticated:
# 			print("room_detail")
# 			room = Room.objects.get(id=id)
# 			unavail = RoomUnavailable.objects.filter(room=room, booked=False).order_by("from_day")
# 			bookings =  RoomBooking.objects.filter(room_id=id)
# 			qs = []
# 			for x in bookings:
# 				qs.append(x.booking)

# 			print( len( bookings ) )

# 			context = {'room': room, 'unavails': unavail, 'bookings': qs }
# 			return render(request, self.template_name, context )
# 		else:
# 			request.message.info('Log in First')
# 			return redirect('/accounts/')

		
# ############################################    Availability        ################################################
# from . import forms
# from . import pre_view

# class CreateUnavailability(views.View):

# 	template_name = "create_availability.html"
# 	form_class = forms.CreateUnavaiabilityForm
	
# 	def get(self, request, room_id):
		
# 		if request.user.is_authenticated:
# 			room = Room.objects.get(id=room_id)
# 			if room.house.user_detail.username == request.user.username:
# 				form = self.form_class()
# 				return render(request, self.template_name, {'form': form, "space": room })
# 			else:
# 				return redirect("/accounts/")
# 		else:
# 			return redirect('/accounts/')
	

# 	def post(self, request, room_id):
		
# 		if request.user.is_authenticated:
# 			room = Room.objects.get(id=room_id)
# 			if room.house.user_detail.username == request.user.username:
# 				form = self.form_class(request.POST or None)
# 				if form.is_valid():
# 					from_date, to_date = pre_view.load_date_from_DateForm(form)
# 					new_unavail = RoomUnavailable( room=room, from_day=from_date, to_day=to_date, house=room.house, booked=False )  
# 					try:
# 						new_unavail.full_clean()
# 						new_unavail.save()
# 						print("created unavail successfully")
# 						return redirect("/residence/room/{}/".format(room.id))
# 					except ValidationError as e :
# 						for kk in e.message_dict:
# 							form.add_error(kk, e.message_dict[kk])
# 						return render(request, self.template_name, {'form': form, "space": room })
# 				else:
# 					return render(request, self.template_name, {'form': form, "space": room })
# 			else:
# 				messages.info(request, 'Permission denied')
# 				return redirect("/accounts/")
# 		else:
# 			messages.info(request, 'Log in First')
# 			return redirect('/accounts/')

# from .models import RoomUnavailable


# class DeleteUnavailability(views.View):
	
	
# 	def get(self, request, id):
# 		if request.user.is_authenticated:
# 			unavail = RoomUnavailable.objects.get(id=id)
# 			if unavail.house.user_detail.username == request.user.username:
# 				unavail.delete()
# 				return redirect("/residence/room/{}/".format(unavail.room.id))
# 			else:
# 				messages.info(request, 'Permission denied')
# 				return redirect('/accounts/')
# 		else:
# 			messages.info(request, 'Log in First')
# 			return redirect('/accounts/')
		



# ###########################################   Search #######################################

# from .forms import RoomSearchForm
# from accounts.models import Country, City

# class SearchRoom(views.View):

# 	form_class = forms.RoomSearchForm

# 	def get(self, request):
# 		if request.user.is_authenticated:
# 			context = {
# 				'form': self.form_class(),
# 			}
# 			return render(request, 'search_room.html', context  )
# 		else:
# 			messages.info(request, 'You must log in first')
# 			return redirect('/accounts/')
		
# 	def post( self, request ):

# 		if request.user.is_authenticated:
# 			form = self.form_class(request.POST)

# 			if form.is_valid():
# 				from_date, to_date = pre_view.load_date_from_DateForm(form)
# 				city_id = form.cleaned_data['city']


# 				qs = RoomUnavailable.objects.all()
# 				qs = qs.filter(house__city_id=city_id)
# 				qs = qs.filter(from_day__lte=to_date, to_day__gte=from_date)

# 				unavail = set()
# 				for x in qs:
# 					unavail.add(x.room.id)
				
# 				ase = Room.objects.all()
# 				ase = ase.filter(house__city_id=city_id)

# 				ans = []

# 				for x in ase:
# 					if x.id not in unavail:
# 						ans.append( x )
				
# 				return render(request, 'search_room.html', {'form': form, 'qs': ans})
# 			else:
# 				return render(request, 'search_room.html', {'form': form})
# 		else:
# 			messages.info(request, 'You must log in first')
# 			return redirect('/accounts/')
		
# from .models import Cart


# class AddToCart(views.View):

# 	def get(self, request, room_id):
# 		if request.user.is_authenticated:
# 			room = Room.objects.get(id=room_id)		
# 			user_detail = UserDetail.objects.get(username=request.user.username)
# 			start_date = request.GET.get('start_date')
# 			end_date = request.GET.get('end_date')
# 			cart = Cart()

# 			cart = Cart()
# 			cart.user_detail = user_detail
# 			cart.room = room
# 			cart.house = room.house
# 			cart.book_from = start_date
# 			cart.book_to = end_date
# 			number_of_days = (cart.book_to - cart.book_from).days
# 			cart.price_per_day = room.price * number_of_days
# 			try:
# 				cart.full_clean()
# 				cart.save()
# 				print("added to cart")
# 				return render(request, 'message.html', {'message': 'Added to cart'} )
# 			except ValidationError as ve:
# 				context = {
# 					'message': 'Failed to add to cart',
# 					'errors': ve.message_dict
# 				}
# 				return render(request, 'message.html', context )
# 		else:
# 			messages.info(request, 'You must log in first')
# 			return redirect('/accounts/')


# class MyCart(views.View):

# 	template_name = "cart.html"
	
# 	def get(self, request):
# 		if request.user.is_authenticated:
# 			qs= Cart.objects.filter(user_detail__username=request.user.username)
# 			return render(request, self.template_name, {'qs': qs}	 )
# 		else:
# 			messages.info(request, 'You must log in first')
# 			return redirect('/accounts/')

# class BookRooms(views.View):
# 	template_name = "message.html"

# 	def get(self, request):
# 		if request.user.is_authenticated:
# 			user_detail = UserDetail.objects.get(username=request.user.username)
# 			qs = Cart.objects.filter(user_detail=user_detail)

# 			if( len(qs)<1 ):
# 				context = { 'message': 'Cart is empty' }
# 				return render(request, self.template_name, context )
			
# 			houses = set()
# 			for x in qs:
# 				houses.add(x.house.id)

# 			if (len(houses) > 1):
# 				context = { 'message': 'All rooms must be from same house' }
# 				return render(request, self.template_name, context )
			
# 			booking01 = Booking()
# 			booking01.guest = user_detail
# 			booking01.house = qs[0].house
# 			booking01.total_price = 0
# 			booking01.booking_time = datetime.datetime.now()

# 			rooms = []
# 			try:
# 				booking01.full_clean()
# 				booking01.save()
				
# 				for x in qs:
# 					room_booking = RoomBooking()
# 					room_booking.booking = booking01
# 					room_booking.room = x.room
# 					room_booking.price = x.price
# 					room_booking.start_date = x.book_from
# 					room_booking.end_date = x.book_to

# 					room_booking.full_clean()
# 					booking01.total_price += room_booking.price
# 					rooms.append( room_booking )

# 			except ValidationError as ve:
# 				context = {
# 					'message': 'Failed to create booking',
# 					'errors': ve.message_dict
# 				}
# 				booking01.delete()
# 				return render(request, self.template_name, context )

# 			booking01.save()
# 			for x in rooms:
# 				x.save()
# 				unavail = RoomUnavailable( room=x.room, house=x.room.house, from_day=x.start_date, to_day=x.end_date, booked=True )
# 				unavail.save()
			
# 			for x in qs:
# 				x.delete()
            

# ######################################   RoomBookings    ####################################


# class MyBookings(views.View):
# 	template_name = "my_booking.html"
	
# 	def get(self, request):
# 		if request.user.is_authenticated:
# 			bookings = Booking.objects.filter(guest__username=request.user.username).order_by("-booking_time")
# 			return render(request, self.template_name, {"orders": bookings})
# 		else:
# 			messages.info(request, 'You must log in first')
# 			return redirect("/accounts/")



# class BookingDetail(views.View):

# 	template_name = "booking_detail.html"

# 	def get(self, request, id):
# 		if request.user.is_authenticated:
# 			booking = Booking.objects.get(id=id)
# 			if booking.guest.username == request.user.username or booking.house.user_detail.username == request.user.username :
# 				qs = RoomBooking.objects.filter(booking_id=id)
# 				rooms = []
# 				for x in qs:
# 					rooms.append(x.room)
# 				return render(request, self.template_name, { "booking": booking, "rooms": rooms })
# 			else:
# 				return redirect("/accounts/")
# 		else:
# 			return redirect("/login_required/")
		





		
