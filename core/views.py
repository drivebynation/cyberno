from django.shortcuts import render
from rest_framework.decorators import api_view
from time import sleep
from .models import Item
import schedule

@api_view()
def stack_fill(request, *args, **kwargs):
    while 1:
        schedule.every(20).seconds.do(Item.remove())
        string = input("please Enter Your Item for queue: ")
        Item.add(string)
        sleep(20)

