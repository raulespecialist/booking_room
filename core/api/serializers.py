from .models import Room, Event, Book
from rest_framework import serializers

class RoomSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source="owner.username", read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Room
        fields = '__all__'

class RoomListSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source="owner.username", read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Room
        fields = ('id', 'owner', 'owner_name', 'capacity')

class BookListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)
    event_name = serializers.CharField(source="event.name", read_only=True)
    event_date = serializers.CharField(source="event.date", read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Book
        fields = ('id', 'user', 'user_name', 'event', 'event_name', 'event_date')

class BookSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)
    event_name = serializers.CharField(source="event.name", read_only=True)
    event_date = serializers.CharField(source="event.date", read_only=True)
    event_room = serializers.CharField(source="event.room", read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Book
        fields = '__all__'#('id', 'user', 'event', 'user_name', 'event_name', 'event_date', 'event_room')

class EventSerializer(serializers.ModelSerializer):
    spaces_available = serializers.SerializerMethodField()
    books = BookSerializer(many=True, read_only=True, source='book_set')
    owner_name = serializers.CharField(source="owner.username", read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Event
        fields = ('id', 'name', 'owner', 'owner_name', 'room', 'date', 'private', 'books', 'spaces_available')
    
    def get_spaces_available(self, instance):
        return instance.room.capacity - instance.book_set.count()
