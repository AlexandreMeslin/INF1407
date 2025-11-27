from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.template.loader import render_to_string
from django.urls import reverse

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Signal to send an email when a password reset token is created.
    :param sender: The sender of the signal
    :param instance: The instance of the view that triggered the signal
    :param reset_password_token: The created reset password token
    :param args: Additional arguments (not used)
    :param kwargs: Additional keyword arguments (not used)
    :return: None
    """
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'token': reset_password_token.key,
    }

    # Render the email content using a template
    email_html_message = render_to_string('email/password_reset_email.html', context)
    email_plaintext_message = render_to_string('email/password_reset_email.txt', context)

    # Create the email
    email = EmailMultiAlternatives(
        'Password Reset for Your Account',
        email_plaintext_message,
        'no-reply@example.com',
        [reset_password_token.user.email],
    )
    email.attach_alternative(email_html_message, "text/html")
    email.send()
    return
