from django.core.management import BaseCommand, call_command
from psycopg2 import ProgrammingError, IntegrityError

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        fixtures_path = 'catalog_data.json'

        Category.objects.all().delete()
        Category.truncate_table_restart_id()

        try:
            call_command('loaddata', fixtures_path)
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(f'Invalid fixture: {e}', self.style.NOTICE)
        else:
            self.stdout.write('Command have been completed successfully', self.style.SUCCESS)
