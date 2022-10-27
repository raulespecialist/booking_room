from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Room, Event, Book
from .serializers import RoomSerializer, EventSerializer, BookSerializer, BookSerializer, BookListSerializer, RoomListSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

class EventViewSet(viewsets.GenericViewSet):
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSerializer
        return EventSerializer

    def get_queryset(self):
        queryset = Event.objects.select_related('room')

        if self.request.GET.get('me'):
            user = self.request.user
            queryset = queryset.filter(owner=user)
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).exclude(private=True)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(id=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        event = queryset.get(id=pk)
        if request.user == event.owner:
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            data_error=({'Error':'You cannot delete this item because it does not belong to you.'})
            return Response(data_error, status=status.HTTP_226_IM_USED)

    def create(self, request, *args, **kwargs):
        if request.user.groups.filter(name='business').exists():
            if request.POST.get('date') and request.POST.get('room'):
                date = request.POST.get('date')
                room = request.POST.get('room')
                create_query=Event.objects.filter(room=room, date=date)
                if create_query.exists():
                    data_error=({'Error':'Already exist an event in this room for ' + date})
                    return Response(data_error, status=status.HTTP_226_IM_USED)
                else:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save(owner=self.request.user)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data_error=({'Error':'Only users type Business can create an Event'})
            return Response(data_error, status=status.HTTP_401_UNAUTHORIZED)

class RoomViewSet(viewsets.GenericViewSet):
    serializer_class = RoomSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return RoomListSerializer
        return RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.all()

        if self.request.GET.get('room'):
            queryset = queryset.filter(id=self.request.GET.get('room'))
        else:
            queryset = queryset.order_by('-id')
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        if request.user.groups.filter(name='business').exists():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data_error=({'Error':'Only users type Business can create a Room'})
            return Response(data_error, status=status.HTTP_401_UNAUTHORIZED)

    
    def destroy(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        room = queryset.get(id=pk)
        if request.user == room.owner:
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            data_error=({'Error':'You cannot delete this item because it does not belong to you.'})
            return Response(data_error, status=status.HTTP_226_IM_USED)
    
    def retrieve(self, request, pk):
        queryset = self.filter_queryset(self.get_queryset())
        retrive_queryset = queryset.filter(id=pk)
        if retrive_queryset.exists():
            serializer = self.get_serializer(retrive_queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class BookViewSet(viewsets.GenericViewSet):
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset
    
    def list(self, request):
        user = self.request.user
        queryset = self.filter_queryset(self.get_queryset().filter(user=user))
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        user = request.user
        event = request.POST.get('event')
        create_query=Book.objects.filter(event=event, user=user)
        if create_query.exists():
            data_error=({'Error':'Already exist a book for this event.'})
            return Response(data_error, status=status.HTTP_226_IM_USED)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        book = queryset.get(id=pk)
        if request.user == book.user:
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            data_error=({'Error':'You cannot delete this item because it does not belong to you.'})
            return Response(data_error, status=status.HTTP_226_IM_USED)
    
    def retrieve(self, request, pk):
        queryset = self.filter_queryset(self.get_queryset())
        retrive_queryset = queryset.filter(id=pk)
        if retrive_queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)