from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from User.models import UserProfile,Institution,TitleModel
import random
fake = Faker()

class Command(BaseCommand):
    help = "Generate users"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of users to create")

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            username = fake.user_name()
            email = fake.email()
            password = "default_password123"
            first_name = fake.first_name()
            last_name = fake.last_name()
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'password': password,
                    'first_name': first_name,
                    'last_name': last_name,
                }
            )

            if created:  
                institution = Institution.objects.order_by('?').first()
                title = TitleModel.objects.order_by('?').first()
                UserProfile.objects.filter(
                    user=user
                ).update(
                    is_active=True,
                    is_verified=True,
                    bio=fake.text(max_nb_chars=200),
                    contact_email=email,
                    title=title,
                    institution=institution
                )

                self.stdout.write(self.style.SUCCESS(f"Kullanıcı ve profil oluşturuldu: {username}"))
            else:
                self.stdout.write(self.style.WARNING(f"Kullanıcı zaten mevcut: {username}"))
