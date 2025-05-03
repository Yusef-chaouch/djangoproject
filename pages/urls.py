from django.urls import path
from .views import homePageView,index
from .views import listBooks
from .views import index,listBooks,show
from .views import add
from .views import edit
from .views import remove
from .views import add_with_form,login


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create the router and register your ViewSet
router = DefaultRouter()
router.register(r'api/books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('index', index,name="index"),
    path('books', listBooks,name='listBooks'),
    path('<int:book_id>/', show,name='show'),
    path('ajouter_livre/', add,name='add'),
    path('modifier_livre/',edit,name='edit'),
    path('supprimer_livre/', remove,name='remove'),
    path('ajouter_livre_form/', add_with_form ,name='add book form'),
    path('login', login, name="login")
]