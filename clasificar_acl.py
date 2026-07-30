numero_acl = int(input("Ingrese el numero de ACL IPv4: "))
if 1 <= numero_acl <= 99 or 1300 <= numero_acl <= 1999: 
 print("La ACL ingresada corresponde a una ACL IPv4 estandar.") 
elif 100 <= numero_acl <= 199 or 2000 <= numero_acl <= 2699: 
 print("La ACL ingresada corresponde a una ACL IPv4 extendida.") 
else: print("El numero ingresado no corresponde a una lista de acceso IPv4 valida.")
