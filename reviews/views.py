from django.shortcuts import render, redirect
from reviews.models import *
from django.http import HttpResponse

#def create_review(request, author_id, text, raiting):
#    review = Review(
#        author = author_id,
#        text = text,
#        raiting = raiting
#    ).save()
#
#    context = {
#        "review": review,
#    }
#
#    return render(
#        context,
#        
#    )
def home(request):
    return render(
        request,
        "reviews/main.html"
    )

def products(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request,
                "reviews/products.html",
                context)

def product_details(request, pk):
    product = Product.objects.get(id = pk)
    if request.method == "POST":
        author = request.POST.get('author')
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        review = Review.objects.create(
            product = product, 
            author = author,
            text = text,
            rating = rating,
        )

        return redirect('product-details', pk=pk)
    else:
        reviews = Review.objects.filter(product=product)
        context = {
            "product": product,
            "reviews": reviews,
        }

        return render(request,
                    "reviews/product_details.html",
                    context,
                    )

