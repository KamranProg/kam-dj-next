import os
import time
import psycopg2
from psycopg2 import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Waits for the database to become available before running further commands."

    def handle(self, *args, **options):
        retries = int(os.environ.get("DB_WAIT_RETRIES") or 30)
        delay = float(os.environ.get("DB_WAIT_DELAY") or 2.0)

        self.stdout.write(f"Waiting for Postgres (retries: {retries}, delay: {delay}s)...")

        for attempt in range(retries):
            try:
                conn = psycopg2.connect(
                    dbname=os.environ["POSTGRES_DB"],
                    user=os.environ["POSTGRES_USER"],
                    password=os.environ["POSTGRES_PASSWORD"],
                    host=os.environ["POSTGRES_HOST"],
                    port=os.environ["POSTGRES_PORT"],
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS("Postgres is available!"))
                return
            except OperationalError:
                self.stdout.write(f"Attempt {attempt + 1}/{retries}: Postgres unavailable, waiting {delay}s...")
                time.sleep(delay)

        raise Exception("Postgres not available after multiple retries.")
