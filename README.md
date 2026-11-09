# Semana 11 – Teste de Integração com Stubs (Mocks)

Atividade da disciplina de Teste de Software (ADS – IFSP).

O objetivo é testar o método que persiste a classe `Aluno` em um banco de dados **MongoDB**. Como o banco ainda não foi implementado, os testes usam um **stub (mock)** no lugar do banco real, com a biblioteca [mongomock](https://github.com/mongomock/mongomock).

## Estrutura do projeto

| Arquivo | Descrição |
|---|---|
| `aluno.py` | Classe `AlunoClass`, com o método `salvar(conexao, colecao)` que grava o aluno no MongoDB |
| `turma.py` | Classe `TurmaClass`, que cadastra alunos, guarda a menor e a maior nota e salva a turma |
| `conexao.py` | Classe `ConexaoClass`, que abre a conexão com o MongoDB via `pymongo` |
| `testes.py` | Casos de teste (`unittest`) usando `mongomock` como stub do banco |
| `main.py` | Ponto de entrada (vazio nesta atividade) |
| `requirements.txt` | Dependências do projeto |

## O que foi implementado

### `AlunoClass.salvar(conexao, colecao)`

Grava os dados do aluno (`nome`, `sobrenome`, `nota`) na coleção informada e retorna `True` quando o banco confirma a gravação.

```python
def salvar(self, conexao, colecao):
    documento = dict(self.__dict__);
    x = conexao[colecao].insert_one(documento);
    return x.acknowledged;
```

É usada uma cópia do `__dict__` porque o `insert_one` adiciona o campo `_id` ao dicionário recebido. Sem a cópia, o próprio objeto `Aluno` seria alterado.

### `alunoTest.test_salvarAluno`

Salva um aluno no banco simulado e verifica:

1. se o método `salvar` retornou `True`;
2. se o documento realmente foi gravado na coleção `aluno`;
3. se o sobrenome e a nota gravados estão corretos.

## Como funciona o stub

No `setUp` dos testes, o decorador `@mongomock.patch` substitui o `pymongo.MongoClient` por um cliente falso, em memória:

```python
@mongomock.patch(servers=(('localhost.com', 27017),))
def setUp(self):
    ...
    self.conexao = ConexaoClass.conexaoMongoDB(self, url = 'localhost.com', banco = 'faculdade')
```

Assim, a `ConexaoClass` é usada normalmente, mas nenhum servidor MongoDB real é necessário.

## Como executar

Requisito: Python 3.

```bash
pip install -r requirements.txt
python -m unittest testes -v
```

Saída esperada:

```
test_salvarAluno (testes.alunoTest.test_salvarAluno) ... ok
test_salvarTurma (testes.alunoTest.test_salvarTurma) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

## Autor

Lucca Zovedi
