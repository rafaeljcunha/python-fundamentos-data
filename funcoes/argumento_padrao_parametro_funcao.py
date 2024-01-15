def funcao(x, y=50):
  """Um argumento padrão é um parâmetro que assume um valor padrão se um valor não for fornecido na chamada da função"""
  print("x: ", x)
  print("y: ", y)
funcao(10)
print("-------")
funcao(10, 20)