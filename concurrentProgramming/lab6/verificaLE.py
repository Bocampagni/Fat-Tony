class LE:
	def __init__(self):
		self.escritores = 0
		self.leitores = 0
		self.escritores_esperando = 0
		self.escrita_pendente = False

	def leitorBloqueado(self, id):
		'''Recebe o id do leitor. Verifica se a decisão de bloqueio está correta.'''
		if self.escritores == 0 and not self.escrita_pendente:
			print("ERRO: Leitor " + str(id) + " bloqueado quando não há escritores!")

	def escritorBloqueado(self, id):
		'''Recebe o id do escritor. Verifica se a decisão de bloqueio está correta.'''
		if self.escritores == 0 and self.leitores == 0:
			print("ERRO: Escritor " + str(id) + " bloqueado quando não há escritores nem leitores!")

	def leitorLendo(self, id):
		'''Recebe o id do leitor, verifica se pode ler e registra que está lendo.'''
		if self.escritores > 0:
			print("ERRO: Leitor " + str(id) + " está lendo quando há escritor escrevendo!")

		self.leitores += 1

	def escritorEscrevendo(self, id):
		'''Recebe o id do escritor, verifica se pode escrever e registra que está escrevendo'''
		if self.escritores > 0 or self.leitores > 0:
			print("ERRO: Escritor " + str(id) + " está escrevendo quando há outro escritor ou leitores!")

		self.escritores += 1

	def leitorSaindo(self, id):
		'''Recebe o id do leitor e registra que terminou a leitura.'''
		self.leitores -= 1
		if self.leitores == 0 and self.escritores_esperando > 0:
			self.escrita_pendente = True

	def escritorSaindo(self, id):
		'''Recebe o id do escritor e registra que terminou a escrita.'''
		self.escritores -= 1
		self.escrita_pendente = False
		if self.escritores_esperando > 0:
			self.escrita_pendente = True
