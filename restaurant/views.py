from django.shortcuts import render
from .models import Menu, Booking
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


# Create your views here.
def index_view(request):
    return render(request, template_name='index.html')


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]