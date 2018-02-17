sexo = input('Sexo(M/F): ').strip()[0]
while sexo not in 'fFmM':  #   enquanto o while nao estiver correto o programa não ira prosseguir
    sexo = input('Sexo invalido ! Por favor digite novamente :')
print('Sexo {} registrado com sucesso ! '.format(sexo))
