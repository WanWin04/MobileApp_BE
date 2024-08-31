from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['POST'])
def add_book(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_books(request):
    query = request.query_params.get('q', None)  # Lấy giá trị của tham số 'q'
    if query:
        books = Book.objects.filter(book_name__icontains=query)  # Tìm kiếm không phân biệt chữ hoa/chữ thường
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Query parameter 'q' is required."}, status=status.HTTP_400_BAD_REQUEST)