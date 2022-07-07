from rest_framework import viewsets, filters, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.post import PostSerializer, PostPostSerializer 
from ..models.post import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser


class PostsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        posts = Post.objects.filter(author=request.user.id)
        data = PostSerializer(posts, many=True).data
        return Response(data)

    def post(self, request, format=None):
        print(request.data)
        request.data['author'] = request.user.id
        post = PostPostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

class PostView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = PostSerializer(post).data
        return Response(data)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        updated_post = PostSerializer(post, data=request.data)
        if updated_post.is_valid():
            updated_post.save()
            return Response(updated_post.data)
        else:
            return Response(updated_post.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostUpload(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         print(request.data)
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)