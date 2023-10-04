'''
Autor: Alexandre Borgmann
Data: 07/04/2020
URI Online Judge | 2483 Feliz Nataaal!

Você fica tão feliz no natal que tem vontade de gritar para todo mundo: "Feliz natal!!".
Pra colocar toda essa felicidade pra fora, você montou um programa que, colocado um índice I de felicidade, seu grito de natal é mais animado.
Entrada
A entrada é composta por um inteiro I (1 < I ≤ 104) que representa o índice de felicidade.
Saída
A saída é composta pela frase "Feliz natal!", sendo repetidas I vezes a última letra a da frase.
Uma quebra de linha é necessária após a impressão da frase.

Exemplo de Entrada
5
Exemplo de Saída
Feliz nataaaaal!
'''
while True:
    n = int(input())
    if(n<0 or n>10000):
        print("Digite (1 < I ≤ 104) ")
        continue
    break
print("Feliz nata"+"a"*(n-1)+"l!")