from django.shortcuts import render
from ArchiveApp.models import Movies, MovieReview, Admin
from django.http.response import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

# Main Screetn
def Main(request):
    datas = Movies.objects.all()
    return render(request, "Main.html", {"recentones" : datas})

def Review(request):   
    if request.method == "GET":
        review_info = MovieReview.objects.get(review_idx=request.GET.get("idx"))
        movie_title = Movies.objects.get(idx=request.GET.get("idx"))
    return render(request, "Review.html", {"review_info" : review_info, "movie_title" : movie_title})

# Login & Regiseter & QNA
def Request(request):   
    return render(request, "Request.html")

def Register(request):   
    return render(request, "Register.html")

def RegisterOK(request):
    if request.method =="POST":
        Admin(
            id = request.POST.get("id"),
            pwd = request.POST.get("pwd")
        ).save() 
    return HttpResponseRedirect("/")
def Login(request):   
    return render(request, "Login.html")


#CRUD Operations
def MoviesInsert(request): 
    return render(request, "moviesinsert.html")  

def MoviesInsertOK(request):
    if request.method == "POST":
        if("img" in request.FILES):
            upload_img = request.FILES["img"]
            fs = FileSystemStorage()
            fs.save(upload_img.name, upload_img)
            Movies(
                idx = Movies.objects.order_by("idx").last().idx + 1,
                title=request.POST.get("title"),
                date=request.POST.get("date"),
                genre=request.POST.get("genre"),
                rate=request.POST.get("rate"),
                img = upload_img.name
            ).save()
        else:
            Movies(
                idx = Movies.objects.order_by("idx").last().idx + 1,
                title=request.POST.get("title"),
                date=request.POST.get("date"),
                genre=request.POST.get("genre"),
                rate=request.POST.get("rate"),
            ).save()
    idx = Movies.objects.order_by("idx").last().idx
    return render(request, "reviewinsert.html", {"idx": idx})

def ReviewInsert(request):
    if request.method=="GET":
        idx = request.GET.get("idx")
    return render(request, "reviewinsert.html", {"idx": idx})

def ReviewInsertOK(request):
    if request.method == "POST":
        MovieReview(
        review_idx = request.POST.get("review_idx"),
        description=request.POST.get("description"),
        violence=request.POST.get("violence"),
        exposure=request.POST.get("exposure"),
        torture=request.POST.get("torture"),
        weak=request.POST.get("weak"),
        drug=request.POST.get("drug"),
        fear=request.POST.get("fear"),
        shocking=request.POST.get("shocking"),
        profanity=request.POST.get("profanity"),
        discrimination=request.POST.get("discrimination"),
        ).save()    
    return HttpResponseRedirect("/")

def MoviesUpdate(request):
    updatemovie = Movies.objects.get(idx=request.GET.get("review_idx"))
    return render(request, "movieupdate.html", {"updatemovie" : updatemovie})
    
def MoviesUpdateOK(request):
    if request.method == "POST":
            index = request.POST.get("idx")
            upload_img = request.FILES["img"]
            fs = FileSystemStorage()
            fs.save(upload_img.name, upload_img)
            updatemovie.img = upload_img.name,
            updatemovie = Movies.objects.get(idx=request.POST.get("idx"))
            updatemovie.title = request.POST.get("title")
            updatemovie.date = request.POST.get("date")
            updatemovie.genre = request.POST.get("genre")
            updatemovie.rate = request.POST.get("rate")
            updatemovie.save()
    return HttpResponseRedirect("/reviewupdate/?idx=%s" % index)


def ReviewUpdate(request):
    updatereview = MovieReview.objects.get(review_idx=request.GET.get("idx"))
    return render(request, "reviewupdate.html", {"updatereview" : updatereview})

    
def ReviewUpdateOK(request):
    if request.method == "POST":
        updatereview = MovieReview.objects.get(review_idx=request.POST.get("review_idx"))
        updatereview.description = request.POST.get("description")
        updatereview.violence = request.POST.get("violence")        
        updatereview.exposure = request.POST.get("exposure")        
        updatereview.torture = request.POST.get("torture")
        updatereview.profanity = request.POST.get("profanity")
        updatereview.weak = request.POST.get("weak")
        updatereview.fear = request.POST.get("fear")
        updatereview.drug = request.POST.get("drug")
        updatereview.shocking = request.POST.get("shocking")
        updatereview.discrimination = request.POST.get("discrimination")
        updatereview.save()
    return HttpResponseRedirect("/")

def Delete(request):
    deletereview = MovieReview.objects.get(review_idx=request.GET.get("review_idx"))
    deletereview.delete()
    deletemovie = Movies.objects.get(idx=request.GET.get("review_idx"))
    deletemovie.delete()
    return(HttpResponseRedirect("/"))
