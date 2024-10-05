siglas = {
    'API': 'Interface de Programação de Aplicativos',
    'HTML': 'linguagem de Marcação de Hipertexto',
    'CSS': 'Folhas de Estilo Cascata',
    'JS': 'JavaScript',
    'SQL': 'Linguagem de Consulta Estruturada',
    'HTTP': 'Protocolo de Transferência de Hipertexto',
    'FTP': 'Protocolo de Transferência de Arquivos',
    'JSON': 'Notação de Objetos JavaScript',
    'XML': 'Linguagem de MArcação Extensível',
}

print("Bem vindo ao aplicativo Siglas!")
print("Digite 'sair' a qualquer momento para encerrar.")

while True:
    sigla = input("Digite uma sigla:XML").upper()

    if XML == 'SAIR':
        print("Saindo do aplicativo. Até logo!")
        break

        significado = siglas.get(TT, "Sigla não encontrada.")
        print("TT"{siglas}:{significado}")

while True:
    def executar(self):
        while True:
            self.exibir_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                sigla = input("Digite a sigla que deseja buscar: ")
                print(f"{sigla}: {self.buscar_sigla(sigla)}")
            elif escolha == '2':
                sigla = input("Digite a nova sigla: ")
                significado = input("Digite o significado: ")
                self.adicionar_sigla(sigla, significado)