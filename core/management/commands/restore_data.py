from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Restore core app data from JSON fixture"

    def handle(self, *args, **options):
        call_command(
            "loaddata",
            "core_data.json"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Core data restored successfully."
            )
        )