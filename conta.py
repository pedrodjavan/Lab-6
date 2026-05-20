class Conta():
  def __init__(self, saldo):
    self.saldo = saldo

  def saca(self, valor):
    if valor <= self.saldo:
      self.saldo -= valor
      print(f"Saque de R${valor:.2f} realizado.")
    else:
      print("Saldo insuficiente.")

      
  def deposita(self, valor):
      self.saldo += valor
      print(f"Deposito de R${valor:.2f} realizado.")

  def rendimento(self, valor):
    
    
    















