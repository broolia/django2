from rest_framework import serializers
from main.models import Book, Order



class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    class Meta:
        model = Book
        fields = '__all__'
    

    #доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['orders_count'] = instance.order_set.count()
        return representation

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    # добавьте поля модели Order
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        books = instance.books.all()
        books_data = BookSerializer(books, many=True).data
        representation['books'] = books_data
        return representation
    ...

    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['books'] = ...
    #     return representation
