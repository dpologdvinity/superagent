def test_three_equal(x,y,z):
  result = set([x,y,z])
  if len(result) == 3:
    return 0
  elif len(result) == 2:
    return 2
  else:
    return 3
