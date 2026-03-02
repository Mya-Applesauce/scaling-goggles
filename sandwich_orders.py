sandwich_orders = ["grilled cheese", "pastrami", "pastrami", "pastrami", "pb&j", "hoagie", "italian", "squid eyeball", "hotdog", "ham on rye", "meatball sub"]
finished_sandwiches = []

print("Alas! This deli hast runneth oute of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

for sandwich in sandwich_orders:
    print(f"We art workinge on thy {sandwich} sandwich now.")
    finished_sandwiches.append(sandwich)

print("These are the sandwiches beinge served to thee: ", end="")
for sandwiches in finished_sandwiches:
    print(f"{sandwiches}, ", end="")
