import bcrypt as bcrypt
from faker import Faker

fake = Faker('fr_FR')


def generer_fake():
    password = str.encode(fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True), 'utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    fiche = {
        "fullName": fake.name(),
        "birthday": fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=65),
        "isActive": fake.boolean(chance_of_getting_true=95),
        "email": fake.email(),
        "password": hashed,
    }
    return fiche


for _ in range(10):
    print(generer_fake())
