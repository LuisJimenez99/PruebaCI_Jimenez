# test_app.py
from app import suma

def test_suma():
  """
  Prueba que la función suma funcione correctamente.
  """
  assert suma(2, 3) == 5
  assert suma(-1, 1) == 0