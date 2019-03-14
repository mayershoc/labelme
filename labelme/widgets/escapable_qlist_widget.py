from qtpy.QtCore import Qt
from qtpy import QtWidgets


class EscapableQListWidget(QtWidgets.QListWidget):

    def __init__(self):
        QtWidgets.QListWidget.__init__(self)
        self.prevItem = None
        self.itemSelectionChanged.connect(self.item_changed)
        self.itemClicked.connect(self.item_click)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.clearSelection()
    
    def item_changed(self):
        self.prevItem = None

    def item_click(self, item):
        if not self.prevItem:
            self.prevItem = item
        elif self.prevItem == item:
            self.prevItem = None
            self.clearSelection()