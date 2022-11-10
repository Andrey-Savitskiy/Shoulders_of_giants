import os
from django.contrib.auth import get_user_model


User = get_user_model()
User.objects.create_superuser(os.getenv('ADMIN_LOGIN'), os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASS'))