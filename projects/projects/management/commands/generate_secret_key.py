from django.core.management.base import BaseCommand, CommandError
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = 'Generate `DJANGO_SECRET_KEY` for other environments'

    def handle(self, *args, **options):
        TERMINAL_BLUE = '\033[94m'

        secret_key = get_random_secret_key()

        print(f'{TERMINAL_BLUE}Generated secret key: {secret_key}')
