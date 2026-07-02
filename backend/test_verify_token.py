from app.core.security import (
    create_access_token,
    verify_access_token
)

token = create_access_token(
    {"sub": "antaryami@example.com"}
)

print("Token:")
print(token)

print("\nDecoded Email:")
print(verify_access_token(token))