{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPB63q+AGcEzSt3HmqwQEKX",
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
        "<a href=\"https://colab.research.google.com/github/FabiannyMendes/ProjetoGit/blob/main/4%C2%B0_Atividade_Python.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.\n"
      ],
      "metadata": {
        "id": "CO_BIdrJlDMj"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "FdCWadMqkiZA"
      },
      "outputs": [],
      "source": [
        "idades = []\n",
        "alturas = []\n",
        "\n",
        "for i in range(5):\n",
        "    idade = int(input(f\"Digite a idade da pessoa {i + 1}: \"))\n",
        "    altura = float(input(f\"Digite a altura da pessoa {i + 1} (em metros): \"))\n",
        "    idades.append(idade)\n",
        "    alturas.append(altura)\n",
        "\n",
        "print(\"\\nIdades e alturas na ordem inversa:\")\n",
        "for i in range(4, -1, -1):\n",
        "    print(f\"Idade: {idades[i]}, Altura: {alturas[i]}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.\n"
      ],
      "metadata": {
        "id": "3Xwsj5GSlD3L"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "vetor_a = [int(input(f\"Digite o número {i + 1}: \")) for i in range(10)]\n",
        "\n",
        "soma_quadrados = sum(x**2 for x in vetor_a)\n",
        "print(f\"\\nA soma dos quadrados dos elementos do vetor é: {soma_quadrados}\")"
      ],
      "metadata": {
        "id": "ubxj3annlEUl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "3 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.\n"
      ],
      "metadata": {
        "id": "tDOOmQ5slFdu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "vetor_1 = []\n",
        "vetor_2 = []\n",
        "\n",
        "for i in range(10):\n",
        "  valor = int(input(f\"Digite o {i+1}º elemento do primeiro vetor: \"))\n",
        "  vetor_1.append(valor)\n",
        "\n",
        "for i in range(10):\n",
        "  valor = int(input(f\"Digite o {i+1}º elemento do segundo vetor: \"))\n",
        "  vetor_2.append(valor)\n",
        "\n",
        "vetor_3 = []\n",
        "\n",
        "for i in range(10):\n",
        "  vetor_3.append(vetor_1[i])\n",
        "  vetor_3.append(vetor_2[i])\n",
        "\n",
        "print(f\"Terceiro vetor: {vetor_3}\")"
      ],
      "metadata": {
        "id": "jdHghMgulFJw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "4 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.\n"
      ],
      "metadata": {
        "id": "otjG65lDlH9x"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "vetor1 = [int(input(f\"Digite o elemento {i + 1} do primeiro vetor: \")) for i in range(10)]\n",
        "vetor2 = [int(input(f\"Digite o elemento {i + 1} do segundo vetor: \")) for i in range(10)]\n",
        "vetor3 = [int(input(f\"Digite o elemento {i + 1} do terceiro vetor: \")) for i in range(10)]\n",
        "\n",
        "vetor_intercalado = [val for triple in zip(vetor1, vetor2, vetor3) for val in triple]\n",
        "\n",
        "print(\"\\nVetor intercalado:\", vetor_intercalado)"
      ],
      "metadata": {
        "id": "zOm3NbTGlF5I"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "5 - Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.\n",
        "\n"
      ],
      "metadata": {
        "id": "fGbmm1svlEyM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "idades = []\n",
        "alturas = []\n",
        "\n",
        "for i in range(10):\n",
        "    idade = int(input(f\"Digite a idade do aluno {i + 1}: \"))\n",
        "    altura = float(input(f\"Digite a altura do aluno {i + 1} (em metros): \"))\n",
        "    idades.append(idade)\n",
        "    alturas.append(altura)\n",
        "\n",
        "media_alturas = sum(alturas) / 10\n",
        "alunos_acima_13_com_altura_abaixo_media = sum(1 for i in range(10) if idades[i] > 13 and alturas[i] < media_alturas)\n",
        "\n",
        "print(f\"\\n{alunos_acima_13_com_altura_abaixo_media} alunos com mais de 13 anos possuem altura inferior à média.\")"
      ],
      "metadata": {
        "id": "pXvEzROqlIYB"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
