from django.shortcuts import render
from django.http import JsonResponse
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def UserList(request,format=None):
    if request.method=='GET':
        user=UserModel.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response({'user':serializer.data})
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def UserDetail(request,id,format=None):
    try:
        user=UserModel.objects.get(pk=id)
    except UserModel.DoesNoyExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if  request.method=="GET":
        serializer=UserSerializer(user)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# @api_view(['GET'])
# def User_View(request,id):
#     user=UserModel.objects.get(id=id)
#     serializer=UserSerializer(user)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def User_create(request):
#     user = UserModel.objects.all()
#     serializer = UserSerializer(user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#
# @api_view(['POST'])
# def User_Update(request,id):
#     user=UserModel.objects.get(id=id)
#     serializer=UserSerializer(instance=user,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#


