from apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/login", views.login, ["POST"], "Login Api to Authenticate User and Make Login"),
    ("/create", views.create, ["POST"], "Login Api to Authenticate User and Make Login")
]

other_urls = []

all_urls = api_urls + other_urls
