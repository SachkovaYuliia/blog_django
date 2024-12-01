from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user_email):
    subject = 'Welcome to My Blog!'
    message = 'Thank you for registering on our platform.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)

def send_comment_notification(user_email, post_title):
    subject = 'New Comment on Your Post'
    message = f'Your post "{post_title}" has a new comment.'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])
