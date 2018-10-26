# Toutes les URLS de mes applis devront etre declarer ici
# Pour cela je dois importer les urls 
from django.conf.urls import url, include
from django.contrib import admin

# chargement du fichier settings et static pour avoir acces aux fichiers static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Je declare les URL de geolocate
    # le include permettra d'aller chercher dans le dossier correspondant
    # geolocate.urls va recuperer le contenu du fichiers urls.py
    url(r'^geolocate/', include('geolocate.urls', namespace='geolocate')),

]

# Cette strucuture de control me permettra de pointer aisemevt sur les 
#fichiers static correspondant
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

