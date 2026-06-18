# 🎓 Simulador BSI - Jogo de Progressão de Períodos

## 📖 Descrição do Projeto

O **Simulador BSI** é um jogo desenvolvido em Python que simula a trajetória de um estudante do curso de **Bacharelado em Sistemas de Informação (BSI)** ao longo dos períodos da graduação.

Durante a partida, o jogador avança pelos períodos do curso respondendo perguntas relacionadas às áreas de conhecimento presentes na matriz curricular de BSI, como Programação, Banco de Dados, Matemática e Lógica, Infraestrutura, Gestão e Sistemas de Informação.

Cada disciplina está associada a uma categoria de perguntas. Ao cursar uma disciplina, o jogador deve responder uma questão sorteada da área correspondente. Caso erre, a disciplina se torna uma pendência que deverá ser paga posteriormente. O objetivo é concluir todos os períodos, quitar possíveis pendências e, ao final do curso, realizar e defender o TCC para conquistar a graduação.

---

## 🎯 Objetivos do Jogo

* Simular a progressão acadêmica de um estudante de BSI.
* Reforçar conhecimentos básicos das áreas do curso.
* Trabalhar conceitos de lógica, programação e estruturas de dados.
* Demonstrar modularização e organização de software em Python.

---

## ⚙️ Funcionalidades

* Cadastro do nome do jogador.
* Progressão pelos períodos do curso.
* Sorteio de perguntas por categoria.
* Sistema de aprovação e reprovação.
* Controle de disciplinas pendentes.
* Possibilidade de pagar pendências em períodos posteriores.
* Sistema de jubilamento após múltiplas reprovações.
* Etapa final de TCC com perguntas específicas sobre desenvolvimento e elaboração de trabalhos acadêmicos.

---

## 🗂️ Estrutura do Projeto

```text
SIMULADOR-BSI---JOGO-DE-PP
│
├── data/
│   ├── disciplina.json
│   └── pergunta.json
│
├── disciplina.py
├── jogador.py
├── jogo.py
├── main.py
├── pergunta.py
├── utils.py
└── README.md
```

### Responsabilidade dos módulos

* **main.py** → Inicialização do jogo.
* **jogo.py** → Controle do fluxo principal da partida.
* **jogador.py** → Classe responsável pelos dados do jogador.
* **disciplina.py** → Classe que representa as disciplinas do curso.
* **pergunta.py** → Classe responsável pelas perguntas e validação das respostas.
* **utils.py** → Funções auxiliares para carregamento de dados e utilidades gerais.
* **data/** → Armazena os arquivos JSON contendo disciplinas e perguntas.

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* JSON
* Programação Orientada a Objetos (POO)
* Colorama
---


## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/GuilhermeValois/Simulador-BSI---Jogo-de-PP.git
```

2. Entre na pasta do projeto:

```bash
cd Simulador-BSI---Jogo-de-PP
```

3. Instale a dependência necessária:

```bash
pip install colorama
```

4. Execute o programa:

```bash
python main.py
```

---

## 📦 Dependências

O projeto utiliza a biblioteca **Colorama** para exibir mensagens coloridas no terminal, tornando a interação com o jogador mais intuitiva e agradável.

Caso a biblioteca não esteja instalada em sua máquina, utilize o comando:

```bash
pip install colorama
```

## 👨‍💻 Autores

* Guilherme Vasconcellos
* Julia Galindo

---

## 📌 Repositório

https://github.com/GuilhermeValois/Simulador-BSI---Jogo-de-PP

