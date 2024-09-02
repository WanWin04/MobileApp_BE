from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ImportBookOrder
from .serializers import ImportBookOrderSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from book.models import Book


class CreateImportBookOrderView(generics.CreateAPIView):
    queryset = ImportBookOrder.objects.all()
    serializer_class = ImportBookOrderSerializer
    permission_classes = [IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save()

@api_view(['POST'])
def check_book_id(request):
    book_id = request.data.get('book_id', None)
    if not book_id:
        return Response({'error': 'Book ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        book = Book.objects.get(book_id=book_id)
        return Response({'book_name': book.book_name, 'author' : book.author}, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)