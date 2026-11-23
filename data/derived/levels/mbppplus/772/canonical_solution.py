def remove_length(test_str, K):
  return ' '.join([i for i in test_str.split() if len(i) != K])
