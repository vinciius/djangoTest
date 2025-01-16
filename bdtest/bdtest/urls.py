from django.urls import path
from fruteirinha.views import home, contato, produtos
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=False)),  # Redireciona a raiz para /home/
    path('home/', home, name='home'),
    path('contato/', contato, name='contato'),
    path('produtos/', produtos, name='produtos'),  # Nova rota para a página de produtos
]