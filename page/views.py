from django.shortcuts import render

def home_view(request):
    return render(request, "page/home_page.html",{})

def about_us_view(request):
    page_title = "Hakkımızda"
    context = dict(
        page_title = page_title,
    )
    return render(request, "page/about_us.html", context)

def contact_us_view(request):
    page_title = "İletişim"
    context = dict(
        page_title = page_title,
    )
    return render(request, "page/contact_us.html", context)

def project_us_view(request):
    page_title = "Projeler"
    context = dict(
        page_title = page_title,
    )
    return render(request, "page/project_us.html", context)

def links_us_view(request):
    page_title = "Linkler"
    context = dict(
        page_title = page_title,
    )
    return render(request, "page/links_us.html", context)

def director_us_view(request):
    page_title = "Ekip"
    context = dict(
        page_title = page_title,
    )
    return render(request, "page/director_us.html", context)

def announcement_us_view(request):
    page_title = "Duyurular"
    context = dict(
        page_title = page_title,
    )
    return render(request, "page/announcements_us.html", context)