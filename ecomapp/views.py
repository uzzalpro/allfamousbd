from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from ecomapp.models import Setting,ContactMessage,ContactForm
from django.urls import reverse

from Product.models import Product, Images, Category, Comment
from ecomapp.forms import SearchForms
from OrderApp.models import ShopCart
# Create your views here.
def Home(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount+=p.product.new_price*p.quantity
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:2]
    Latest_Clothings = Product.objects.all().order_by('-id')
    products = Product.objects.all()
    


    context = {'category': category,
               'setting': setting,
               'sliding_images': sliding_images,
               'Latest_Clothings': Latest_Clothings,
               'products': products,
               'total_amount': total_amount}
    return render(request, 'home.html',context)


def About(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)

    context = {'category': category,
               'setting': setting   
    }
    return render(request, 'about.html',context)



def product_single(request,id):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    single_product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('id')[:4]
    comment_show = Comment.objects.filter(product_id=id, status='True')

    context = {'category': category,
               'setting': setting,
               'single_product':single_product,
               'images': images,
               'products':products,
               'comment_show': comment_show}
    return render(request, 'product_single.html',context)


def category_product(request,id,slug):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:2]
    product_cat = Product.objects.filter(category_id=id)
    context={
    'category': category,
    'setting': setting,
    'sliding_images': sliding_images,
    'product_cat': product_cat    
    }
    return render(request,'category_product.html',context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form. is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            #messages.success(request. 'Your message has been sent')

            return HttpResponseRedirect(reverse('contact_dat'))

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    category = Category.objects.all()

    context={    
    'setting': setting,
    'category': category,
    'form': form,
    }
    return render(request,'contact_form.html',context)


def SearchView(request):
    if request.method == 'POST':
        form = SearchForms(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=cat_id)
            category = Category.objects.all()        

            context={    
            'category': category,
            'query': query,
            'product_cat': products,
            }
            return render(request,'category_product.html',context)

    return HttpResponseRedirect('category_product')            

def ShopAll(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    shop_all = Product.objects.all().order_by('-id')[:10]

    context = {'setting': setting,
               'category': category,
               'shop_all': shop_all}

    return render(request,'Shop_all.html',context)     