from fastapi import FastAPI
import csv
import os
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
	name: str
	curso: str
	ativo: bool

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
	return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
	return id_estudante > 0


@app.get("/")
# 127.0.0.1:8000/
async def root():
    return {"message": "TESTANDO O DOCKER"}

# Nome do arquivo onde os dados serão salvos
arquivo_csv = 'clientes.csv'


# Função para adicionar cliente
def adicionar_cliente():
    id_cliente = input("Digite o ID do cliente: ")
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    # Verificar se o arquivo já existe e se precisa adicionar cabeçalhos
    arquivo_existe = os.path.isfile(arquivo_csv)

    with open(arquivo_csv, mode='a', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)

        # Adicionar cabeçalhos se o arquivo não existe
        if not arquivo_existe:
            escritor_csv.writerow(['ID', 'Nome', 'Telefone'])

        escritor_csv.writerow([id_cliente, nome, telefone])

    print("Cliente adicionado com sucesso!")


# Função para listar clientes
def listar_clientes():
    if not os.path.isfile(arquivo_csv):
        print("Nenhum cliente cadastrado.")
        return

    with open(arquivo_csv, mode='r', newline='') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            print(linha)


# Menu principal
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Adicionar cliente")
        print("2. Listar clientes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o menu
if __name__ == '__main__':
    menu()
