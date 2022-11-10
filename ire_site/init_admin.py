import os
from django.contrib.auth import get_user_model


username = os.getenv('ADMIN_LOGIN')
email = os.getenv('ADMIN_EMAIL')
password = os.getenv('ADMIN_PASS')

User = get_user_model()
if not User.objects.filter(username=username).exists():
    print('Creating account for %s (%s)' % (username, email))
    User.objects.create_superuser(
        email=email, username=username, password=password)
else:
    print('Admin account has already been initialized.')
