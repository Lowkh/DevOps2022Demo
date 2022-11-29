import pytest
import helloworld

def test_testOne():
  result = helloworld()
  assert result == "hello world!"
