from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# Create your views here.


class MiControlView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(data={}, status=200)

    def post(self, request):
        return Response(data={}, status=200)
