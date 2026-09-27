from django.core.management.base import BaseCommand
from django.core.management import call_command
from pathlib import Path


class Command(BaseCommand):
    help = "Backup core app data to JSON fixture"

    def handle(self, *args, **options):
        fixture_dir = Path("core/fixtures")
        fixture_dir.mkdir(parents=True, exist_ok=True)

        output_file = fixture_dir / "core_data.json"

        with open(output_file, "w", encoding="utf-8") as file:
            call_command(
                "dumpdata",
                "core",
                indent=2,
                stdout=file
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Backup created successfully: {output_file}"
            )
        )