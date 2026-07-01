from app.core.security import create_access_token

token = create_access_token(
    {"sub": "antaryami@example.com"}
)

print(token)