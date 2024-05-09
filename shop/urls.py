from . import views
from django.urls import path

urlpatterns = [
    path("", views.woocommerce,name='shop'),
    #path('<shop>/<description>', views.dynamic_shop),
    path("list", views.listofdays),
    # path("models/",views.viewName,name='viewName'),
    # path("<int:shop>", views.dynamic_shop_keys),
    # path("<str:shop>", views.dynamic_shop),
    path("add-to-cart/",views.add_to_cart,name="add_to_cart"),
    path("cart/",views.cart_view,name='cart_view'),
    path("<slug:s>",views.viewNameDetails,name="viewNameDetails"),

    
]


