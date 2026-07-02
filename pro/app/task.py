from celery import shared_task
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage



@shared_task
def send_welcome_email(email, username):

   
    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        </head>

        <body style="margin:0;padding:0;background:#f4f6f9;font-family:Arial,Helvetica,sans-serif;">

        <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f9;padding:40px 0;">
        <tr>
        <td align="center">

        <table width="600" cellpadding="0" cellspacing="0"
        style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.08);">

        <tr>
        <td align="center" style="background:#2563eb;padding:35px;">

        <img src="https://gautamsinh.duckdns.org/static/b.jpeg"
            alt="Photos Gallery"
            style="width:90px;border-radius:50%;">

        <h1 style="color:white;margin-top:20px;margin-bottom:0;">
        📸 Photos Gallery
        </h1>

        </td>
        </tr>

        <tr>
        <td style="padding:40px;">

        <h2 style="color:#222;margin-top:0;">
        Welcome, {username}! 👋
        </h2>

        <p style="font-size:16px;color:#555;line-height:1.7;">
        Your account has been created successfully.
        </p>

        <p style="font-size:16px;color:#555;line-height:1.7;">
        Thank you for joining <strong>Photos Gallery</strong>.
        We're excited to have you in our community.
        </p>

        <p style="font-size:16px;color:#555;line-height:1.7;">
        Upload your favorite memories, organize your collection,
        and enjoy sharing your best moments.
        </p>

        <div style="text-align:center;margin:40px 0;">

        <a href="https://gautamsinh.duckdns.org"
        style="
        background:#2563eb;
        color:white;
        padding:14px 30px;
        text-decoration:none;
        border-radius:8px;
        display:inline-block;
        font-weight:bold;
        ">
        Visit Photos Gallery
        </a>

        </div>

        <hr style="border:none;border-top:1px solid #eee;">

        <p style="font-size:13px;color:#888;text-align:center;">
        If you did not create this account, you can safely ignore this email.
        </p>

        </td>
        </tr>

        <tr>
        <td style="background:#f8f9fa;padding:20px;text-align:center;color:#777;font-size:13px;">

        © 2026 Photos Gallery<br>
        Made with ❤️ By Gautam Sinh<br>
        <a href="https://gautamsinh.duckdns.org" style="color:#2563eb;text-decoration:underline;">Visit My Website</a>

        </td>
        </tr>

        </table>

        </td>
        </tr>
        </table>

        </body>
        </html>
        """
  


    msg = EmailMultiAlternatives(
        subject="Welcome to Photos Gallery",
        body=f"Welcome to Photos Gallery, {username}!",
        # from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()