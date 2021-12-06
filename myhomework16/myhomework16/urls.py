from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from badminton.views import mlist, mdetail  # , minton_list, minton_detail
from myhomework16 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('badminton/', mlist),
    path('badminton/<int:pk>', mdetail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

