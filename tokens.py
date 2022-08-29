from enum import Enum
from dataclasses import dataclass
# tokenların sembol tablosunda kaydedilirken yerleşecekleri alanlar aşağıda sınıflandırılmıştır. sembol tablosunda okunan değerlerin bir karşılığı vardır.
# bu sınıflandırmaya göre ayrıştırma işlemi yapılır.
class TokenType(Enum):
	sayi    = 0
	arti      = 1
	eksi     = 2
	carpma  = 3
	bölme    = 4
	sol_parantez    = 5
	sag_parantez    = 6

@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")