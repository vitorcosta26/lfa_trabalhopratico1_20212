# lfa_trabalhopratico1_20212

- Trabalho prático da matéria de LFA - Linguagens formais e autômatos , ministrada pelo professor Adolfo Guimarães

## Integrantes

- Johnny William Severo Dantas Costa
- Paulo Vitor Costa Melo

## Abreviações e termos
- AFD > Autômato Finito  Determinístico
- AFND > Autômato Finito Não Determinístico
- AFNDε > Autômato Finito Não Determinístico com Transição Vazia

# Tutorial de como utilizar o algoritmo

Após executar o código será exibido 4 opções:

- Cadastrar autômato

- Imprimir autômato

- Testar palavra

- Finalizar programa

### 1 - Cadastrar autômato
Nesta opção você poderá digitar o nome do arquivo sem a extensão “.txt” para cadastrar o autômato desejado no algoritmo, após cadastrado você estará pronto para utilizaras próximas opções.
### 2 - Imprimir autômato
Aqui como o próprio nome diz ele fará a impressão do autômato e também se o autômato for AFND  o algoritmo fará a transformação para AFD automática, e logo em seguida a impressão do mesmo.
### 3 - Testar palavra
Esta opção será para o testamento de palavras para o autômato cadastrado. Estando nela somente será necessário digitar qual palavra você deseja testar e ele irá retornar uma das opções abaixo:
 - A palavra " " não pode ser testada, pois seus símbolos não fazem parte do alfabeto definido
 - A palavra " " foi aceita
 - A palavra " " foi rejeitada  

No caso do teste de uma palavra AFNDε terá duas formas de valida-la:  
 - Passando "" como parâmetro 
 - Digitando nada no console 
### 4 - Finalizar programa
Selecionando essa opção o programa será encerrado.
