from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from badminton.views import minton_list, minton_detail, minton_new_1, minton_new
from myhomework15 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('badminton/', minton_list),
    path('badminton/<int:pk>', minton_detail),
    path('badminton/new1', minton_new_1),
    path('badminton/new', minton_new),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

