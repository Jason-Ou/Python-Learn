#There are 100 cars.
cars = 100
#There are 4 space each car.
space_in_a_car = 4
#there are 30 drivers.
drivers = 30
#There are 90 passengers.
passengers = 90
#There are 70 cars empty.
cars_not_driven = cars - drivers
#There are 30 cars could be drivern.
cars_driven = drivers
#So 120 seats here.
carpool_capacity = cars_driven * space_in_a_car
#3 seats each car will be used.
average_passengers_per_car = passengers / cars_driven

print "There are",cars,"cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty car today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
