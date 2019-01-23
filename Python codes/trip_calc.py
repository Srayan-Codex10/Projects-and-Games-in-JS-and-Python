def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == 'Charlotte':
    return 183
  elif city == 'Tampa':
    return 220
  elif city == 'Pittsburgh':
    return 222
  elif city == 'Los Angeles':
    return 475
  else:
    return 'Enter a the correct city'
  
def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  else:
    print("No discount !!")
  return cost

def trip_cost(city,days,spending_money):
  return spending_money + rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city)


print ("The total cost for the trip is: %d$"%(trip_cost('Los Angeles',5,600)))