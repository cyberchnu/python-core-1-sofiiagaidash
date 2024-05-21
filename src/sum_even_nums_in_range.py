def sum_even_nums_in_range(start, stop):
  a = 0
  for num in range(start,stop+1):
    if num % 2 == 0:
      a += num
  return a
