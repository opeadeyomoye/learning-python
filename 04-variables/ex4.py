# breathing space...

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = cars - cars_not_driven # or just drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

passengers_driveable = (cars_driven * space_in_a_car) - drivers


print "There are", cars , "cars available"; print
print "A car can take", space_in_a_car , "passengers"
print "There are only", drivers ,"drivers available"
print "There will be", cars_not_driven ,"empty cars today"
print "We can transport", carpool_capacity , "people today"
print "We have", passengers ,"people to carpool today"
print "We need to put about", average_passengers_per_car ,"people in each car"
