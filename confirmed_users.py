unconfirmed_users = ["sonic", "amy", "knuckles"]
confirmed_users = []

for unconfirmed_user in unconfirmed_users:
    print(f"Verifying user: {unconfirmed_user.title()}")
    confirmed_users.append(unconfirmed_user)
    unconfirmed_users.remove(unconfirmed_user)

print("\nThe following users hath been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())