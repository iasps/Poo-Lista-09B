from listapoo09B.models.cliente import Cliente, NCliente

class View:
  @classmethod
  def cliente_inserir(cls, nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)

  @classmethod
  def cliente_listar(cls):
    return NCliente.listar()
  @classmethod
  def lista_de_clientes(cls):
    lista = []
    for cliente in NCliente.listar():
      lista.append(cliente)
    return lista

  @classmethod
  def cliente_atualizar(cls, id, nome, email, fone):
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)

  @classmethod
  def cliente_excluir(cls, obj):
    NCliente.excluir(obj)
