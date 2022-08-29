from dataclasses import dataclass
#parser işlemi için yazılmıştır.
#işlem önceliklerinin belirlenmesi için ağacın yapısının oluşturulmasında yararlanılmıştır.
@dataclass
class sayiNode:
	value: any

	def __repr__(self):
		return f"{self.value}"

@dataclass
#toplama işlemi
class AddNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}+{self.node_b})"

@dataclass
#çıkarma işlemi
class SubtractNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}-{self.node_b})"

@dataclass
class carpmaNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}*{self.node_b})"

@dataclass
class bölmeNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}/{self.node_b})"

@dataclass
class artiNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"
	
@dataclass
class eksiNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"