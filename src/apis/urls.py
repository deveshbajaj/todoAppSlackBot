from apis import views


api_urls = [
    ("/addTodo", views.addTodo, ["POST"],
        "add todo item in list"),
    ("/removeTodo", views.removeTodo, ["POST"],
        "remove todo item from list"),
    ("/listAll", views.listAll, ["POST"],
        "List all to do for a a channel")
]

other_urls = []

all_urls = api_urls + other_urls
