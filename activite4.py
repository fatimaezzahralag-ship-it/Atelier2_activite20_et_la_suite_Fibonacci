
with open ("la table de multiplication.txt","w") as file:
    file.write("la table de multiplication des nombre de 1 jusqu'a 10 : \n")
    
    for i in range(1,11):
        file.write(f"table de multiplication de {i} \n")
        for j in range(1,11):
            
            file.write(f"{i}*{j}={i*j}\n")
            
        file.write("\n")
    file.close()