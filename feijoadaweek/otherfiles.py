from django.http import HttpResponse

def adstxt():
    content = "google.com, pub-0800147848250371, DIRECT, f08c47fec0942fa0\n"
    return HttpResponse(content, content_type="text/plain; charset=utf-8")