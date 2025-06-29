from django.core.management.base import BaseCommand
from kudos_app.models import Organization, User, Kudos
from django.utils import timezone
import random

MESSAGES = [
    "Great teamwork!", "Awesome job!", "Thanks for your help!", "You rock!", "Fantastic effort!",
    "Impressive work!", "Super helpful!", "Much appreciated!", "Outstanding!", "Brilliant solution!"
]

class Command(BaseCommand):
    help = 'Generate demo data for kudos app'

    def handle(self, *args, **kwargs):
        # Clear old data
        Kudos.objects.all().delete()
        User.objects.all().delete()
        Organization.objects.all().delete()

        # Create organizations
        orgs = [Organization.objects.create(name=f"Org {i+1}") for i in range(2)]

        # Create users
        users = []
        for org in orgs:
            for i in range(5):
                user = User.objects.create_user(
                    username=f"user_{org.id}_{i+1}",
                    password="password",
                    organization=org
                )
                users.append(user)

        # Create random kudos
        for _ in range(20):
            giver, receiver = random.sample(users, 2)
            if giver.organization == receiver.organization:
                Kudos.objects.create(
                    giver=giver,
                    receiver=receiver,
                    message=random.choice(MESSAGES),
                    created_at=timezone.now() - timezone.timedelta(days=random.randint(0, 30))
                )

        self.stdout.write(self.style.SUCCESS('Demo data generated!'))