from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .models import QueryResponse
from .serializers import QueryResponseSerializer
import google.generativeai as genai
import os
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


Api_key = 'AIzaSyBdiPViXz26n3eFeQKSx6wKtK8rBk0ZkNk'

genai.configure(api_key=Api_key)

model = genai.GenerativeModel('gemini-1.5-flash') # Assuming you have this function available

# class QueryResponseView(APIView):

#     def post(self, request):
#         email = request.data.get('email')
#         question = request.data.get('question')
        
#         # Generate AI response using Gemini AI (or any other AI model)
#         response_text = model.generate_content(question)
        
#         # Save to the database
#         query_response = QueryResponse.objects.create(email=email, question=question, response=response_text)
        
#         # Serialize and return the response
#         serializer = QueryResponseSerializer(query_response)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@method_decorator(csrf_exempt,name = 'dispatch')
class QueryResponseView(APIView):

    def post(self, request,*args,**kwargs):
        email = request.data.get('email')
        question = request.data.get('question')

        # Assuming you have a function to generate the AI response
        response_text = model.generate_content(question)
        print(response_text)
        
        my_res = {
            'email': email,
            'question': question,
            'response': response_text
        }

        serializer = QueryResponseSerializer(data = my_res)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')
    
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     # Return an error response with the validation errors
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



