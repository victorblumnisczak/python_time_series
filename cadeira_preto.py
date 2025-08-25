Em python, o que é um cabeçalho dentro de um arquivo python e para que serve? O que é um docstring e para que serve? Qual a diferença do cabeçalho arquivo para o docstring?

###  Cabeçalho de Arquivo Python:

* Fica no *início do arquivo*.
* Usa **comentários (#).
* Serve para indicar:

  * Autor, data, descrição.
  * Codificação (# -*- coding: utf-8 -*-).
  * Interpretador (#!/usr/bin/env python3).

*Exemplo:*

python
# Autor: João
# Descrição: Script de exemplo


---

###  Docstring:

* Fica *dentro de funções, classes ou no topo do arquivo*.
* Usa **aspas triplas (""").
* Serve para *explicar o que o código faz*.

*Exemplo:*

python
def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b


---

###  Diferença:

| Cabeçalho            | Docstring               |
| -------------------- | ----------------------- |
| Comentários (#)    | String com """        |
| Fora do código       | Dentro do código        |
| Metadados do arquivo | Explica o funcionamento |

---
