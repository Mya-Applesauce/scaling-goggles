sandwich_orders = ["grilled cheese", "pb&j", "hoagie", "italian", "squid eyeball", "hotdog", "ham on rye", "meatball sub"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"Thy {sandwich} sandwich 'tis served.")
    finished_sandwiches.append(sandwich)

for sandwiches in finished_sandwiches:
    print(f"{sandwiches}, ", end="")
