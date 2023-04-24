from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

app_name='blog'
urlpatterns =[

    path("", views.render_posts, name='posts'),
    path('<int:post_id>', views.post_detail, name="post_detail"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)