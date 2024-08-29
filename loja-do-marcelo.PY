print('==========LOJA DO MARCELO==========')

preço = float(input('Digite o valor das compras R$: '))

print('FORMAS DE PAGAMENTO:')
print("""
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
      """)
opc = int(input('Digite a opção desejada: '))

if opc == 1:
    print(f'Sua compra será a vista no dinheiro no valor de R${preço - (preço * 0.1)}!')
elif opc == 2:
    print(f'Sua compra será a vista no cartão no valor de R${preço - (preço*0.05)}!')
elif opc == 3:
    print(f'Sua compra será parcelada em 2x no cartão no valor de R${preço/2} cada parcela!')
elif opc == 4:
    parcelas = int(input('Digite em quantas vezes você quer parcelar: '))
    vf = (preço + preço*0.2)/parcelas 
    print(f'Sua compra será parcelada em {parcelas}x no cartão no valor de R${vf} cada parcela com JUROS!')
else:
    print('Opção invalida!')