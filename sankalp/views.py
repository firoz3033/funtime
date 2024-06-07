from django.shortcuts import render,redirect,HttpResponse
from sankalp.models import registered_Students,students_result,course,testimonial, enquiryform
from django.core.mail import send_mail, EmailMultiAlternatives
from PIL import Image, ImageDraw, ImageFont  # for certificate 
from django.conf import settings
import io
import os
import uuid


# home page 

def index(request):
    courses = course.objects.all()
    testimonials = testimonial.objects.all()

    courseData = {
        'course': courses,
        'testimonial':testimonials
    }
    
    # enquiry data form submit handling
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        msg = request.POST.get('msg')

        enquiryForm = enquiryform(enquiryform_firstName=fname,enquiryform_lastName=lname,enquiryform_email=email,enquiryform_number=number,enquiryform_msg=msg)

        enquiryForm.save()
        fullname = fname.capitalize() + lname.capitalize()
        # enquiry mail 
        subject = "Thankyou For Enquiry"
        message = f'<div style="font-family: Arial, sans-serif; background-color: #f9f9f9; margin: 0; padding: 0;"><div style="max-width: 600px; margin: 20px auto; background-color: #ffffff; border: 1px solid #dddddd; border-radius: 5px;"> <div style="padding: 20px; text-align: center; background-color: #FFA500; color: white; border-top-left-radius: 5px; border-top-right-radius: 5px;"><h1 style="margin: 0;">Thank You for Your Inquiry!</h1></div><div style="padding: 20px;"><p style="font-size: 16px; color: #333333;">Dear {fullname},</p><p style="font-size: 16px; color: #333333;">Thank you for reaching out to Fun Time. We have received your inquiry and our team will get back to you shortly. Here are the details you provided:</p><div style="margin: 20px 0; padding: 15px; background-color: #f2f2f2; border-radius: 5px;"><h2 style="font-size: 18px; color: #333333; text-align: center;">Inquiry Details</h2><p style="font-size: 16px; color: #333333;"><strong>Name:</strong> {fullname}</p><p style="font-size: 16px; color: #333333;"><strong>Email:</strong> {email} </p><p style="font-size: 16px; color: #333333;"><strong>Phone:</strong> {number} </p><p style="font-size: 16px; color: #333333;"><strong>Message:</strong> {msg} </p></div><p style="font-size: 16px; color: #333333;">We appreciate your interest in our services. If you have any urgent questions, please feel free to contact us directly at <a href="mailto:Support.funtime@gmail.com" style="color: #4CAF50; text-decoration: none;">Support.funtime@gmail.com</a> or call us at <a href="tel:[Support Phone Number]" style="color: #4CAF50; text-decoration: none;">+91 1234567890</a>.</p><p style="font-size: 16px; color: #333333;">Thank you for choosing Fun Time. We look forward to assisting you.</p><p style="font-size: 16px; color: #333333;">Best regards,</p><p style="font-size: 16px; color: #333333;"><strong>Firoz Ansari</strong><br>Customer Support Team<br>Fun Time<br><a href="[Website URL]" style="color: #4CAF50; text-decoration: none;">funtime.com</a><br><a href="mailto:Support.funtime@gmail.com" style="color: #4CAF50; text-decoration: none;">Support.funtime@gmail.com</a><br><a href="tel:[Support Phone Number]" style="color: #4CAF50; text-decoration: none;">+91 1234567890</a></p><div style="margin-top: 20px; text-align: center;"><h2 style="font-size: 18px; color: #333333;">Connect with Us on Social Media</h2><div><a href="https://www.facebook.com/firozansari8767" style="margin: 0 10px; text-decoration: none;"><img src="https://i.pinimg.com/736x/c1/45/7e/c1457ec61545d41c3398072daf3cbd53.jpg" alt="" height="30px" width="30px"></a><a href="https://www.instagram.com/firozansari8767" style="margin: 0 10px; text-decoration: none;"><img src="https://i.pinimg.com/474x/1e/d6/e0/1ed6e0a9e69176a5fdb7e090a1046b86.jpg" alt="" height="30px" width="30px"> </a><a href="https://linkedin.com/in/firoz-ansari8767" style="margin: 0 10px; text-decoration: none;"><img src="https://i.pinimg.com/736x/d0/24/2f/d0242fc3351571f8243a1db4ac0370c6.jpg" alt="" height="30px" width="30px"></a><a href="https://www.youtube.com/@webcorecrafts" style="margin: 0 10px; text-decoration: none;"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfZgwqGYUpQDDGfyfeIrFzlPbqhGID2eqpfQ&s" alt="" height="30px" width="30px"> </a></div></div></div></div></div>'
        username = 'webahope@gmail.com'
        to = email
        email_msg = EmailMultiAlternatives(subject, message, username,[to])
        email_msg.content_subtype = 'html'
        email_msg.send()

        return render(request,'thankyou2.html')
    

    return render(request, 'index.html',courseData)







