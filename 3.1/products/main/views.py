from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Product, Review

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        product = get_object_or_404(Product, pk=product_id)
        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data)



# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """
        Получение отзывов к товару с фильтрацией по оценке.
        """
        mark = request.query_params.get('mark')
        product = get_object_or_404(Product, pk=product_id)
        if mark is not None:
            comments = product.comments.filter(mark=mark)  # Изменено на product.comments
        else:
            comments = product.comments.all()  # Изменено на product.comments
        serializer = ReviewSerializer(comments, many=True)
        return Response(serializer.data)