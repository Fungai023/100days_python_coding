travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

#printing Berlin
print("Example one answer : " + travel_log["Germany"][1])

#Nested dictionary question
travel_logs = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print("Example 2 answer : " + travel_logs["Germany"]["cities_visited"][2])