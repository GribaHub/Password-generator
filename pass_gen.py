import sys, random, string, ctypes

from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Dialog

# clearing shell
def cls():
    print(50 * "\n")

# creating variable with strings    
def strings(i,j):
    txt = []
    for k in range(i,j): txt.append(chr(k))

    return("".join(txt))

# main program        
class GuiProgram(Ui_Dialog):
	def __init__(self, dialog):
		cls()            

		Ui_Dialog.__init__(self)
		self.setupUi(dialog)
		
		dialog.setWindowTitle("Password generator by Griba")

		self.checkBox_1.setText(strings(65,65+26)) # string.ascii_letters
		self.checkBox_2.setText(strings(97,97+26)) # string.ascii_letters
		self.checkBox_3.setText(strings(48,48+10)) # string.digits
		self.checkBox_4.setText(strings(33,33+15)) # string.punctuation
		self.checkBox_5.setText(strings(58,58+7)) # string.punctuation
		
		self.lineEdit_1.setText("8")
		self.lineEdit_2.setText("5")
		
		self.pushButton_1.clicked.connect(self.generate)
		self.pushButton_3.clicked.connect(self.txtbr_cls)
		self.pushButton_4.clicked.connect(self.copy)

		self.lineEdit_1.textEdited.connect(self.edit_colors)
		self.lineEdit_2.textEdited.connect(self.edit_colors)

		#checkBox_1.stateChanged.connect(self.check)
		for i in range(1,6): getattr(self, "checkBox_"+str(i)).stateChanged.connect(self.check)

# setting white color for line edits
	def edit_colors(self):
		#self.lineEdit_1.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")
		self.lineEdit_1.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")

# handling error message
	def err_msg(self,msg):
		dialog.setEnabled(0)

		if msg == 0:
			self.lineEdit_1.setStyleSheet("background-color: rgb(255, 0, 0);")
			self.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240);")

			ctypes.windll.user32.MessageBoxW(0, "Invalid password length!", "Error", 0)

			self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
			dialog.setEnabled(1)
			#self.lineEdit_1.clear()
			self.lineEdit_1.setFocus()
		else:
			self.lineEdit_2.setStyleSheet("background-color: rgb(255, 0, 0);")
			self.lineEdit_1.setStyleSheet("background-color: rgb(240, 240, 240);")

			ctypes.windll.user32.MessageBoxW(0, "Incorrect number of passwords to be generated!", "Error", 0)

			self.lineEdit_1.setStyleSheet("background-color: rgb(255, 255, 255);")
			dialog.setEnabled(1)
			#self.lineEdit_2.clear()
			self.lineEdit_2.setFocus()

# clearing text browser
	def txtbr_cls(self):
		self.textBrowser.clear()
		self.pushButton_3.setEnabled(0)
		self.pushButton_4.setEnabled(0)
		self.lineEdit_1.setFocus()

# copying text browser
	def copy(self):
		self.textBrowser.selectAll()
		self.textBrowser.copy()
		dialog.setEnabled(0)
		self.lineEdit_1.setStyleSheet("background-color: rgb(240, 240, 240);")
		self.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240);")

		ctypes.windll.user32.MessageBoxW(0, "Data copied to clipboard.", "Information", 0)

		self.lineEdit_1.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.textBrowser.clear()
		self.pushButton_3.setEnabled(0)
		self.pushButton_4.setEnabled(0)
		dialog.setEnabled(1)
		#self.lineEdit_1.setFocus()

# checking how many check box is checked
	def check(self):
		#self.checkBox_1.setEnabled(1)
		for i in range (1,6): getattr(self, "checkBox_"+str(i)).setEnabled(1)

		chb = []
		#chb.append(self.checkBox_1.isChecked())
		for i in range (1,6): chb.append(getattr(self, "checkBox_"+str(i)).isChecked())

		st = 0
		for i in range(5):
			if chb[i]: st=st+1

		if st < 2:
			for i in range (1,6):
				#if chb[0]: self.checkBox_1.setEnabled(0)
				if chb[i-1]: getattr(self, "checkBox_" + str(i)).setEnabled(0)

# generating password         
	def passw_f(self,passlen):
		p = []
		while len(p)<passlen:
			i = random.randint(0,5) # 5
			for j in range (0,5):
				#self.chceckBox_1.isChecked()                            
				if i == j and getattr(self, "checkBox_" + str(j+1)).isChecked(): p.append(i)

		passw = []
		for i in p:
			if i == 0: passw.append(chr(random.randint(65,65+25)))
			if i == 1: passw.append(chr(random.randint(97,97+25)))
			if i == 2: passw.append(chr(random.randint(48,48+9)))
			if i == 3: passw.append(chr(random.randint(33,33+14)))
			if i == 4: passw.append(chr(random.randint(58,58+6)))

		return("".join(passw))

# checking if string can be convert to number
	def chk_str(self,txt):
		for i in txt:
			if i not in string.digits: # string.dgits = "0123456789"
				txt = ""
				break

		if txt == "": txt = "0"
		return(txt)

# controlling for passwords generator
	def generate(self):
		lntxt=self.chk_str(self.lineEdit_1.text())
		howm=self.chk_str(self.lineEdit_2.text())

		if (int(lntxt) in range(4,33)):
			if int(howm) in range(1,101):
				for i in range (0,int(howm)): self.textBrowser.append(self.passw_f(int(lntxt)))
				self.pushButton_3.setEnabled(1)
				self.pushButton_4.setEnabled(1)
			else: self.err_msg(1)
		else: self.err_msg(0)

# starting gui
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
 
	prog = GuiProgram(dialog)
 
	dialog.show()
	sys.exit(app.exec_())
