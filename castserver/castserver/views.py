import json
import traceback
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ipware.ip import get_ip

from castserver import models

@csrf_exempt
def report(request):
    try:
        if request.method == 'POST':
            tags = request.POST.get("tags", [])
            print("######################################")
            print("Report from %s" % (get_ip(request)))

            print("Available tags:")

            for tag in json.loads(tags):
                print("%s %s" % (tag["name"], tag["signal"]))

            return HttpResponse(status=200)
    except:
        traceback.print_exc()
        raise