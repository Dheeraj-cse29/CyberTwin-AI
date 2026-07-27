from app.core.security import hash_password, verify_password

password = "CyberTwin123"

hashed = hash_password(password)

print("Original :", password)
print("Hashed   :", hashed)

print(
    verify_password(
        "CyberTwin123",
        hashed
    )
)