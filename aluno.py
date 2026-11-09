class AlunoClass:
  def __init__(self, nome, sobrenome, nota):
    self.nome = nome;
    self.sobrenome = sobrenome;
    self.nota = nota;

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);

  def salvar(self, conexao, colecao):
    # Usa uma cópia dos atributos para que o insert_one (que adiciona o campo _id)
    # não altere o próprio objeto Aluno.
    documento = dict(self.__dict__);
    x = conexao[colecao].insert_one(documento);
    return x.acknowledged;
