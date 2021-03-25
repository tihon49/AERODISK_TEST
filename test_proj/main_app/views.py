from django.shortcuts import render
from django.views import View

import subprocess



class BaseView(View):
    """отображение всех дисков"""

    def get(self, request):
        template = 'main_app/index.html'
        context = {'data': []}
        data = subprocess.Popen('lsblk', stdout = subprocess.PIPE, shell = True)
        result = data.communicate()[0].decode('cp866')

        for line in result.split('\n'):
            context['data'].append(line)
        
        return render(request, template, context)
        