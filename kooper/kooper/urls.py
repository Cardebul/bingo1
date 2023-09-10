from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView

urlpatterns = [
    path('', include('bingo.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('bingo:main'),
        ),
        name='registration',
    ),
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.handler500'