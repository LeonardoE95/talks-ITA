from faker import Faker
import hashlib

fake = Faker()
m = hashlib.sha1()
n = 100

print(f"name,email,password")
for _ in range(100):
    name = fake.name()
    email = fake.email()
    password = fake.password()
    m.update(password.encode())
    password = m.hexdigest()

    print(f"{name},{email},{password}")
