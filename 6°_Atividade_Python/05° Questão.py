{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNviZmawdqhL9rYyPMpaGvv",
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
        "<a href=\"https://colab.research.google.com/github/FabiannyMendes/ProjetoGit/blob/main/6%C2%B0_Atividade_Python.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "1. Faça um programa que possua um Dicionário, adicione elementos ao dicionário e os mostre na tela.\n",
        "\n",
        "\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "RMWp2RTfgv22"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7zUY0OdmgXSu",
        "outputId": "33f13852-4701-43d1-8228-55e70eb5349e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'nome': 'Fabianny', 'idade': 17, 'cidade': 'Recife'}\n"
          ]
        }
      ],
      "source": [
        "dicionario = {}\n",
        "\n",
        "dicionario[\"nome\"] = \"Fabianny\"\n",
        "dicionario[\"idade\"] = 17\n",
        "dicionario[\"cidade\"] = \"Recife\"\n",
        "\n",
        "print(dicionario)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.\n",
        "\n"
      ],
      "metadata": {
        "id": "ASa48NtLgwzx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "produtos = {}\n",
        "\n",
        "for i in range(3):\n",
        "  nome = input(\"Digite o nome do produto: \")\n",
        "  preco = float(input(\"Digite o preço do produto: \"))\n",
        "  produtos[nome] = preco\n",
        "\n",
        "print(produtos)"
      ],
      "metadata": {
        "id": "v9qJfPgegwWA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.\n",
        "\n"
      ],
      "metadata": {
        "id": "QNz4v4H-g7aU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "notas = {}\n",
        "\n",
        "for i in range(4):\n",
        "  nota = float(input(\"Digite a nota: \"))\n",
        "  notas[f\"nota{i+1}\"] = nota\n",
        "\n",
        "media = sum(notas.values()) / len(notas)\n",
        "\n",
        "print(f\"Notas: {notas}\")\n",
        "print(f\"Média: {media}\")"
      ],
      "metadata": {
        "id": "2g4ykoRMg8LT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Faça um programa, utilizando Dicionários, que:\n",
        "\n",
        "1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .\n",
        "\n",
        "2° Passo: Peça para o usuário inserir um número.\n",
        "\n",
        "3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.."
      ],
      "metadata": {
        "id": "NV1vGcYQg9Bu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "caixa_misteriosa = {}\n",
        "\n",
        "for i in range(4):\n",
        "  item = input(f\"Digite o {i+1}º item para colocar na caixa misteriosa: \")\n",
        "  caixa_misteriosa[f\"item{i+1}\"] = item\n",
        "\n",
        "numero = int(input(\"Digite um número entre 1 e 4: \"))\n",
        "\n",
        "if not 1 <= numero <= 4:\n",
        "  print(\"Número inválido. Digite um número entre 1 e 4.\")\n",
        "else:\n",
        "  item = caixa_misteriosa[f\"item{numero}\"]\n",
        "  print(f\"O item na posição {numero} é: {item}\")"
      ],
      "metadata": {
        "id": "SK_79TLtg9k7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. Faça um programa, utilizando Dicionários, que:\n",
        "\n",
        "1° Passo: Peça para o usuário inserir o nome de três funcionários e os mostre na tela.\n",
        "\n",
        "2° Passo: Peça para o usuário demitir um funcionário e mostre na tela os funcionários restantes."
      ],
      "metadata": {
        "id": "K1Qhdgs9g-gI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "funcionarios = {}\n",
        "\n",
        "for i in range(3):\n",
        "  nome = input(f\"Digite o nome do {i+1}º funcionário: \")\n",
        "  funcionarios[f\"funcionario{i+1}\"] = nome\n",
        "\n",
        "print(f\"Funcionários: {funcionarios}\")\n",
        "\n",
        "nome_demitido = input(\"Digite o nome do funcionário que deseja demitir: \")\n",
        "\n",
        "if nome_demitido not in funcionarios.values():\n",
        "  print(f\"Funcionário {nome_demitido} não encontrado.\")\n",
        "else:\n",
        "  for key, value in funcionarios.items():\n",
        "    if value == nome_demitido:\n",
        "      del funcionarios[key]\n",
        "      break\n",
        "\n",
        "  print(f\"Funcionários restantes: {funcionarios}\")"
      ],
      "metadata": {
        "id": "CKYeuwVXg-3P"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
