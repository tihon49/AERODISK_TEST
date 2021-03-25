from django.shortcuts import render, redirect
from django.views import View

import subprocess
import re


def get_disk_data(some_data: str) -> dict:
    """принимает строку, ищет в ней:
            1. Имя диска
            2. Размер диска
            3. Mountpoint

        возвращает словарь с данными о диске либо False
    """

    # находим нужные данные с помощью регулярных выражений
    disk_name_lookFor = 'sd[a-z]\d?'
    disk_space_lookFor = '\d{1,4},?\d?[A-Z]'

    disk_name = re.findall(disk_name_lookFor, some_data)
    disk_space = re.findall(disk_space_lookFor, some_data)
    mountpoint = some_data.split(' ')[-1]

    if disk_name:
        data_to_return = ({'name': disk_name[0],
                           'size': disk_space[0],
                           'mountpoint': mountpoint
                           })

        return data_to_return

    return False


class BaseView(View):
    """отображение всех дисков"""

    def get(self, request):
        template = 'main_app/index.html'
        context = {'data': []}
        command = subprocess.Popen('lsblk', stdout=subprocess.PIPE, shell=True)
        result = command.communicate()[0].decode('cp866')

        for line in result.split('\n')[1:]:
            result = get_disk_data(line)

            if result:
                context['data'].append(result)

        return render(request, template, context)


class MountView(View):
    """монтирование диска"""

    def get(self, request, disk_name):
        command = subprocess.Popen(f'sudo mount /dev/{disk_name} /mnt/', stdout=subprocess.PIPE, shell=True)
        result = command.communicate()[0].decode('cp866')
        print(result)

        return redirect('base')


class UnmountView(View):
    """размонтирование диска"""

    def get(self, request, disk_name):
        command = subprocess.Popen(f'sudo umount -l /mnt', stdout=subprocess.PIPE, shell=True)
        result = command.communicate()[0].decode('cp866')
        print(result)

        return redirect('base')


class FormateDiskView(View):
    """фоматирование диска"""

    def get(self, request, disk_name):
        command = subprocess.Popen(f'sudo mkfs -t ext4 /dev/{disk_name}', stdout=subprocess.PIPE, shell=True)
        result = command.communicate()[0].decode('cp866')
        print(result)

        return redirect('base')
