from django.urls import path, include
from shopping_list.api.views import AddShoppingItem, ShoppingItemDetail, ListAddShoppingList, ShoppingListDetail

# from shopping_list.api.viewsets import ShoppingItemViewSet


# router = routers.DefaultRouter()
# router.register("shopping-items", ShoppingItemViewSet, basename="shopping-items")

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/shopping-lists/", ListAddShoppingList.as_view(), name="all-shopping-lists"),
    path("api/shopping-lists/<uuid:pk>/", ShoppingListDetail.as_view(), name="shopping-list-detail"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/", AddShoppingItem.as_view(), name="add-shopping-item"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/<uuid:item_pk>/", ShoppingItemDetail.as_view(), name="shopping-item-detail"),
]
