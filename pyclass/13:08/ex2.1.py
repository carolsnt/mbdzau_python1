# -*- coding: utf-8 -*-
from __future__ import division

#Exercício 2.1
# ⁠Converta as seguintes expressões matemáticas para que possam ser calculadas usando o interpretador Python.
# a = 10 + 20 × 30
# b = 4² ÷ 30
# c = (9⁴ + 2) × 6-1

a = 10 + 20 * 30
b = 4 ** 2 / 30
c = (9 ** 4 + 2) * 6 - 1

print (a)
print (b)
print (c)

x = 5.234123654
#novo, aqui estou pedindo depois do ponto que quero apenas 2 casas decimais
print (f'{x:.2}')
#antigo, aqui estou pedindo depois do ponto que quero apenas 2 casas decimais
print ('{:.2}'.format(x))
#no livro vemos essa terceira forma, o f é de formatação, e o %f é de float, ou seja, número decimal. O .2 é de duas casas decimais.
print ('%f' % x)
print ('%.2f' % x)