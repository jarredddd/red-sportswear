from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProductForm
from main.models import Product

def show_main(request):

    products_list = Product.objects.all()
    context = {
        'npm' : '2406432425',
        'nama' : 'Jarred Muhammad Radithya',
        'kelas' : 'PBP D',
        'nama_produk' : 'Adizero Evo SL',
        'harga' : 2700000,
        'kategori': 'Sepatu Running',
        'deskripsi': 'Sepatu yang ringan dan nyaman jika digunakan untuk lari',
        'stok' : '9',
        'products_list' : products_list
    }

    return render(request, "main.html", context)

def add_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_products.html", context)

def show_products(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "products_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
   try: 
    product_item = Product.objects.filter(pk=product_id)
    xml_data = serializers.serialize("xml", product_item)
    return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
      return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try: 
    product_item = Product.objects.get(pk=product_id)
    json_data = serializers.serialize("json", [product_item])
    return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
      return HttpResponse(status=404)


# Create your views here.
