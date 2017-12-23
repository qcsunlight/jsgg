import xlrd

from showdata.models import Data
import datetime


def import_data(self, request, obj, change):

    # file = request.FILES.get('file')
    # dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath('File'))), 'jsgg', 'File')
    # filepath = os.path.join(dir, file)
    data = xlrd.open_workbook(obj.file.path)
    sheet = data.sheet_by_index(0)
    headers = ['addr', 'name', 'time', 'shui_1', 'wen_1', 'shui_2', 'wen_2', 'shui_3', 'wen_3']
    lists = []
    for row in range(1, sheet.nrows):
        addr = sheet.cell_value(row, 0)
        name = sheet.cell_value(row, 1)
        time = sheet.cell_value(row, 2)
        shui_1 = sheet.cell_value(row, 3)
        wen_1 = sheet.cell_value(row, 4)
        shui_2 = sheet.cell_value(row, 5)
        wen_2 = sheet.cell_value(row, 6)
        shui_3 = sheet.cell_value(row, 7)
        wen_3 = sheet.cell_value(row, 8)
        data = Data(addr=addr, name=name, time=time,
                    shui_1=shui_1, wen_1=wen_1,
                    shui_2=shui_2, wen_2=wen_2,
                    shui_3=shui_3, wen_3=wen_3)
        lists.append(data)
    Data.objects.bulk_create(lists)


def get_date_list(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list
