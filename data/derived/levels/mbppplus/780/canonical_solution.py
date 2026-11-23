from itertools import combinations 
def find_combinations(test_list):
  return [tuple(map(sum, zip(*t))) for t in combinations(test_list, 2)]
