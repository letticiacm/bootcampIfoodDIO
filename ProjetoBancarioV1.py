#Montando o menu
menu = """
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [4] Sair

  =>"""

#Variáveis que precisam ser inicializadas
saldo = 0
limite = 500
extrato = "\n**********  EXTRATO  **********\n"
#print(len(extrato))
QdeDeSaques = 0
opcao = 0

#Loop para manter o menu ativo enquanto usuário não digitar a opção 4 (SAIR)
while opcao != 4 :
   
   opcao = int(input(menu))
   #Se opção escolhida for Depositar. Será verificado se o valor é válido ou seja, maior que zero
   if opcao == 1:
      valorDeposito = float(input("\nInforme o Valor a ser Depositado:"))
      if valorDeposito > 0:
         extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
         saldo += valorDeposito
         print("\nDepósito Realizado com Sucesso...")
      else:
         print ("\nValor Inválido!")
   
    #Opção para Sacar. Será verificado se o usuário já realizou os 3 saques permitidos
    #Se o valor a sacar é superior ou igual a R$500.0 e se o valor do saque é inferior
    # ou igual ao saldo
   elif opcao == 2:

      if (QdeDeSaques < 3):
          valorSaque = float(input("\nInforme o Valor do Saque:"))      
          if (valorSaque <= saldo):
             if (valorSaque <= 500.0):            
                saldo -= valorSaque
                extrato += f"Saque:    R$ {valorSaque:.2f}\n"
                QdeDeSaques += 1
                print("\nSaque Realizado com Sucesso...")
             else:
                print("\nValor max. do Saque: R$ 500.0!")
          else:
             print("\nSaldo Insuficiente!") 
      else:
          print("\nLimite diário de Saque excedido!") 

    #Opção para visualizar o Extrato
    #Ele primeiro irá contar o tamanho da variável extrato p saber se 
    # já foi realizado alguma operação como depósito ou saque
    # se não houver, exibirá mensagem informando que ainda não há movimentação    
   elif opcao == 3:

      print(extrato)

      if int(len(extrato)) == 33:          
          print("\nNão há movimentações\n")     

      imprimeSaldo = f"Saldo: R${saldo:.2f}"
      print(imprimeSaldo)
      print("\n*********************************")      
   elif opcao == 4:
      break
   else:
      print("Opção inválida!")   

      
      
          
   
         


