import hashlib
from pathlib import Path
from django.conf import settings
from django.http import HttpResponse
from django.utils.http import http_date
from django.utils.timezone import now

ADS_TXT_PATH = getattr(settings, 'BASE_DIR', Path(__file__).resolve().parent.parent) / "ads.txt"

def adstxt(request):
    if ADS_TXT_PATH.exists():
        content = ADS_TXT_PATH.read_text(encoding="utf-8")
    else:
        content = "google.com, pub-0800147848250371, DIRECT, f08c47fec0942fa0\n"
    etag = hashlib.md5(content.encode("utf-8")).hexdigest()
    if request.META.get("HTTP_IF_NONE_MATCH") == etag:
        return HttpResponse(status=304)

    resp = HttpResponse(content, content_type="text/plain; charset=utf-8")
    resp["ETag"] = etag
    resp["Last-Modified"] = http_date(now().timestamp())
    resp["Cache-Control"] = "public, max-age=3600"
    return resp

