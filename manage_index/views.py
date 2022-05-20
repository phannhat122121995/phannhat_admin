from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm
import json
# Create your views here.
from django.urls import reverse

from manage_index.models import Category


def index_admin(request):
    # return HttpResponse("hello")
    return render(request, 'manager/index.html')


def addcategory(request,):
    # get_parents = Category.objects.all().filter(parent__isnull=True)
    get_parents = Category.objects.all()
    # slug = request.POST.get('texInputValue')
    if request.method == 'POST' and request.FILES:
        parent = request.POST['parent']
        # parentid = Category.objects.get(id=parent)
        title = request.POST['title']
        keywords = request.POST['keywords']
        description = request.POST['description']
        image = request.FILES['image']
        slug = request.POST['slug']
        status = request.POST['status']
        print("------đã chỉnh--------")
        print(image)
        print("-------end-------")
        if not title and image:
            messages.warning(request, "Bạn chưa điền vào form tiêu đề danh mục hoặc trường ảnh!!!")
        else:
            Category.objects.create(parent_id=parent, title=title, keywords=keywords, description=description, image=image, slug=slug, status=status)
            messages.success(request, "Bạn đã nhập danh mục thành công!!!")
    context = {
        'get_parents': get_parents,
    }
    return render(request, 'manager/add_category.html', context)


def index_category(request):
    get_list_categorys = Category.objects.all()
    context = {
        'get_list_categorys': get_list_categorys,
    }
    return render(request, 'manager/list_category.html', context)


def update_category(request, id):
    get_parents = Category.objects.all()
    get_id = Category.objects.filter(id=id)
    update_cate = Category.objects.get(id=id)
    category_intance = get_object_or_404(Category, id=id)
    print(category_intance)
    # form = CategoryForm(request.POST, instance=category_intance)
    # if form.is_valid():
    #     form.save()
    return render(request, 'manager/update_category.html', {'form':"form"})

    # if request.method == 'POST' and request.FILES:
    #     parent = request.POST['parent']
    #     # parentid = Category.objects.get(id=parent)
    #     title = request.POST['title']
    #     keywords = request.POST['keywords']
    #     description = request.POST['description']
    #     image = request.FILES['image']
    #     slug = request.POST['slug']
    #     status = request.POST['status']
    #     print("--------------")
    #     print(image)
    #     print("--------------")
    #     # if not title and image:
    #     #     messages.warning(request, "Bạn chưa điền vào form tiêu đề danh mục hoặc trường ảnh!!!")
    #     # else:
    #     print(type(image))
    #     print(image)
    #     Category.objects.filter(id=id).update(parent_id=parent, title=title, keywords=keywords, description=description, image=image, slug=slug, status=status)
    #     messages.success(request, "Bạn đã sửa danh mục thành công!!!")
    #     return render(request, 'manager/update_category.html')
    # context = {
    #     'get_parents': get_parents,
    #     'update_cate': update_cate,
    #     'get_id': get_id,
    # }
    # return render(request, 'manager/update_category.html', context)


def geturl(request):
    slug = request.GET.get('texInputValue')
    checkurl1 = Category.objects.filter(slug=slug).exists()
    if not checkurl1:
        test1 = "url tốt"
        check_status = 2
        response = {
            'test1': test1,
            'check_status': check_status,
        }
        return HttpResponse(json.dumps(response, default=str), content_type="application/json")
    else:
        test1 = "url đã tồn tại xin bạn hãy sửa lại, nút thêm sẻ kích hoạt"
        check_status = 1
        response = {
            'test1': test1,
            'check_status': check_status,
        }
        return HttpResponse(json.dumps(response, default=str), content_type="application/json")
    # print(checkurl1)
    # checkurl = Category.objects.all()
    # response = {
    #     'slug': checkurl,
    # }
    # return HttpResponse(json.dumps(response, default=str), content_type="application/json")


