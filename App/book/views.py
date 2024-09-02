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
        books = (Book.objects.filter(book_id__icontains=query) | 
                 Book.objects.filter(book_name__icontains=query) | 
                 Book.objects.filter(author__icontains=query) | 
                 Book.objects.filter(category__icontains=query))
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Query parameter 'q' is required."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def check_book_id(request):
    book_id = request.query_params.get('book_id', None)
    if not book_id:
        return Response({'error': 'Book ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        book = Book.objects.get(book_id=book_id)
        return Response({'book_name': book.book_name, 'author' : book.author}, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)