def count_reverse_pairs(test_list):
  return sum(test_list[i+1:].count(s[::-1]) for i, s in enumerate(test_list))
