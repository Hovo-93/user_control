from faker import Faker
from .models import User

fake = Faker(['ru_RU'])


def generate_user_fake_data(count):
    for _ in range(count):
        users = User.objects.create(
            username=fake.name(),
            email=fake.email(),
        )
        users.save()