soldado = input("Qual seu QRA?")
matricula = float (input("Qual a sua matricula?"))
horario = float(input("Qual o horário do seu turno?"))
entrada = float(input("Digite o horário da primeira honda:"))
ronda = 4.0
proxima_ronda = 0
continua = 'sim' 
contador =0
while 'sim':
    print(f"As hondas de celas são feitas de 4 em 4 horas {soldado} portador da matricula: {matricula}")
#logo a cima dfinimos as variaveis, a baixo de agora em diante vai ser os comandos logicos para definir os horarios.
   

    if continua=='sim':
       
        entrada = (ronda) + (entrada)
        print ("o horario da proxima ronda é ", entrada)

    continua=str(input("digite sim ou não para continuar no sistema "))


    
    
   
 
    
    

    







