#match statement is used to perform different actions based on different conditions
#insted of many if-else statements you can use the match statement
#example
day=3
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
#default value-'-' 
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
#combine values--|
day=5
match day:
   case 1|2|3|4|5:
      print("Today is a weekday")
   case 6|7:
      print("I love weekends!")


