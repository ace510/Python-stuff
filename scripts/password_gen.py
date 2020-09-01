import string
import secrets

alphabet = string.ascii_letters + string.digits

password = "".join(secrets.choice(alphabet) for i in range(20))


# print(secrets.token_urlsafe(14))

print(secrets.randbelow(10000))
