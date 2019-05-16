from django.http import HttpResponse
from django.shortcuts import render
import json
import os


def upload(request):
    if request.method == 'POST':
        ret = {'status': False, 'data': None, 'error': None}
        try:

            img = request.FILES.get('img')
            fi = open(os.path.join('static', img.name), 'wb')
            for chunk in img.chunks(chunk_size=1024):
                fi.write(chunk)
            ret['status'] = True
            ret['data'] = os.path.join('static', img.name)
        except Exception as e:
            ret['error'] = e
        finally:
            fi.close()
            return HttpResponse(json.dumps(ret))
    return render(request, 'test.html')

