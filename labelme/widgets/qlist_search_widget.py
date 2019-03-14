from qtpy.QtCore import Qt
from qtpy import QtWidgets


class QlistSearchWidget(QtWidgets.QWidget):
    def __init__(self, listWidget):
        super(QlistSearchWidget, self).__init__()
        self.listWidget = listWidget
        vLayout = QtWidgets.QVBoxLayout(self)
        hLayout = QtWidgets.QHBoxLayout()

        self.searchWidget = QtWidgets.QLineEdit(self)
        hLayout.addWidget(self.searchWidget)
        self.searchWidget.setPlaceholderText("enter text to search")
        self.searchWidget.textChanged.connect(self.filter_labels)

        vLayout.addLayout(hLayout)
        vLayout.addWidget(self.listWidget)

    def filter_labels(self, text):
        filter_text = str(text).lower()
        for row in range(self.listWidget.count()):
            self.listWidget.setRowHidden(row, True)
        items = self.listWidget.findItems(filter_text, Qt.MatchContains)
        for item in items:
            self.listWidget.setRowHidden(self.listWidget.row(item), False)