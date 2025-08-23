import hashlib
from django.http import HttpResponse
from django.utils.http import http_date
from django.utils.timezone import now

def adstxt(request):
    content = "google.com, pub-0800147848250371, DIRECT, f08c47fec0942fa0\n"
    etag = hashlib.md5(content.encode("utf-8")).hexdigest()
    if request.META.get("HTTP_IF_NONE_MATCH") == etag:
        return HttpResponse(status=304)

    resp = HttpResponse(content, content_type="text/plain; charset=utf-8")
    resp["ETag"] = etag
    resp["Last-Modified"] = http_date(now().timestamp())
    resp["Cache-Control"] = "public, max-age=3600"
    return resp
