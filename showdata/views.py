from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from showdata.models import Data, DeviceName
from showdata.utils import get_date_list

hour_list = [" {num:02d}:00:00".format(num=i) for i in range(24)]
headers = ['shui_1','wen_1',
           'shui_2', 'wen_2',
           'shui_3', 'wen_3']


def home_view(request):

    return render(request, 'home.html')


def get_data_one(request):
    '''
    一天之内单个或多个传感器的数据
    :param request:
    :return:
    '''
    date = request.GET.get('date')
    addrs = request.GET.getlist('addr')
    result = []
    for addr in addrs:
        obj = {}
        obj['addr'] = addr
        obj['name'] = DeviceName.objects.filter(addr=addr).values()[0]['name']
        obj['shui_15'] = []
        obj['wen_15'] = []
        obj['shui_30'] = []
        obj['wen_30'] = []
        obj['shui_45'] = []
        obj['wen_45'] = []

    #     obj['data'] = []
    #     for hour in hour_list:
    #         try:
    #             data = {}
    #             data['time'] = date + hour
    #             arr = []
    #             temp = Data.objects.filter(addr=addr, time=data['time']).values()[0]
    #             for i in range(6):
    #                 arr.append(temp[headers[i]])
    #             data['arr'] = arr
    #             obj['data'].append(data)
    #         except Exception:
    #             pass
    #     result.append(obj)
    # json_obj = {'result': result}
    # return JsonResponse(json_obj)
    #     obj['15'], obj['30'], obj['45'] = [], [], []
        lists = {1: 'shui_1', 2: 'wen_1', 3: 'shui_2', 4: 'wen_2', 5: 'shui_3', 6: 'wen_3'}
        items = {1: 'shui_15', 2: 'wen_15', 3: 'shui_30', 4: 'wen_30', 5: 'shui_45', 6: 'wen_45'}
        temp = Data.objects.filter(addr=addr, time__contains=date).values()

        for tt in temp:
            obj['shui_15'].append(tt.get('shui_1'))
            obj['wen_15'].append(tt.get('wen_1'))
            obj['shui_30'].append(tt.get('shui_2'))
            obj['wen_30'].append(tt.get('wen_2'))
            obj['shui_45'].append(tt.get('shui_3'))
            obj['wen_45'].append(tt.get('wen_3'))
        result.append(obj)
    json_obj = {'result': result}
    return JsonResponse(json_obj)



# def get_data_mult(request):
#     '''
#
#     :param request:
#     :return:
#     '''
#     return HttpResponse('OK!')


def get_data_hour(request):
    '''
    选择一个小时
    单个或多个传感器在多天的数据
    :param request:
    :return:
    '''
    hour = request.GET.get('hour')
    addrs = request.GET.getlist('addr')
    start = request.GET.get('start')
    end = request.GET.get('end')

    result = []
    for addr in addrs:
        obj = {}


    return HttpResponse('ok')


def get_data_day(request):
    '''
    求一天之内的平均值
    单个或多个传感器在多天的数据
    :param request:
    :return:
    '''
    # day = request.GET.get('day')
    addrs = request.GET.getlist('addr')
    start = request.GET.get('start')
    end = request.GET.get('end')

    result = []
    for addr in addrs:
        obj = {}
        obj['addr'] = addr
        obj['name'] = DeviceName.objects.filter(addr=addr).values()[0]['name']
        obj['shui_15'] = []
        obj['wen_15'] = []
        obj['shui_30'] = []
        obj['wen_30'] = []
        obj['shui_45'] = []
        obj['wen_45'] = []

        for i in range(30):
            da = str('2017-09-' + str('{num:02d}'.format(num=i+1)))
            shui1, wen1, shui2, wen2, shui3, wen3 = 0, 0, 0, 0, 0, 0

            temp = Data.objects.filter(addr=addr, time__contains=da).values()
            tlen = len(temp)
            for i in range(tlen):
                shui1 += temp[i].get('shui_1')
                shui2 += temp[i].get('shui_2')
                shui3 += temp[i].get('shui_3')
                wen1 += temp[i].get('wen_1')
                wen2 += temp[i].get('wen_2')
                wen3 += temp[i].get('wen_3')
            obj['shui_15'].append(round(shui1 / tlen, 3))
            obj['wen_15'].append(round(wen1 / tlen, 3))
            obj['shui_30'].append(round(shui2 / tlen, 3))
            obj['wen_30'].append(round(wen2 / tlen, 3))
            obj['shui_45'].append(round(shui3 / tlen, 3))
            obj['wen_45'].append(round(wen3 / tlen, 3))

        result.append(obj)

    json_obj = {'result': result}
    return JsonResponse(json_obj)
