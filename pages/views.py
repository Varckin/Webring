from django.shortcuts import render
from api.models import WebringModel
from django.core.cache import cache
import time, requests

CACHE_TIMEOUT = 3 * 60 * 60 # 3 hour


def home(request):
    cached_webring = cache.get("webring_data")

    if cached_webring:
        return render(request, 'pages/home.html', {'participants': cached_webring})
    
    update_website_status()
    participants = WebringModel.objects.values('name', 'status', 'description', 'url', 'ping')
    cache.set("webring_data", participants, CACHE_TIMEOUT)

    return render(request, 'pages/home.html', {'participants': participants})


def check_website_status(url):
    try:
        start_time = time.time()
        response = requests.get(url=url, timeout=5)
        end_time = time.time()

        ping = int((end_time - start_time) * 1000)
        status = "online" if response.status_code == 200 else "offline"
    except requests.RequestException:
        ping = 0
        status = "offline"

    return {"status": status, "ping": ping}


def update_website_status():
    webring = WebringModel.objects.only("url", "status", "ping")

    for site in webring:
        result = check_website_status(site.url)
        if site.status != result.get("status"):
            site.status = result.get("status")
            site.ping = result.get("ping")
            site.save(update_fields=["status", "last_updated", "ping"])
        
        site.ping = result.get("ping")
        site.save(update_fields=["last_updated", "ping"])
