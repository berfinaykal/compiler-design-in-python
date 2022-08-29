from tokens import Token, TokenType
#bosluklar tanımlanmıştır.
#rakamlar kümesi oluşturulmuştur.
bosluklar = ' \n\t'
rakamlar = '0123456789'

class Lexer:
	def __init__(self, text):
        #iter() ile her seferde bir öge döndürülür.
		self.text = iter(text)
		self.sonraki()

	def sonraki(self):
        #iter fonksiyonu ile döngüyle birlikte her adımda bir öge döndürülmektedir. Öge simdiki_öge değişkenine aktarılır. eğer simdiki_ögeden sonra bir değer yoksa iterasyon bitirilir.
		try:
			self.simdiki_öge = next(self.text)
		except StopIteration:
			self.simdiki_öge = None

	def generate_tokens(self):
        #simdiki_öge değişkeni none olmadığı sürece while döngüsü çalışacaktır. 
		while self.simdiki_öge != None:
            #token tablosuna bosluklar dahil edilmemiştir. Çünkü ayrıştırma ağacında yer almayacaklar. Eğer sonraki değer okunduğunda boşluk gelirse bir sonraki değeri oku.
			if self.simdiki_öge in bosluklar:
				self.sonraki()
                #. veya rakam okuduğunda sayı üret fonksiyonu çalışmaktadır.
			elif self.simdiki_öge == '.' or self.simdiki_öge in rakamlar:
				yield self.generate_number()
                #artı geldiğinde token tablosunda tanımlanmış bir işaret olması gerektiğinden token fonksiyonu ile tanıma işlemi yapılır. 
                #aynı işlemler dilde tanımasını istediğimiz diğer işaretler için de geçerlidir.
			elif self.simdiki_öge == '+':
				self.sonraki()
				yield Token(TokenType.arti)
			elif self.simdiki_öge == '-':
				self.sonraki()
				yield Token(TokenType.eksi)
			elif self.simdiki_öge == '*':
				self.sonraki()
				yield Token(TokenType.carpma)
			elif self.simdiki_öge == '/':
				self.sonraki()
				yield Token(TokenType.bölme)
			elif self.simdiki_öge == '(':
				self.sonraki()
				yield Token(TokenType.sol_parantez)
			elif self.simdiki_öge == ')':
				self.sonraki()
				yield Token(TokenType.sag_parantez)
			else:
                #bunların dışında okunan ögeler için hata yakalanmaktadır.
				raise Exception(f"Illegal character '{self.simdiki_öge}'")

	def generate_number(self):
		ondalık_nokta_sayisi = 0
		number_str = self.simdiki_öge # örn 0.5 değerini tanımamız gerekiyor. ilk olarak 0 okuduk. bu okuduğumuz değeri number_str değişkenine aktardık. 
		self.sonraki()
        #bu kısımda ondalık sayıları tanımak için noktanın geldiği kısımdan sonra döngüden çıkma işlemi yapılmıştır.
        #döngüde nokta geldikten sonra döngüden çıkılmıştır.
		while self.simdiki_öge != None and (self.simdiki_öge == '.' or self.simdiki_öge in rakamlar):
			if self.simdiki_öge == '.':
				ondalık_nokta_sayisi += 1
				if ondalık_nokta_sayisi > 1:
					break
			#number_str değişkenimizde 0 değeri vardı. şimdiki öge ile . okuduk. bu iki değer number_str değişkenine toplanarak aktarılır ve sonraki öge okunur.
			number_str += self.simdiki_öge #
			self.sonraki()
        #eğer number_str değişkeni . ile başlıyorsa number_str değişkeninin başına sıfır eklensin. örn .5 yerine 0.5 olsun.
		if number_str.startswith('.'):
			number_str = '0' + number_str
        #eğer number_str değişkeni . ile bitiyorsa number_str değişkeninin sonuna sıfır eklensin. örn 5. yerine 5.0 olsun.
		if number_str.endswith('.'):
			number_str += '0'
        
		return Token(TokenType.sayi, float(number_str))