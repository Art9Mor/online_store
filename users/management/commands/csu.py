from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@os.ky',
            first_name='admin',
            last_name='admin',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password('666')
        user.save()
