print("\t\t\t Trust Fund Buddy\n")
print("Totals your monthly spending so that your trust fund doesn't run out")
print("(and you're forced to get a real job).\n")
print("Please enter the requested, monthly costs. Sinec you're rich, ignore pennies and use only dollar amounts.\n\n")

car = input("Lamborghini Tune-Ups: ")
car = int(car)

apart = input("Manhattan Apartment: ")
apart = int(apart)

rent = input("Private Jet Rental: ")
rent = int(rent)

gift = input("Gifts: ")
gift = int(gift)

out = input("Dinning Out: ")
out = int(out)

staff = input("Staff <butlers, chef, driver, assistant>: ")
staff = int(staff)

coach = input("Personal Guru and Coach: ")
coach = int(coach)

game = input("Computer Games: ")
game = int(game)

print("\n\nGrand Total: ", car+apart+rent+gift+out+staff+coach+game)
