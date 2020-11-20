import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTreeWidgetItem
from PyQt5.uic import loadUi
import xml.etree.ElementTree as et


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("treewidgettutorial.ui", self)
        f = open("books.xml", "r").read()
        self.print_tree(f)
        self.treeWidget.itemClicked.connect(self.on_item_clicked)

    def print_tree(self, s):
        tree = et.fromstring(s)
        self.treeWidget.setColumnCount(1)
        a = QTreeWidgetItem([tree.tag])
        self.treeWidget.addTopLevelItem(a)
        self.treeWidget.setHeaderHidden(True)

        def display_tree(a, s):
            for child in s:
                branch = QTreeWidgetItem([child.tag])
                a.addChild(branch)
                display_tree(branch, child)
            if s.text is not None:
                content = s.text
                a.addChild(QTreeWidgetItem([content]))

        display_tree(a, tree)

    def on_item_clicked(self):
        item = self.treeWidget.currentItem()
        # print(item.text(0))
        print(self.get_parent_path(item))

    def get_parent_path(self, item):
        def get_parent(item, outstring):
            if item.parent() is None:
                return outstring
            outstring = item.parent.text(0) + "/" + outstring
            return get_parent(item.parent, outstring)

        output = get_parent(item, item.text(0))
        return output


# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")