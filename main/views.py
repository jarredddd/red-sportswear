import json
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils.html import strip_tags


@csrf_exempt
@require_POST
def add_news_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_news = Product(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_news.save()

    return HttpResponse(b"CREATED", status=201)


@login_required(login_url='/login')
def show_main(request):

    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406432425',
        'nama' : request.user.username,
        'kelas' : 'PBP D',
        'products_list' : products_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def add_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
       'form': form
        }

    return render(request, "add_products.html", context)

@login_required(login_url='/login')
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
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price' : product.price,
            'stok' : product.stok,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'news_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try: 
    product_item = Product.objects.filter(pk=product_id)
    xml_data = serializers.serialize("xml", product_item)
    return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
      return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try: 
    product = Product.objects.select_related('user').get(pk=product_id)
    data = {

        'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price' : product.price,
            'stok' : product.stok,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,

    }
    return JsonResponse(data)
   
   except Product.DoesNotExist:
      return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    if request.method == "POST":
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            form = UserCreationForm({
                'username': data.get('username'),
                'password1': data.get('password1'),
                'password2': data.get('password2'),
            })
            
            if form.is_valid():
                form.save()
                return JsonResponse({
                    'status': 'success',
                    'message': 'Your account has been successfully created!'
                })
            else:
                errors = form.errors.as_json()
                return JsonResponse({
                    'status': 'failed',
                    'message': 'Invalid registration details.',
                    'errors': errors
                }, status=400)
                
        # Handle non-AJAX POST request (fallback)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = JsonResponse({
                    'status': 'success',
                    'message': 'Successfully logged in!'
                })
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                return JsonResponse({
                    'status': 'failed',
                    'message': 'Sorry, incorrect username or password. Please try again.'
                }, status=401)
                
        # Handle non-AJAX POST request (fallback)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Sorry, incorrect username or password. Please try again.')
    
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
   if request.method == "POST":
        try:
            product = get_object_or_404(Product, pk=id)
            
            if request.headers.get('Content-Type') == 'application/json':
                data = json.loads(request.body)
                form = ProductForm(data, instance=product)
                
                if form.is_valid():
                    product = form.save()
                    return JsonResponse({
                        "status": "success",
                        "message": "Product updated successfully!",
                        "product": {
                            "id": str(product.id),
                            "name": product.name,
                            "description": product.description,
                            "price": product.price,
                            "stok": product.stok,
                            "category": product.category,
                            "thumbnail": product.thumbnail,
                        }
                    })
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid form data",
                    "errors": form.errors
                }, status=400)
            
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)
    
        product = get_object_or_404(Product, pk=id)
        context = {'form': ProductForm(instance=product)}
        return render(request, "edit_product.html", context)

def delete_product(request, id):
    if request.method == "DELETE":
        try:
            product = get_object_or_404(Product, pk=id)
            product.delete()
            return JsonResponse({
                "status": "success",
                "message": "Product deleted successfully!"
            })
        except Product.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Product not found"
            }, status=404)
    
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


# Create your views here.
