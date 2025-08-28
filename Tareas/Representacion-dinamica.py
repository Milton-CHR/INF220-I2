#Representacion dinamica
transacciones=[]
def depositar(monto):
    transacciones.append({"tipo":"deposito", "monto": monto})

def retirar(monto):
    transacciones.append({"tipo":"retiro", "monto": monto})

def ver_historial():
    for movimiento in transacciones:
        print(movimiento["tipo"], "de", movimiento["monto"])

def saldo_actual():
    saldo=0
    for movimiento in transacciones:
        if movimiento["tipo"]=="deposito":
            saldo=saldo+movimiento["monto"]
        else:
            saldo=saldo-movimiento["monto"]
    return saldo

#prueba
depositar(1000)
retirar(200)
depositar(300)

print("HISTORIAL:")
ver_historial()

print("Saldo final:", saldo_actual())
