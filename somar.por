programa {
    funcao inicio () {
        inteiro numero, i, soma

        soma = 0

        escreva("Digite um número")
        leia(numero)

        para (i = 1; i <= numero; i++)
        {
            soma = soma + 1
        }

        escreva("Soma = ", soma)
    }
}