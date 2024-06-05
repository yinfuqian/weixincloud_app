import json
import logging
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
from .models import Falans
from .form import UploadFileForm

logger = logging.getLogger('log')



def handle_uploaded_file(file):
    df = pd.read_excel(file)

    # 遍历DataFrame中的每一行并创建Falans对象
    for _, row in df.iterrows():
        Falans.objects.create(
            Prssure=row['压力'],
            Diameter=row['通经'],
            Lenght=row['长度'],
            OutsideDiameter=row['外径'],
            Centre=row['孔中心'],
            WaterLineStep=row['水线台阶'],
            Thick=row['厚度'],
            WaterLineHeight=row['水线高度'],
            Count=row['孔数量']
        )


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            messages.success(request, '文件上传并处理成功！')
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
