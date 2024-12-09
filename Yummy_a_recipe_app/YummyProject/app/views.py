from django.shortcuts import render
from .models import Yummy , RecipeLikes
from django.db.models import Q
from .forms import RecipeForm , UserRegistraionForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request , 'home.html' )

# @login_required
def recipe_list(request):
    recipes = Yummy.objects.all().order_by('-created_at')
    # return render(request, 'home.html')
    return render(request, 'recipe_list.html', {'recipes': recipes ,})

@login_required
def recipe_create(request):
    if request.method == "POST" :
       form = RecipeForm(request.POST , request.FILES)
       if form.is_valid():
           recipe = form.save(commit=False)
           recipe.user = request.user
           recipe.save()
           return redirect(recipe_list)
    else:
       form = RecipeForm()
    return render(request , 'recipe_form.html', {'form': form,})

@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Yummy, pk=recipe_id, user= request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST , request.FILES, instance=recipe)
        if form.is_valid():
            recipe= form.save(commit=False)
            form.user = request.user
            recipe.save()       
            return redirect(recipe_list)
    else:
        form = RecipeForm(instance=recipe)
    return render(request , 'recipe_form.html', {'form': form,})

@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Yummy, pk=recipe_id, user= request.user)
    if request.method=='POST':
        recipe.delete()
        return redirect(recipe_list)
    return render(request , 'recipe_delete.html', {"recipe": recipe ,})

def register(request):
    
    if request.method == "POST":
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect(recipe_list)
        # pass
    else:
        form = UserRegistraionForm()
    

    return render(request, 'registration/signup.html' , {"form":form,})

@login_required
def search(request):
    query = request.GET.get('query')
    # result = Yummy.objects.all()
    result = Yummy.objects.filter(
        Q(recipe_name__icontains=query) | Q(user__username__icontains=query)
        )
    return render(request, 'search.html', {'query': query, "recipes":result})

@login_required
def oldest(request):
    # oldest = Yummy.objects.all().order_by('-created_at')
    oldest= Yummy.objects.all().order_by('-created_at').reverse()[:5]
    return render(request, 'recipe_list.html', {'recipes': oldest ,})

@login_required
def like_others_post(request, recipe_id):
    # getting recipe the user want to like
    recipe= get_object_or_404(Yummy, pk= recipe_id)

    # checking liked or not
    already_liked = RecipeLikes.objects.filter(
        user= request.user , recipe= recipe
    ).first()

    if already_liked:
        # deleting existing like
        already_liked.delete()
    else:
        # adding a new like
        RecipeLikes.objects.get_or_create(user= request.user , recipe= recipe)
    return redirect(recipe_list)