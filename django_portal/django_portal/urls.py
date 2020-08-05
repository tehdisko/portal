"""django_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from kb.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleSearchView,
    ArticleTagSearchView,
    # CommingSoonView
)

from kb.views import login_view, logout_view, soon_view
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view), 
    path('', ArticleListView.as_view(), name = 'article-list'),
    path('search/', ArticleSearchView.as_view(), name = 'article-list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name = "article-detail"),
   # path('soon/',CommingSoonView.as_view(), name = "soon"),
    path('create/', ArticleCreateView.as_view(), name = "article-create"),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name = "article-update"),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name = "article-delete"),
    path('admin/', admin.site.urls),
    path('soon/', soon_view, name = 'soon'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
