from django.contrib import admin
from sankalp.models import registered_Students, students_result,course,testimonial,enquiryform

# Register your models here.

class StudentData(admin.ModelAdmin):
  list_display = ( "registration_number", "firstName", "fatherName", "course")


class StudentsResult(admin.ModelAdmin):
    model = students_result
    list_display = ['grade','get_name',]
    
    
    def get_name(self, obj):
        student_data = obj.result_of_reg
        return f"{student_data.firstName}"



    
class courseData(admin.ModelAdmin):
  list_display = ( "courseName", "courseDesc",)

# class testimonialData(admin.ModelAdmin):
#   list_display = ( "testimonial_name", "testimonial_role",'testimonial_para')

# class enquiryData(admin.ModelAdmin):
#   list_display = ( "enquiryform_firstName", "enquiryform_email",'enquiryform_number','enquiryform_msg')






admin.site.register(registered_Students,StudentData)
admin.site.register(students_result,StudentsResult)
admin.site.register(course,courseData)
admin.site.register(testimonial)
admin.site.register(enquiryform)


  

