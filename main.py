cadena1 = '__servidor1'
cadena2 = '3servidor'

def AFD (cadena):
    s = 0
    pertenece1 = False
    pertenece2 = False
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for i in range(len(cadena)):

        if (s == 0):
            if (cadena[i]=='_'):
                s = 1
            else: 
                for j in range(len(letras)):
                    if (cadena[i]==letras[j]): 
                        pertenece1 = True 
                        break
                    else: 
                        pertenece1 = False

                if pertenece1==True: 
                    s = 2 
                else:
                    print("'"+cadena+"' no pertenece")
                    return

        elif (s == 1):
            if (cadena[i]=='_'):  
                s = 1  
            else:
                for j in range(len(letras)):
                    if (cadena[i]==letras[j]):
                        pertenece1= True
                        break
                    else: 
                        pertenece1 = False

                if (pertenece1==True):
                    s = 3
                else: 
                    print("'"+cadena+"' no pertenece")
                    return

        elif (s == 2):
            if (cadena[i]=='_'):
                print("'"+cadena+"' no pertenece") 
                return
            else: 
                for j in range(len(letras)):
                    if (cadena[i]==letras[j]):
                        pertenece1 = True
                        break
                    else: 
                        pertenece1 = False
                        
                for m in range(len(numeros)):
                    if(cadena[i]==numeros[m]): 
                        pertenece2 = True
                        break
                    else: 
                        pertenece2 = False 

                if (pertenece1 == True):
                    s = 2
                elif (pertenece2==True):
                    s = 4 
                    return     

        elif (s == 3):
            if (cadena[i]=='_'):
                print("'"+cadena+"' no pertenece") 
                return
            else: 
                for j in range(len(letras)):
                    if (cadena[i]==letras[j]):
                        pertenece1 = True
                        break
                    else:
                        pertenece1 = False

                for m in range(len(numeros)):
                    if(cadena[i]==numeros[m]):
                        pertenece2 = True
                        break
                    else: 
                        pertenece2 = False

                if pertenece1== True:
                    s = 3
                elif pertenece2 == True: 
                    s = 4 
                else: 
                    print("'"+cadena+"' no pertenece")
                    return              

    print("'"+cadena+"' pertenece")
            
AFD(cadena1) 
AFD(cadena2)