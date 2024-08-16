import after_response
from django.core.mail import send_mail


@after_response.enable
def send_contact_us_email(subject, message, sender, recipients):
    send_mail(
        subject,  # subject of the email
        message,  # body/message of the email
        sender,  # sender email
        recipients,
        fail_silently=False,
    )