# registeration page 
def register(request):

    # sending course list 
    courselist = course.objects.all()

    # getting data from register form through post method
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        fatherName = request.POST.get("fatherName")
        motherName = request.POST.get("motherName")
        passed_class = request.POST.get("passed_class")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        student_number = request.POST.get("student_number")
        parent_number = request.POST.get("parent_number")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")
        crs = request.POST.get("course")
        # image = request.POST.get("image")
        image = request.FILES.get("image")


        # sending data to table of register students 
        student_registeration = registered_Students(firstName=firstName,lastName=lastName,fatherName=fatherName,motherName=motherName,passed_class=passed_class,dob=dob,gender=gender,student_number=student_number,parent_number=parent_number,email=email,address=address,city=city,state=state,zipcode=zipcode,course=crs,image=image)
        student_registeration.save()


        # email to user 
        register_no_to_mail = registered_Students.objects.filter(firstName=firstName,lastName=lastName,fatherName=fatherName).first()
        fullname = firstName.capitalize() + lastName.capitalize()
        x = course.objects.filter(courseName=crs).first()
        subject = 'Welcome To Fun Time! Your registration has successful'
        message = f'<div style="font-family: Arial, sans-serif; background-color: #f9f9f9; margin: 0; padding: 0;"><div style="max-width: 600px; margin: 20px auto; background-color: #ffffff; border: 1px solid #dddddd; border-radius: 5px;"><div style="padding: 20px; text-align: center; background-color: #FFA500; color: white; border-top-left-radius: 5px; border-top-right-radius: 5px;"><h1 style="margin: 0;">Welcome to Fun Time!</h1></div><div style="padding: 20px;"><p style="font-size: 16px; color: #333333;">Dear {fullname},</p><p style="font-size: 16px; color: #333333;">Congratulations! We are excited to inform you that your registration for the <strong>{crs}</strong> course at Fun Time has been successfully completed.</p> <div style="margin: 20px 0; padding: 15px; background-color: #f2f2f2; border-radius: 5px;"><h2 style="font-size: 18px; color: #333333; text-align: center;">Course Details</h2><p style="font-size: 16px; color: #333333;"><strong>Registration NO:</strong> {register_no_to_mail.registration_number}</p><p style="font-size: 16px; color: #333333;"><strong>Course Name:</strong> {crs}</p><p style="font-size: 16px; color: #333333;"><strong>Start Date:</strong>{x.courseStartDate} </p><p style="font-size: 16px; color: #333333;"><strong>Duration:</strong> {x.courseEndDate}</p><p style="font-size: 16px; color: #333333;"><strong>Instructor:</strong> {x.courseAuthor}</p></div><p style="font-size: 16px; color: #333333;">To get started, please visit your course dashboard at <a href="[Website URL]" style="color: #4CAF50; text-decoration: none;">funtime.com</a>. Here, you\'ll find all the necessary materials, schedules, and resources to help you succeed in your learning journey.</p><p style="font-size: 16px; color: #333333;">If you have any questions or need assistance, feel free to reach out to our support team at <a href="mailto:[Support Email]" style="color: #4CAF50; text-decoration: none;">Support.funtime@gmail.com</a> or call us at <a href="tel:[Support Phone Number]" style="color: #4CAF50; text-decoration: none;">+91 1234567890</a>. We\'re here to help!</p><p style="font-size: 16px; color: #333333;">Thank you for choosing Fun Time. We look forward to seeing you in class and supporting you in achieving your goals.</p><p style="font-size: 16px; color: #333333;">Best regards,</p><p style="font-size: 16px; color: #333333;"><strong>Firoz Ansari</strong><br>Customer Support Team<br>Fun Time<br><a href="[Website URL]" style="color: #4CAF50; text-decoration: none;">funtime.com</a><br><a href="mailto:[Support Email]" style="color: #4CAF50; text-decoration: none;">Support.funtime@gmail.com</a><br><a href="tel:[Support Phone Number]" style="color: #4CAF50; text-decoration: none;">+91 1234567890</a></p><div style="margin-top: 20px; text-align: center;"><h2 style="font-size: 18px; color: #333333;">Connect with Us on Social Media</h2><div><a href="https://www.facebook.com/firozansari8767" style="margin: 0 10px; text-decoration: none;"> <img src="https://i.pinimg.com/736x/c1/45/7e/c1457ec61545d41c3398072daf3cbd53.jpg" alt="" height="30px" width="30px"></a><a href="https://www.instagram.com/firozansari8767" style="margin: 0 10px; text-decoration: none;"><img src="https://i.pinimg.com/474x/1e/d6/e0/1ed6e0a9e69176a5fdb7e090a1046b86.jpg" alt="" height="30px" width="30px"></a><a href="https://linkedin.com/in/firoz-ansari8767" style="margin: 0 10px; text-decoration: none;"><img src="https://i.pinimg.com/736x/d0/24/2f/d0242fc3351571f8243a1db4ac0370c6.jpg" alt="" height="30px" width="30px"></a><a href="https://www.youtube.com/@webcorecrafts" style="margin: 0 10px; text-decoration: none;"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfZgwqGYUpQDDGfyfeIrFzlPbqhGID2eqpfQ&s" alt="" height="30px" width="30px"></a></div></div></div></div></div>'
        username ='webahope@gmail.com'
        to = email

        email_send = EmailMultiAlternatives(subject,message,username,[to])
        email_send.content_subtype = 'html'
        email_send.send()

        # now again sending a mail for registeration number 

        return render (request, 'thankyou.html')

    context = {
        'course': courselist,
        }
    return render(request, 'register.html', context)






