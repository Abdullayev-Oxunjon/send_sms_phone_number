import random

from twilio.rest import Client


def send_sms(body, number):
    account_id = "AC52a658bfaa6f62566e239868e1a6cd2d"
    auth_token = "0a2eb3371c8b0f929a753d48ee2aeb89"
    client = Client(account_id, auth_token)
    messages = client.messages.create(
        body=body,
        from_='+17733210345',
        to=number
    )


def generate_verification_code():
    return str(random.randint(100000, 999999))


# def send_forgot_password_email(to_, verification_code):
#     subject = 'Parolni tiklash'
#     message = f"Parolni tiklash uchun quyidagi kodni kiriting:\n\n{verification_code}\n\nRahmat!"
#     from_email = settings.EMAIL_HOST_USER
#     send_mail(subject, message, from_email, [to_email])


def send_forgot_password_phone_number(body, number):
    account_id = "AC52a658bfaa6f62566e239868e1a6cd2d"
    auth_token = "0a2eb3371c8b0f929a753d48ee2aeb89"
    client = Client(account_id, auth_token)
    messages = client.messages.create(
        body=body,
        from_='+17733210345',
        to=number
    )
