def tuple_to_dict(test_tup):
  return dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))
