from apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/loginUser", views.login, ["POST"],
        "Login Api to Authenticate User and Make Login"),
    ("/createUser", views.create, ["POST"],
        "Login Create a User to User Collection and so that user can Login"),
    ("/search", views.search, ["GET"],
        "Search api to search by Name and phoneNo by passing it as a \
            queryString"),
    ("/view", views.view, ["GET"],
        "View Api to view User Profile contains all data of user"),
    ("/addSpam", views.addSpam, ["GET"],
        "addSpam Api add phoneNo in spam collection and if \
            same phoneNo is added it increment the count of it")
]

other_urls = []

all_urls = api_urls + other_urls
