# This is a test commit
def add(a, b):
  return a + b

def test_add(a, b):
  assert add(1, 2) == 3
  assert add(1, -1) == 0