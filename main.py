from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
while True:
	try:
		text = input("hesapla -> ")
		#lexer kısmında tokenlara ayrıştırılması için dil öncelikle text olarak alınır.
		lexer = Lexer(text)
		#tokenler üretilir.
		tokens = lexer.generate_tokens()
		#parser tokenları kullanarak ayrıştırma işlemi yapar.
		#sadece okuma ve sınıflandırma, tabloya kaydetme işlemi yapılır.
		#semantik analiz aşamasında hata ayıklama yapılmaktadır.
		parser = Parser(tokens)
		tree = parser.parse()
		if not tree: continue
		interpreter = Interpreter()
		value = interpreter.visit(tree)
		print(value)
	except Exception as e:
		print(e)