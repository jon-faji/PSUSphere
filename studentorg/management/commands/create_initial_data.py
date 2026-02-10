from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import *
import random

class Command(BaseCommand):
    help = "Load fake data for PSUSphere"

    def handle(self, *args, **kwargs):
        fake = Faker("en_PH")  # Filipino style names and companies

        # Colleges
        colleges = [College.objects.create(college_name=fake.company()) for _ in range(5)]

        # Programs
        programs = [
            Program.objects.create(prog_name=fake.job(), college=random.choice(colleges))
            for _ in range(10)
        ]

        # Students
        students = [
            Student.objects.create(
                student_id=f"{fake.year()}-{fake.random_int(1,8)}-{fake.random_number(4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=random.choice(programs)
            ) for _ in range(20)
        ]

        # Org Members
        organizations = [
            Organization.objects.create(
                name=fake.company(),
                college=random.choice(colleges),
                description=fake.sentence()
            ) for _ in range(5)
        ]

        for student in students:
            OrgMember.objects.create(
                student=student,
                organization=random.choice(organizations),
                date_joined=fake.date_between(start_date="-2y", end_date="today")
            )

        self.stdout.write(self.style.SUCCESS("PSUSphere fake data loaded"))
