# py otp package

import random
from django.core.mail import EmailMessage


def generateOtp():
	otp = ""

	for i in range(6):
		otp += str(random.randint(1, 9))

	return otp


def send_code_to_user(email):
	Subject = "One time password for Email verification"
	otp_code = generateOtp()
	print(otp_code)
	user = User.objects.get(email=email)
	current_site = "myAuth.com"
	email_body = f"Hi thanks for signing up on {current_site} please use the code below to verify your email \n {otp_code}"
	from_email=settings.DEFAULT_FROM_EMAIL

	OneTimePassword.objects.create(user=user, code=otp_code)

	d_email = EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])
	d_email.send(fail_silent=True)


