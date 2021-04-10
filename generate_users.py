from faker import Faker

fake = Faker('pt_BR')

list_users = []

for i in range(100):
    first_name = fake.first_name()
    first_name = first_name.split(" ")[0]  # elimina nomes compostos
    last_name = fake.last_name()

    username = f"{first_name}_{last_name}".lower()
    email = f"{first_name}_{last_name}@gmail.com".lower()
    password = f"{first_name[0:3]}{fake.password()}"

    user = {
        'username': username,
        'email': email,
        'password': password
    }

    list_users.append(user)
