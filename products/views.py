from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from products.form import CommentForm
from products.models import Comment, Product

def index(request):
    products = Product.objects.all();
    
    return render(request, 'products/list_of_products.html', {'products': products});

def get_product(request, id):
    product = Product.objects.get(id=id);
    
    comments = Comment.objects.filter(product=id);
    
    form = CommentForm();
    
    return render(request, 'products/show_product.html', 
                  {'product': product,
                  'comments': comments,
                  'form': form}
                  );

@login_required
def add_new_comment(request, id):
    
    if request.method == "POST":
        
        form = CommentForm(request.POST);
        
        if form.is_valid:
            user = request.user;
            product = Product.objects.get(id=id)
            
            new_comment = form.save(commit=False);
            new_comment.author = user;
            new_comment.product = product;
            
            new_comment.save();

    return redirect('get_product', id);     