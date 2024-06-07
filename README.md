Este projeto foi desenvolvido por:

Gabriel Machado Lacerda                RM:556714   

João Pedro Signor Avelar               RM:558375

Roger Cardoso Ferreira                 RM:557230

Vinicius Augusto Siqueira Gonçalves    RM:557065

TURMA:1ESPW

Jogo da Memória da Fórmula E
Bem-vindo ao jogo da memória da Fórmula E! Este é um jogo simples onde o objetivo é encontrar todos os pares correspondentes de cartas. As cartas representam equipes da Fórmula E, e você deve lembrar suas posições para encontrar todos os pares.

Funcionalidades
Verificação de entradas numéricas.
Verificação de valores entre 1 e 4 para garantir que as escolhas estejam dentro do tabuleiro.
Impressão da tabela do jogo mostrando as cartas descobertas.
Lógica para verificar se um par correspondente foi encontrado.
Opção de reiniciar o jogo após encontrar todos os pares.

Requisitos
Para executar o jogo, você precisa de:
Python 3.x instalado no seu sistema.
Um terminal ou ambiente de desenvolvimento que permita a execução de scripts Python.

Instruções de Uso
1. Clone o repositório ou copie o código para um arquivo Python (.py) no seu computador.
2. Abra um terminal ou um ambiente de desenvolvimento Python.
3. Navegue até o diretório onde o arquivo .py está localizado.
4. Execute o arquivo com o comando: python nome_do_arquivo.py
5. Siga as instruções que aparecerão na tela para jogar o jogo.

Dependências
Este projeto não possui dependências externas. Todo o código é executado com bibliotecas padrão do Python.

Informações Adicionais
Estrutura do Código
O código está estruturado da seguinte forma:
Função verificaValorNumerico(msg): Verifica se a entrada do usuário é numérica.
Função verificaValorCerto(num, msg): Verifica se a entrada do usuário está entre 1 e 4.
Função imprimirTabela(cartas_descobertas): Imprime a tabela do jogo com as cartas descobertas.
Função inicioDoJogo(): Controla o fluxo principal do jogo.
Função verificarCarta(linha, coluna): Devolve o valor da carta com base na linha e coluna.
Função verificaIndice(lista, elemento): Verifica se um elemento está presente em uma lista.
Função forcaOpcao(lista, msg): Obriga o usuário a escolher uma opção presente em uma lista.

Regras do Jogo
1. Você será solicitado a escolher a linha e a coluna da primeira carta.
2. Em seguida, será solicitado a escolher a linha e a coluna da segunda carta.
3. Se as cartas formarem um par, elas permanecerão viradas para cima.
4. Se as cartas não formarem um par, elas serão viradas novamente para baixo.
5. O jogo termina quando todos os pares forem encontrados.
6. Após encontrar todos os pares, você terá a opção de jogar novamente ou encerrar o jogo.

Esperamos que você se divirta jogando o Jogo da Memória da Fórmula E! Se encontrar algum problema ou tiver sugestões, sinta-se à vontade para entrar em contato.

