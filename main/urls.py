from django.urls import path
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import show_main, add_products, show_products, show_xml, show_json, show_json_by_id, show_xml_by_id, edit_product, delete_product, add_news_entry_ajax, proxy_image, create_flutter, show_json_mine

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-products/', add_products, name='add_products'),
    path('products/<str:id>/', show_products, name="show_products"),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('news/<uuid:id>/edit', edit_product, name='edit_product'),
    path('news/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-news-ajax', add_news_entry_ajax, name='add_news_entry_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_flutter, name='create_flutter'),
    path("show-json/mine/", show_json_mine, name="show_json_mine"),
]