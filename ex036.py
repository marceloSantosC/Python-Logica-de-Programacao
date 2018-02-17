v = float(input('Qual o valor da casa ? R$'))
s = float(input('Qual o seu salario atual ? R$'))
t = int(input('Em quantos anos você ira pagar o emprestimo ?'))
e = s*30/100
pm = v/t
if pm > e:
    print('Seu emprestimo foi negado!')
else:
    print('Seu emprestimo foi aprovado.Você pagara R${} mensais durante {} anos'.format(pm, t))





