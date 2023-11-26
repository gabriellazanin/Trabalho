# README Trabalho ADC 

Este README documenta as etapas necessárias para colocar seu aplicativo em funcionamento.

### Para que serve este repositório?

* Resumo rápido...
* Versão...
* [Sintaxe básica de gravação e formatação no GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

### Como faço para configurar?

* Resumo da configuração...
* Configuração...
* Dependências

    Para criar um ambiente virtual

    ```
    $ python -m venv .venv
	```
	
	Depois, é necessário ativar o ambiente virtual
	
	```
    $ .venv\Scripts\activate
    ```

    e depois instalar as livrarias necessárias

    ```
    $ pip install -r requirements.txt
    ```

* Pretendemos usar um postgres no futuro para guardar as fatura e dados dos clientes.
* Precisamos de contribuição para testes com pytest neste projeto.

#### Documentação

Para gerar a configuração para o sphinx, crie uma pasta com o nome `doc`, e mude para essa pasta

```
$ mkdir doc
$ cd doc
```

e depois escreva o comando abaixo, alterando o nome do(s) autor(es), e o nome da aplicação:

```
$ sphinx-apidoc -F -f -A "nome do autor" -V 0 -R 0.1 -H "nome da aplicação" -e -P -a --ext-autodoc --ext-viewcode --ext-todo -o . ./../src/
```

Posteriormente deve configurar o ficheiro `doc\config.py` com as alterações que entenda necessárias

### Diretrizes de contribuição

* Quem tiver muita certeza do que está a fazer, pode alterar.
* Repositorio privado, restrito a alunos da UALG

### Com quem devo falar?

* David Valente, Gabriella Zanin, Sofia Martins
