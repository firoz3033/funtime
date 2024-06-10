from django.db import models
from tinymce.models import HTMLField


# registration data models
class registered_Students(models.Model):
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=80)
    fatherName = models.CharField(max_length=150)
    motherName = models.CharField(max_length=150)
    dob = models.DateField()
    gender        = models.CharField(max_length=30)
    email         = models.EmailField( max_length=50)
    registration_number  = models.CharField(max_length=12)
    student_number  = models.CharField(max_length=12)
    parent_number  = models.CharField(max_length=12)
    passed_class  = models.CharField(max_length=50)
    address  = models.CharField(max_length=200)
    city  = models.CharField(max_length=100)
    state  = models.CharField(max_length=100)
    zipcode  = models.CharField(max_length=100)
    course  = models.CharField(max_length=100)
    image = models.FileField(upload_to="students/",max_length=250,default=None,null=True)


    # New field for generating unique student IDs
    student_id = models.AutoField(primary_key=True)
    
    # Override the save method to generate unique IDs in the format 
    def save(self, *args, **kwargs):
        # Check if the instance is being created (not updated)
        if not self.pk:
            # Get the count of existing registered students
            count = registered_Students.objects.count()
            # Generate the unique student ID
            student_id = f"FNT2024{count+1:03d}"
            # Assign the generated student ID to the instance
            self.registration_number = student_id
        super().save(*args, **kwargs)


    def __str__(self) :
        return self.firstName 
    


# result model 
class students_result(models.Model):
    grade = models.CharField(max_length=50)
    result_of_reg =models.ForeignKey(registered_Students,on_delete=models.CASCADE)

    def __str__(self):
        return self.grade
    



# enquiry form model 

class enquiryform(models.Model):
    enquiryform_firstName = models.CharField(max_length=50)
    enquiryform_lastName = models.CharField(max_length=50)
    enquiryform_email = models.EmailField( max_length=50)
    enquiryform_number = models.CharField(max_length=50)
    enquiryform_msg = models.CharField(max_length=500)

    def __str__(self):
        return self.enquiryform_firstName



# course model 
class course(models.Model):
    courseName = models.CharField(max_length=100)
    courseDesc = models.CharField(max_length=200)
    courseAuthor = models.CharField(max_length=100)
    courseStartDate = models.DateField()
    courseEndDate = models.DateField()
    courseLanguage = models.CharField(max_length=100)
    coursePrice = models.CharField( max_length=10)
    courseDisPrice = models.CharField( max_length=10)
    courseDetails = HTMLField()
    courseFeatureImg = models.FileField(upload_to="course/",max_length=250,default=None,null=True)
    courseTagImg = models.FileField(upload_to="course/",max_length=250,default=None,null=True)

    def __str__(self) :
        return self.courseName





# testimonial model 
class testimonial(models.Model):
    testimonial_name = models.CharField( max_length=50)
    testimonial_role = models.CharField( max_length=50)
    testimonial_para = models.CharField( max_length=1000)
    testimonial_Img = models.FileField(upload_to="testimonial/",max_length=350,default=None,null=True)

    def __str__(self) :
        return self.testimonial_name

