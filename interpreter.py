from nodes import *
from values import Number

class Interpreter:
	def __init__(self):
		pass

	def visit(self, node):
		method_name = f'visit_{type(node).__name__}'
		method = getattr(self, method_name)
		return method(node)
		#sadece sayı geldiğinde sayı döndürür.
	def visit_sayiNode(self, node):
		return Number(node.value)
        #toplama işlemi için nodeları dolaşır.
	def visit_AddNode(self, node):
		return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
        #çıkarma işlemi için nodeları dolaşır.
	def visit_SubtractNode(self, node):
		return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)
        #çarpma işlemi için nodeları dolaşır.
	def visit_carpmaNode(self, node):
		return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
        #bölme işlemi için nodeları dolaşır.
	def visit_bölmeNode(self, node):
		try:
			return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
		except:
			raise Exception("Çalışma zamanı matematik hatası")