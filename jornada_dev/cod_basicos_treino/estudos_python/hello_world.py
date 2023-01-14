print("\tHello World!")

print("\tOk, me livrei da maldição...")

print("\nAgora vou explorar possíveis erros que eu possa causar na sintaxe, tanto de forma a forçar o terminal a me retornar o erro, como um possível erro sem retorno. Seria isso possível?")

print ("\nLinha 07: Teoricamente esta linha poderia me retornar um erro, porém, isto não ocorre. A linha foi escrita com um espaço entre o comando print e o () que recebem o valor a ser retornado.")

print("\nEm um breve brainstorm do que eu poderia projetar com python, utilizando a base de conhecimento do que acredito ser viável criar com esta linguagem, traço como meta que meu primeiro programa seja uma automação de consultade status de um ativo de rede, neste caso impressoras, utilizando como base um arquivo .bat previamente criado por mim.")

print("\nPara poder manter o programa de impressão mais agradável aos olhos, foram adicionadas entre as linhas de impressão o comando 'print("")' vazio, fazendo com que quando o python fizer a leitura, uma linha vazia seja adicionada entre cada um dos textos.")

print("\nConforme informei acima, estava utilizando o comando de impressão vazio para criar espaços entre as mensagens, porém, agora todos esses comandos de impressão estão sendo removidos, para que o texto seja formatado utilizando tabulações e quebras de linha.")

print("\nAlteração realizada no VSCode, realizando commit.")

print("\n\tIniciando a utilização de variáveis. A próxima mensagem impressa nesse programa será declarada na variável 'first_message'e impressa na tela.")

first_message = "\nEsta mensagem está atribuída a uma variável. Variáveis podem receber novos valores no decorrer das linhas do programa."

print(first_message)

name_rules_var = "\nRegras para nomeação de variáveis: 1 - Espaços não são permitidos, mas podemos usar underscores para simular a separação entre palavras '_'. 2 - Evitar usar palavras reservadas como 'print' por exemplo. 3 - Usar nomes concisos, porém descritivos. Não ao invés de 'nm' por exemplo, usar 'nome'. 4 - Quando possível evitar o uso de 'L minúsculo' ou 'O e o' que podem ser confundidos com 1 e 0 respectivamente. 5 - É possível utilizar letras maiúsculas em variáveis no python, mas não aconselhado no início...espero descobrir porque. "

print(name_rules_var)

var_change = "\nA variável 'var_change' recebe o valor que está sendo impresso nesse momento, porém, mais a frente ele será alterado e re-impresso."

print(var_change)

var_change = "\nA partir deste momento, esse é o novo valor desta variável, podendo ser mudado novamente quando programado. Assim ocorre com as variáveis conforme elas recebem novos valores."

print(var_change)

print("\n\t--Strings são tipos de dados.Tudo que estiver entre aspas é considerado uma String em python. Agora farei algumas alterações em strings, como por exemplo, alterar o tipo de leitura, onde os valores recebidos se comportarão com escrita de Nomes, Títulos, em letras Maiúsculas ou integralmente Minúsculas")

print("\nO método '.title()', por exemplo, aparecendo na escrita após a variável no print; print(name.title()), fará com que a formatação de impressão saia com letras iniciais maiúsculas, mesmo sendo inseridas em letras minúsculas.")

name = "\ntarsis m. s. martins"

print(name.title())

print("\nNa sequência, serão declaradas duas novas variáveis; nameup e namelo, que receberão os métodos .upper() e .lower(), respectivamente, fazendo com que elas imprimam em maiúsculo e minúsculo independente da forma que foi dada entrada no valor. Armazenar dados em letras minúsculas pode ser muito útil.")

nameup = "\nTaRSis M. s. martins"

namelo = "\nTARSIS m. S. mArTiNs"

print(nameup.upper())

print(namelo.lower())

print("\n\t--Combinando/Concatenando Strings. Pode ser valioso juntar mais de uma String para criar um valor desejado sem solicitar diretamente todas as informações em apenas um campo.")

first_name = "tarsis"

last_name = "martins"

full_name = first_name + " " + last_name

print("\nHello, " + full_name.title() + "!")

print("\nNesse caso, na mensagem acima, foi criado o comando print, seguindo de uma mensagem formatada, combinada a variável full_name, formatada pelo método '.title()', combinada a mais uma mensagem de texto ao final.")

message_greeting = "\nHello, " + full_name.title() + "!"

print(message_greeting)

print("\nNa mensagem acima, o valor foi atribuído à variável 'message_greeting', facilitando a impressão em qualquer momento, pois basta chamar o print desta, ao invés de recriar toda a mensagem.")

print("\n\t--O Traceback retornado na linha N diz que na linha N, no módulo executado pelo console diz que a sintaxe 'Print' não está definida, re completa com uma sugestão, se o correto não seria 'print'.")

print("")

Print("Linha N: Este comando retornará um erro, pois na sintaxe em python, não devem existir letras maiúsculas.")
