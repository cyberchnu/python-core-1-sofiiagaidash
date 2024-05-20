def fizz_buzz(param):
  if param % 5 == 0 and param % 3 == 0:
    return "FizzBuzz"
  if param % 5 == 0:
    return "Buzz"
  if param % 3 == 0:
    return "Fizz"
