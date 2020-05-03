from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

from opinion_ate.models import Author, Movie
from opinion_ate.serializers import AuthorSerializer, MovieSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @staticmethod
    @api_view(['GET'])
    def AuthorFindByNameViewSet(request, name):
        return HttpResponse(name)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@api_view(['POST'])
def AuthorCreate(request):
    try:
        payload = str(request.body)
        firstIndex = payload.find('{')
        lastIndex = payload.rindex('}')
        payloadFinal = json.loads(payload[firstIndex:lastIndex+1])


        #payload = { "id": 0,  "name": "Emilio3 Jacinto3", "email": "ej@gmail.com3" }
        #author = Author.objects.get(id=payload["author"])
        author = Author.objects.create(
            #id=payload["id"],
            name=payloadFinal["name"],
            email=payloadFinal["email"]
            )
        serializer=AuthorSerializer(author)
        return JsonResponse({'author': serializer.data})
    except ObjectDoesNotExist as e:
        return JsonResponse({'error1': str(e)})
    except Exception as f:
        return JsonResponse({'error2': 'Something terrible went wrong'})
