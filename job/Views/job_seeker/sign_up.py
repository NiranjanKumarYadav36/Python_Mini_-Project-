import re
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views import generic, View
from job.models import JobSeeker
from job.utils import *
from django.contrib import messages
from django.core.exceptions import ValidationError


class UserSignupView(View):
    template_name = 'job_seeker/UserRegistration.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:

            # Get form data from POST request
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            password = request.POST.get('pwd')
            location = request.POST.get('location')
            city = request.POST.get('city')

            name = name.title()
            city = city.title()

            # Check password strength
            if not is_password_strong(password):
                messages.warning(request, "Password does not meet strength requirements.")
                return render(request, self.template_name)

            # Check for forbidden words in the password
            forbidden_words = ['password', '123456', 'qwerty']
            for word in forbidden_words:
                if word.lower() in password.lower():
                    messages.warning(request, "Password contains forbidden word(s).")
                    return render(request, self.template_name)

            # Define a regular expression pattern to match only digits
            pattern = r'^\d{10,11}$'

            # Check if the mobile number matches the pattern
            if not re.match(pattern, mobile) or len(mobile) > 10 or len(mobile) < 10:
                messages.error(request, "Mobile number should contain only digits and be 10 digits long.")
                return render(request, self.template_name)

            if User.objects.filter(email=email).exists():
                messages.warning(request, "User with this email already exists.")

            # Create new User object
            new_user = User.objects.create_user(username=email, password=password)
            new_user.save()

            # Create new JobSeeker object
            new_job_seeker = JobSeeker(full_name=name, email_id=email, mobile_no=mobile, address=location,
                                       city=city, user=new_user)
            new_job_seeker.save()

            # message_body = f"A new job Application was submitted. Thank You, {name}."
            # email_message = EmailMessage("Form Submission Confirmation", message_body, to=[email])
            # email_message.send()

            messages.success(request, 'Signup success')
            return redirect('login')

        except ValidationError as e:
            messages.warning(request, f"Fail: {str(e)}")

        return render(request, self.template_name)