# results page where we will enter our roll no 
regist_number = ''
def searchResults(request):

    global regist_number        # declare global variable 
    if request.method=="POST":
        registration_number = request.POST.get('registration_number')
        
        regist_number = registration_number    # updating the value 
        print('registration number =',regist_number)

        matching_results = students_result.objects.filter(result_of_reg__registration_number = registration_number)
        if matching_results.exists():
            result = matching_results.first() #getting first elemnt of mathiching data
            reg_num = result.result_of_reg.registration_number
            url = f"/result/resultget?key={reg_num}"
            return redirect(url)
        else:
            message = {
                'error': "No Records Found"
            }
            print("nothins found")
            return render(request, 'searchResults.html',message)

    

    return render(request, 'searchResults.html')







# result page  
def result(request,res):
    
    matching_results = students_result.objects.filter(result_of_reg__registration_number = regist_number)
    if matching_results.exists():
            result = matching_results.first() #getting first elemnt of mathiching data
            
            resultData = {
                "grade" : result.grade,
                "student":result.result_of_reg,
            }

            fullName = result.result_of_reg.firstName.capitalize() + result.result_of_reg.lastName.capitalize()
    
            template_path = os.path.join(settings.BASE_DIR, 'static/certificates/certificate_template.png' )
            certificate_template = Image.open(template_path)
            draw = ImageDraw.Draw(certificate_template)

            # Define the font and size
            font_path1 = os.path.join(settings.BASE_DIR, 'static/certificates/GreatVibes-Regular.ttf')
            font_path = 'arial.ttf'
            font = ImageFont.truetype(font_path1, 105)
            font2 = ImageFont.truetype(font_path, 40)

            # Draw the text on the certificate
            draw.text((730, 620), fullName, font=font, fill='#0E477D')
            draw.text((485, 765), result.result_of_reg.fatherName, font=font2, fill='#0E477D')
            draw.text((525, 820), result.result_of_reg.course, font=font2, fill='#0E477D')
            draw.text((368, 126), result.result_of_reg.registration_number, font=font2, fill='#0E477D')

            # Save the generated certificate to a temporary file
            temp_filename = f"{uuid.uuid4()}.png"
            temp_filepath = os.path.join(settings.MEDIA_ROOT, temp_filename)
            certificate_template.save(temp_filepath)

            # Pass the file URL to the template
            certificate_url = os.path.join(settings.MEDIA_URL, temp_filename)
            context = {
                'certificate_url': certificate_url,
                'studentname':fullName
            }
        
            return render(request, 'result.html', context)
            
    else:
        return redirect("/search_results")





# course details page 
    
def courseDetails(request,course_name):
    # course_name = course_name
    course_Data = course.objects.filter(courseName = course_name)
    courseData = course_Data.first()
    return render(request, 'courseDetails.html',{'course':courseData})




# other page 

def refundPolicy(request):
    return render(request, 'refundpolicy.html')

def desclaimer(request):
    return render(request, 'desclaimer.html')

def privacyPolicy(request):
    return render(request, 'privacyPolicy.html')

def termsandcondition(request):
    return render(request, 'termsandcondition.html')