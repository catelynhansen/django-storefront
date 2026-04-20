from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from store.models import Collection

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Running seed...")

        # 1. ONLY create superuser if missing
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@domain.com",
                password="1234"
            )
            self.stdout.write("Superuser created")
        else:
            self.stdout.write("Superuser already exists")

        # 2. ONLY seed data if needed
        if not Collection.objects.exists():
            self.stdout.write("Seeding collections/products...")
            # run SQL or ORM seeding here
        else:
            self.stdout.write("Data already exists, skipping seed")