# forms.py
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import EmailMessage


from django.core.mail import send_mail
from django.template.loader import render_to_string



class CustomPasswordResetForm(PasswordResetForm):
   def send_password_reset_email(user, reset_link):
    subject = 'Password Reset'
    message = 'Please check your email for the password reset link.'
    from_email = 'akhilreddykaipausa@gmail.com'  # Replace with your email
    to_email = user.email

    html_message = render_to_string('template/registration/password_reset_email.html', {'reset_link': reset_link})

    send_mail(subject, message, from_email, [to_email], html_message=html_message)
