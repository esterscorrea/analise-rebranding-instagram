import pandas as pd
import matplotlib.pyplot as plt

# importação de dados
df = pd.read_csv("rebranding_boom.csv")

print("Dados:")
print(df.head())

# convertendo datas
df["data"] = pd.to_datetime(df["data"])

# criar engajamento
df["engajamento"] = df["likes"] + df["comentarios"]

print("\nCom engajamento:")
print(df.head())

# Engajamento por fase (ANTES vs DEPOIS)
engajamento_fase = df.groupby("fase")["engajamento"].mean()

print("\nEngajamento médio por fase:")
print(engajamento_fase)

# Engajamento por tipo de post
engajamento_tipo = df.groupby("tipo_post")["engajamento"].mean()

print("\nEngajamento por tipo de post:")
print(engajamento_tipo)

# Engajamento por tema
engajamento_tema = df.groupby("tema")["engajamento"].mean()

print("\nEngajamento por tema:")
print(engajamento_tema)

# Engajamento por colaboração
engajamento_colab = df.groupby("colaboração")["engajamento"].mean()

print("\nEngajamento por colaboração:")
print(engajamento_colab)

# Porcentagem de crescimento
crescimento = (1299.8 - 733.2) / 733.2 * 100
print(crescimento)

# Gráfico 1 - Fase
engajamento_fase.plot(kind="bar", color="green")
plt.title("Engajamento médio por fase")
plt.xlabel("Fase")
plt.ylabel("Engajamento médio")
plt.tight_layout()
plt.show()

# Gráfico 2 - Tipo de post
engajamento_tipo.plot(kind="bar", color="green")
plt.title("Engajamento médio por tipo de post")
plt.xlabel("Tipo de post")
plt.ylabel("Engajamento médio")
plt.tight_layout()
plt.show()

# Gráfico 3 - Tema
engajamento_tema.plot(kind="bar", color="green")
plt.title("Engajamento médio por tema")
plt.xlabel("Tema")
plt.ylabel("Engajamento médio")
plt.tight_layout()
plt.show()

# Gráfico 4 - Colaboração
engajamento_colab.plot(kind="bar", color="green")
plt.title("Engajamento médio por colaboração")
plt.xlabel("Colaboração")
plt.ylabel("Engajamento médio")
plt.tight_layout()
plt.show()
