from tokens import TokenType
from nodes import *

class Parser:
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.sonraki()

	def raise_error(self):
		raise Exception("geçersiz syntax")
	
	def sonraki(self):
		try:
            #iter fonksiyonu ile döngüyle birlikte her adımda bir öge döndürülmektedir. Öge simdiki_öge değişkenine aktarılır. eğer simdiki_ögeden sonra bir değer yoksa iterasyon bitirilir.
			self.simdiki_öge = next(self.tokens)
		except StopIteration:
			self.simdiki_öge = None

	def parse(self):

		if self.simdiki_öge == None:
			return None
		result = self.expr()

		if self.simdiki_öge != None:
			self.raise_error()

		return result

        #işlem önceliğinin belirlenmesi için ilk olarak expressionlar kullanılır. toplama ve çıkarma işlemleri yapılır.


	def expr(self):
		#expression içinde term çağırılır. 
		result = self.term()
		while self.simdiki_öge != None and self.simdiki_öge.type in (TokenType.arti, TokenType.eksi):
			if self.simdiki_öge.type == TokenType.arti:
				self.sonraki()
				result = AddNode(result, self.term())
			elif self.simdiki_öge.type == TokenType.eksi:
				self.sonraki()
				result = SubtractNode(result, self.term())
		return result
        
        #toplama ve çıkarmaya göre işlem önceliği carpma ve bölmededir.

	def term(self):
		result = self.factor()

		while self.simdiki_öge != None and self.simdiki_öge.type in (TokenType.carpma, TokenType.bölme):
			if self.simdiki_öge.type == TokenType.carpma:
				self.sonraki()
				result = carpmaNode(result, self.factor())
			elif self.simdiki_öge.type == TokenType.bölme:
				self.sonraki()
				result = bölmeNode(result, self.factor())
		return result

        #çarpma ve bölmeye göre işlem önceliği parantez içindedir. 
	def factor(self):
		token = self.simdiki_öge

		if token.type == TokenType.sol_parantez:
            #açma parantezi geldikten sonra expr fonksiyonu çağırılır. parantez içi işlem önceliği alır.
			self.sonraki()
			result = self.expr()
            #kapatma parantezi açma parantezinden önce gelemeyeceği için hata verir.
			if self.simdiki_öge.type != TokenType.sag_parantez:
				self.raise_error()
			self.sonraki()
			return result

		elif token.type == TokenType.sayi:
			self.sonraki()
			return sayiNode(token.value)

		elif token.type == TokenType.arti:
			self.sonraki()
			return artiNode(self.factor())
		
		elif token.type == TokenType.eksi:
			self.sonraki()
			return eksiNode(self.factor())
		
		self.raise_error()