from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Department, Teacher,School
from django.views import View


# Create your views here.
def home(request):
    return render(request, 'navapp/home.html')

def hostel(request):
    return render(request,'navapp/hostel.html')

def admission(request):
    return render(request,'navapp/admission.html')

def searchbar(request):
    
    if request.method=='POST':
        # 'searched' is the name of input
        searched =  request.POST['searched']
        dept_search = Department.objects.filter(dept_name__icontains = searched)
        dept_search_hod = Department.objects.filter(head_name__icontains = searched)
        dept_search_loc = Department.objects.filter(location__icontains = searched)
        
        teacher_search = Teacher.objects.filter(name__icontains = searched)
        teacher_office_search = Teacher.objects.filter(office__icontains = searched)
        
        school_search = School.objects.filter(school_name__icontains = searched)
        school_search_loc = School.objects.filter(location__icontains = searched)
        
    
    else:
        
        searched =  request.POST['searched']
        
        dept_search = Department.objects.filter(dept_name__icontains = searched)
        dept_search_hod = Department.objects.filter(head_name__icontains = searched)
        dept_search_loc = Department.objects.filter(location__icontains = searched)
        
        teacher_search = Teacher.objects.filter(name__icontains = searched)
        teacher_office_search = Teacher.objects.filter(office__icontains = searched)        
        
        school_search = School.objects.filter(school_name__icontains = searched)
        school_search_loc = School.objects.filter(location__icontains = searched)
        
    return render(request,'navapp/search.html',context={
        "searched":searched,
        
        "searched_depts":dept_search,
        "searched_hod": dept_search_hod,
        "searched_by_dept_loc":dept_search_loc,
        
        "searched_teacher": teacher_search,
        "seacherd_by_office":teacher_office_search,
        
        "searched_school": school_search,
        "school_search_for_loc":school_search_loc,
    })

class AllSchoolView(ListView):
    template_name="navapp/all_schools.html"
    model= School
    context_object_name = "all_schools"

# class AllDeptView(ListView):
#     template_name="navapp/all_dept.html"
#     model = Department
#     context_object_name = "all_dept"

class AllDeptView(View):
    
    def get(self,request,slugy):
        school = School.objects.get(slugy=slugy)
        
        context={
            "school": school,
            "all_dept" : school.departments.all().order_by("id")
            
        }
        return render(request,"navapp/all_dept.html",context)
    
class AllTeacherView(View):
    
    def get(self,request,slug):
        dept = Department.objects.get(slug=slug)
        
        context={
            "dept": dept,
            "all_teachers" : dept.teachers.all().order_by("id")
            
        }
        return render(request,"navapp/dept_teachers.html",context)
    
        