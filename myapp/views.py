from django.shortcuts import render
from .models import Property  # ต้อง import Property ก่อนใช้

def propertiesPage(request):
    # ดึงข้อมูลจากฐานข้อมูล
    properties = Property.objects.all()  # หรือใช้ query อื่นๆ ตามความต้องการ
    return render(request, 'property.html', {'properties': properties})

def homePage(request):
    return render(request, 'home.html')  # สำหรับหน้าแรก (index.html)

def navbar(request):
    return render(request, 'navbar.html')  # ถ้ามีไฟล์ navbar.html หรือส่วนอื่นที่ต้องการ

def aboutPage(request):
    return render(request, 'about.html')

def contactPage(request):
    return render(request, 'contact.html')

def ownerPage(request):
    return render(request,  'owner.html')

def tenant_view(request):
    return render(request, 'tenant.html')  # Adjust template as needed

def leasePage(request):
    return render(request, 'lease.html')