

from django.urls import path, include
from . import views

urlpatterns = [

    path("my_house/", views.MyHouse.as_view() ),
    path("add_house/", views.AddHouse.as_view() ),
    path("house/<int:house_id>/", views.HouseDetail.as_view() ),
    path("add_room/house/<int:house_id>/", views.AddRoom.as_view() ),
    path("room/<int:room_id>/", views.RoomDetail.as_view() ),

    path("create_unavail/room/<int:room_id>/", views.CreateUnavailability.as_view() ),
    path("del_unavail/<int:id>/", views.DeleteUnavailability.as_view() ),

    path("search_vacancy/", views.SearchRoom.as_view() ),
    path("my_cart/", views.MyCart.as_view() ),
    path("add_to_cart/", views.AddToCart.as_view() ),
    path("book/", views.BookRooms.as_view() ),

    path("bookings/house/<int:house_id>/", views.HouseBookings.as_view() ),
    path("bookings/room/<int:room_id>/", views.RoomBookings.as_view() ),
    path("my_bookings/", views.MyBookings.as_view() ),
    path( "booking_detail/<int:booking_id>/", views.BookingDetail.as_view() ),
    
    # path( 'my_house/', views.MyHouse.as_view(), name='my residence'),
    # path( 'add_house/', views.AddHouse.as_view(), name='add residence'),
    # path( 'house/<int:id>/', views.HouseDetail.as_view(), name='residence detail'),
    # path( 'house/<int:id>/addroom/', views.AddRoom.as_view() , name='add room'),
    # path( 'room/<int:id>/', views.RoomDetail.as_view() , name='room detail'),
    # path( 'order/<int:id>/', views.BookingDetail.as_view() , name='order detail'),
    # path( 'room/<int:room_id>/create_unavail/', views.CreateUnavailability.as_view(), name='create room availability'),
    # path( 'del_unavail/<int:id>/', views.DeleteUnavailability.as_view(), name='room unavailabilities'),
    # path( 'search_vacancy/', views.SearchRoom.as_view(), name='search room'),
    # path( 'add_to_cart/<int:room_id>/', views.AddToCart.as_view(), name='search room detail'),
    # path( 'go_to_cart/', views.MyCart.as_view(), name='cart'),
    # path( 'book/', views.BookRooms.as_view(), name='book'),
    # path( 'my_booking/', views.MyBookings.as_view(), name='my booking'),

]


