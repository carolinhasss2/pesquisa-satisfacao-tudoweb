Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

... # Pesquisa de Satisfação - TudoWeb
... 
... excelente = 0
... bom = 0
... ruim = 0
... 
... print("PESQUISA DE SATISFAÇÃO - TUDOWEB")
... 
... for i in range(1, 51):
...     print("\nEntrevistado", i)
... 
...     nome = input("Digite seu nome: ")
...     idade = int(input("Digite sua idade: "))
... 
...     print("\nOPINIÃO SOBRE O ATENDIMENTO")
...     print("1 - EXCELENTE")
...     print("2 - BOM")
...     print("3 - RUIM")
... 
...     opiniao = int(input("Digite sua opção: "))
... 
...     if opiniao == 1:
...         print("Resposta: EXCELENTE")
...         excelente += 1
... 
...     elif opiniao == 2:
...         print("Resposta: BOM")
...         bom += 1
... 
...     elif opiniao == 3:
...         print("Resposta: RUIM")
...         ruim += 1
... 
...     else:
...         print("Opção inválida!")
... 
... print("\n===== RESULTADO FINAL =====")
... print("Respostas EXCELENTE:", excelente)
... print("Respostas RUIM:", ruim)
