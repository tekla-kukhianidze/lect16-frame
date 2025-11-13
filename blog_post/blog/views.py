from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


@api_view(['POST'])
def create_blog_post(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        # For now, we’ll just return the validated data
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def blog_post_list_create(request):
    if request.method == 'GET':
        books = BlogPost.objects.filter(deleted=False)
        serializer = BlogPostSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            BlogPost.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def blog_post_detail_update_delete(request, id):
    if request.method == 'GET':
        book = BlogPost.objects.filter(id=id).first()
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogPostSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            book = BlogPost.objects.filter(id=id)
            if not book:
                return Response(status=status.HTTP_404_NOT_FOUND)
            BlogPost.objects.filter(id=id).update(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book = BlogPost.objects.filter(id=id).first()
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.deleted = True
        book.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostListCreateView(APIView):
    def get(self, request):
        books = BlogPost.objects.filter(deleted=False)
        serializer = BlogPostSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            BlogPost.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogPostDetailUpdateDeleteView(APIView):
    def get(self, request, id):
        book = BlogPost.objects.filter(id=id).first()
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogPostSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            book = BlogPost.objects.filter(id=id)
            if not book:
                return Response(status=status.HTTP_404_NOT_FOUND)
            BlogPost.objects.filter(id=id).update(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book = BlogPost.objects.filter(id=id).first()
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.deleted = True
        book.save()
        return Response(status=status.HTTP_204_NO_CONTENT)