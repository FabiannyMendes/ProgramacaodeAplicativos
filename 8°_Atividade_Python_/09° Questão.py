{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPIQR+zPe+J0kIO5FY4cQUs",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/FabiannyMendes/ProjetoGit/blob/main/8%C2%B0_Atividade_Python_.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Crie uma classe que modele uma pessoa\n",
        "(a) Atributos: nome, idade e endereco\n",
        "(b) Metodos: mostrar endereco e alterar endereco"
      ],
      "metadata": {
        "id": "II5hSz6XoHiX"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "w4Pi_2y3oCd4"
      },
      "outputs": [],
      "source": [
        "class Pessoa:\n",
        "  def __init__(self, nome, idade, endereco):\n",
        "    self.nome = nome\n",
        "    self.idade = idade\n",
        "    self.endereco = endereco\n",
        "\n",
        "  def mostrar_endereco(self):\n",
        "    print(f\"Endereço: {self.endereco}\")\n",
        "\n",
        "  def alterar_endereco(self, novo_endereco):\n",
        "    self.endereco = novo_endereco\n",
        "\n",
        "pessoa = Pessoa(\"Fabianny\", 17, \"73 Recife\")\n",
        "\n",
        "pessoa.mostrar_endereco()\n",
        "pessoa.alterar_endereco(\"825 Janga\")\n",
        "pessoa.mostrar_endereco()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Crie uma classe que modele uma aluno (a) Atributos: nome, numero de matrıcula e curso (b) Metodos: mostrar curso e alterar curso"
      ],
      "metadata": {
        "id": "gOmvPb4ToIhs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Aluno:\n",
        "  def __init__(self, nome, numero_matricula, curso):\n",
        "    self.nome = nome\n",
        "    self.numero_matricula = numero_matricula\n",
        "    self.curso = curso\n",
        "\n",
        "  def mostrar_curso(self):\n",
        "    print(f\"Curso: {self.curso}\")\n",
        "\n",
        "  def alterar_curso(self, novo_curso):\n",
        "    self.curso = novo_curso\n",
        "\n",
        "aluno = Aluno(\"Fabi\", 6223, \"Odontologia\")\n",
        "\n",
        "aluno.mostrar_curso()\n",
        "aluno.alterar_curso(\"Biomedicina\")\n",
        "aluno.mostrar_curso()"
      ],
      "metadata": {
        "id": "LqOO-r4HoMjS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Crie uma classe representando os alunos de um determinado curso. A classe deve conter os atributos matrıcula do aluno, nome, nota da primeira prova, nota da segunda prova e nota da terceira prova. Crie metodos para acessar o nome e a media do aluno.  (a) Permita ao usuario entrar com os dados de 5 alunos.  (b) Encontre o aluno com maior media geral.  (c) Encontre o aluno com menor media geral  (d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para aprovacao."
      ],
      "metadata": {
        "id": "3vFbs5E-oI1u"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Aluno:\n",
        "  def __init__(self, matricula, nome, nota1, nota2, nota3):\n",
        "    self.matricula = matricula\n",
        "    self.nome = nome\n",
        "    self.nota1 = nota1\n",
        "    self.nota2 = nota2\n",
        "    self.nota3 = nota3\n",
        "\n",
        "  def get_nome(self):\n",
        "    return self.nome\n",
        "\n",
        "  def get_media(self):\n",
        "    return (self.nota1 + self.nota2 + self.nota3) / 3\n",
        "\n",
        "alunos = []\n",
        "\n",
        "for i in range(5):\n",
        "  matricula = int(input(\"Digite a matrícula do aluno: \"))\n",
        "  nome = input(\"Digite o nome do aluno: \")\n",
        "  nota1 = float(input(\"Digite a nota da primeira prova: \"))\n",
        "  nota2 = float(input(\"Digite a nota da segunda prova: \"))\n",
        "  nota3 = float(input(\"Digite a nota da terceira prova: \"))\n",
        "  alunos.append(Aluno(matricula, nome, nota1, nota2, nota3))\n",
        "\n",
        "maior_media = 0\n",
        "aluno_maior_media = None\n",
        "for aluno in alunos:\n",
        "  media = aluno.get_media()\n",
        "  if media > maior_media:\n",
        "    maior_media = media\n",
        "    aluno_maior_media = aluno\n",
        "\n",
        "menor_media = 10\n",
        "aluno_menor_media = None\n",
        "for aluno in alunos:\n",
        "  media = aluno.get_media()\n",
        "  if media < menor_media:\n",
        "    menor_media = media\n",
        "    aluno_menor_media = aluno\n",
        "\n",
        "print(f\"Aluno com maior média: {aluno_maior_media.nome} - Média: {maior_media}\")\n",
        "print(f\"Aluno com menor média: {aluno_menor_media.nome} - Média: {menor_media}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 443
        },
        "id": "VnGHnaCvoLe4",
        "outputId": "c9c1fb8e-ef28-48fe-9931-ffbb7752e7a9"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Digite a matrícula do aluno: 10\n",
            "Digite o nome do aluno: Fabi\n",
            "Digite a nota da primeira prova: 10\n",
            "Digite a nota da segunda prova: 10\n",
            "Digite a nota da terceira prova: 0\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-0600cd9b4de6>\u001b[0m in \u001b[0;36m<cell line: 17>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 18\u001b[0;31m   \u001b[0mmatricula\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Digite a matrícula do aluno: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     19\u001b[0m   \u001b[0mnome\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Digite o nome do aluno: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     20\u001b[0m   \u001b[0mnota1\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfloat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Digite a nota da primeira prova: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Crie uma classe para representar um numero complexo. Implemente, usando sobrecarga de operador, os metodos para fazer as operacoes de soma, subtracao e produto entre dois numeros"
      ],
      "metadata": {
        "id": "zYSNJg0boIHz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class NumeroComplexo:\n",
        "  def __init__(self, real, imag):\n",
        "    self.real = real\n",
        "    self.imag = imag\n",
        "\n",
        "  def __add__(self, other):\n",
        "    return NumeroComplexo(self.real + other.real, self.imag + other.imag)\n",
        "\n",
        "  def __sub__(self, other):\n",
        "    return NumeroComplexo(self.real - other.real, self.imag - other.imag)\n",
        "\n",
        "  def __mul__(self, other):\n",
        "    return NumeroComplexo(\n",
        "      self.real * other.real - self.imag * other.imag,\n",
        "      self.real * other.imag + self.imag * other.real\n",
        "    )\n",
        "\n",
        "  def __str__(self):\n",
        "    return f\"{self.real} + {self.imag}i\"\n",
        "\n",
        "numero1 = NumeroComplexo(2, 3)\n",
        "numero2 = NumeroComplexo(4, 5)\n",
        "\n",
        "soma = numero1 + numero2\n",
        "diferenca = numero1 - numero2\n",
        "produto = numero1 * numero2\n",
        "\n",
        "print(f\"Soma: {soma}\")\n",
        "print(f\"Diferença: {diferenca}\")\n",
        "print(f\"Produto: {produto}\")"
      ],
      "metadata": {
        "id": "KQB8QlEuoL3z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os metodos para fazer as operacoes de incremento (de segundos) no horario e diferenca entre dois horarios."
      ],
      "metadata": {
        "id": "UqV4YO2doJHz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Horario:\n",
        "  def __init__(self, hora, minuto, segundo):\n",
        "    self.hora = hora\n",
        "    self.minuto = minuto\n",
        "    self.segundo = segundo\n",
        "\n",
        "  def incrementar(self, segundos):\n",
        "    self.segundo += segundos\n",
        "    self.__ajustar_tempo()\n",
        "\n",
        "  def diferenca(self, outro_horario):\n",
        "    segundos_self = self.hora * 3600 + self.minuto * 60 + self.segundo\n",
        "    segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo\n",
        "    return segundos_self - segundos_outro\n",
        "\n",
        "  def __ajustar_tempo(self):\n",
        "    if self.segundo >= 60:\n",
        "      self.minuto += self.segundo // 60\n",
        "      self.segundo %= 60\n",
        "    if self.minuto >= 60:\n",
        "      self.hora += self.minuto // 60\n",
        "      self.minuto %= 60\n",
        "\n",
        "  def __str__(self):\n",
        "    return f\"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}\"\n",
        "\n",
        "horario1 = Horario(10, 30, 0)\n",
        "horario2 = Horario(11, 45, 0)\n",
        "\n",
        "horario1.incrementar(3600)\n",
        "\n",
        "diferenca = horario2.diferenca(horario1)\n",
        "\n",
        "print(f\"Horário 1 após incremento: {horario1}\")\n",
        "print(f\"Diferença entre horários: {diferenca} segundos\")"
      ],
      "metadata": {
        "id": "dARbpgEwoMEz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. Implemente uma classe para representar em vetor (x,y,z) no R3 . Implemente os metodos para calcular a soma, subtracao, produto vetorial, produto escalar e modulo."
      ],
      "metadata": {
        "id": "BArPMABToJcY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Vetor3D:\n",
        "  def __init__(self, x, y, z):\n",
        "    self.x = x\n",
        "    self.y = y\n",
        "    self.z = z\n",
        "\n",
        "  def __add__(self, other):\n",
        "    return Vetor3D(self.x + other.x, self.y + other.y, self.z + other.z)\n",
        "\n",
        "  def __sub__(self, other):\n",
        "    return Vetor3D(self.x - other.x, self.y - other.y, self.z - other.z)\n",
        "\n",
        "  def produto_vetorial(self, other):\n",
        "    return Vetor3D(\n",
        "      self.y * other.z - self.z * other.y,\n",
        "      self.z * other.x - self.x * other.z,\n",
        "      self.x * other.y - self.y * other.x\n",
        "    )\n",
        "\n",
        "  def produto_escalar(self, other):\n",
        "    return self.x * other.x + self.y * other.y + self.z * other.z\n",
        "\n",
        "  def modulo(self):\n",
        "    return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5\n",
        "\n",
        "  def __str__(self):\n",
        "    return f\"({self.x}, {self.y}, {self.z})\"\n",
        "\n",
        "vetor1 = Vetor3D(1, 2, 3)\n",
        "vetor2 = Vetor3D(4, 5, 6)\n",
        "\n",
        "soma = vetor1 + vetor2\n",
        "subtracao = vetor1 - vetor2\n",
        "produto_vetorial = vetor1.produto_vetorial(vetor2)\n",
        "produto_escalar = vetor1.produto_escalar(vetor2)\n",
        "modulo_vetor1 = vetor1.modulo()\n",
        "\n",
        "print(f\"Soma: {soma}\")\n",
        "print(f\"Subtração: {subtracao}\")\n",
        "print(f\"Produto vetorial: {produto_vetorial}\")\n",
        "print(f\"Produto escalar: {produto_escalar}\")\n",
        "print(f\"Módulo do vetor 1: {modulo_vetor1}\")"
      ],
      "metadata": {
        "id": "XPtWeIr6oMPH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "7. Crie uma classe que modele um carro (a) Atributos: marca, ano e preco (b) Metodos: mostrar preco e de exibicao dos dados Leia os dados de 5 carros e um valor p, Mostre as informacoes de todos os carros com preco menor que p."
      ],
      "metadata": {
        "id": "y9otzP82oKQB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Carro:\n",
        "  def __init__(self, marca, ano, preco):\n",
        "    self.marca = marca\n",
        "    self.ano = ano\n",
        "    self.preco = preco\n",
        "\n",
        "  def mostrar_preco(self):\n",
        "    print(f\"Preço: R${self.preco:.2f}\")\n",
        "\n",
        "  def __str__(self):\n",
        "    return f\"Marca: {self.marca}\\nAno: {self.ano}\\nPreço: R${self.preco:.2f}\"\n",
        "\n",
        "carros = []\n",
        "\n",
        "for i in range(5):\n",
        "  marca = input(\"Digite a marca do carro: \")\n",
        "  ano = int(input(\"Digite o ano do carro: \"))\n",
        "  preco = float(input(\"Digite o preço do carro: \"))\n",
        "  carros.append(Carro(marca, ano, preco))\n",
        "\n",
        "p = float(input(\"Digite o valor p: \"))\n",
        "\n",
        "print(f\"\\nCarros com preço menor que R${p:.2f}:\")\n",
        "for carro in carros:\n",
        "  if carro.preco < p:\n",
        "    print(carro)"
      ],
      "metadata": {
        "id": "3bLYLIezoMZr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "8. Crie uma classe que modele uma conta corrente (a) Atributos: numero da conta, nome do correntista e saldo (b) Metodos: alterar nome, deposito e saque; No construtor, saldo e opcional, com valor default zero e os demais atributos sao obrigatorios."
      ],
      "metadata": {
        "id": "B15NZqe0oKip"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class ContaCorrente:\n",
        "  def __init__(self, numero_conta, nome_correntista, saldo=0):\n",
        "    self.numero_conta = numero_conta\n",
        "    self.nome_correntista = nome_correntista\n",
        "    self.saldo = saldo\n",
        "\n",
        "  def alterar_nome(self, novo_nome):\n",
        "    self.nome_correntista = novo_nome\n",
        "\n",
        "  def deposito(self, valor):\n",
        "    self.saldo += valor\n",
        "\n",
        "  def saque(self, valor):\n",
        "    if valor <= self.saldo:\n",
        "      self.saldo -= valor\n",
        "    else:\n",
        "      print(\"Saldo insuficiente para saque.\")\n",
        "\n",
        "  def __str__(self):\n",
        "    return f\"Número da conta: {self.numero_conta}\\nNome do correntista: {self.nome_correntista}\\nSaldo: R${self.saldo:.2f}\""
      ],
      "metadata": {
        "id": "YCVByG2coYPA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "9. Um racional e qualquer numero da forma p/q, sendo p inteiro e q inteiro nao nulo. Crie uma classe para representar um racional e os seguinte metodos: 1 (a) inverter sinal; (b) somar dois racionais; (c) subtrair dois racionais; (d) produto de dois racionais; (e) quociente de dois racionais;"
      ],
      "metadata": {
        "id": "Tx82ETA_oK2v"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Racional:\n",
        "  def __init__(self, numerador, denominador):\n",
        "    self.numerador = numerador\n",
        "    self.denominador = denominador\n",
        "\n",
        "  def __str__(self):\n",
        "    return f\"{self.numerador}/{self.denominador}\"\n",
        "\n",
        "  def sinal_contrario(self):\n",
        "    return Racional(-self.numerador, self.denominador)\n",
        "\n",
        "  def somar(self, outro_racional):\n",
        "    numerador = self.numerador * outro_racional.denominador + outro_racional.numerador * self.denominador\n",
        "    denominador = self.denominador * outro_racional.denominador\n",
        "    return Racional(numerador, denominador).simplificar()\n",
        "\n",
        "  def subtrair(self, outro_racional):\n",
        "    numerador = self.numerador * outro_racional.denominador - outro_racional.numerador * self.denominador\n",
        "    denominador = self.denominador * outro_racional.denominador\n",
        "    return Racional(numerador, denominador).simplificar()\n",
        "\n",
        "  def multiplicar(self, outro_racional):\n",
        "    numerador = self.numerador * outro_racional.numerador\n",
        "    denominador = self.denominador * outro_racional.denominador\n",
        "    return Racional(numerador, denominador).simplificar()\n",
        "\n",
        "  def dividir(self, outro_racional):\n",
        "    numerador = self.numerador * outro_racional.denominador\n",
        "    denominador = self.denominador * outro_racional.numerador\n",
        "    return Racional(numerador, denominador).simplificar()\n",
        "\n",
        "  def simplificar(self):\n",
        "    divisor = self.mdc(self.numerador, self.denominador)\n",
        "    self.numerador //= divisor\n",
        "    self.denominador //= divisor\n",
        "    return self\n",
        "\n",
        "  def mdc(self, a, b):\n",
        "    while b != 0:\n",
        "      a, b = b, a % b\n",
        "    return a"
      ],
      "metadata": {
        "id": "SPXMQgLlodUM"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
