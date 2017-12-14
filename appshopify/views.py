from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import F
from django.db.models import Sum
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status
#from .models import UserTodo,TodoList,LogUser,ListContent
#from .serializers import UserTodoSerializer, TodoListSerializer, ListContentSerializer#, LogUserSerializer 
import datetime
import time
import random
import re
import string
import json
#status-code
STATUS = {
    "200":status.HTTP_200_OK,
    "201":status.HTTP_201_CREATED,
    "202":status.HTTP_202_ACCEPTED,
    "204":status.HTTP_204_NO_CONTENT,
    "400":status.HTTP_400_BAD_REQUEST,
    "401":status.HTTP_401_UNAUTHORIZED,
    "404":status.HTTP_404_NOT_FOUND,
    "500":status.HTTP_500_INTERNAL_SERVER_ERROR
}
