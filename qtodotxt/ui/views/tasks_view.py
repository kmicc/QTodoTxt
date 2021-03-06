from PySide import QtGui, QtCore
from qtodotxt.ui.views.tasks_search_view import TasksSearchView
from qtodotxt.ui.views.tasks_list_view import TasksListView
from qtodotxt.ui.resource_manager import getIcon


class TasksView(QtGui.QWidget):

    def __init__(self, parent=None):
        super(TasksView, self).__init__(parent)
        self._initUI()

    def _initUI(self):
        layout = QtGui.QVBoxLayout(self)
        layout.setSpacing(10)

        self.tasks_search_view = TasksSearchView(getIcon("ActionSearch.png"), getIcon("ActionClear.png"), self)
        self.tasks_list_view = TasksListView(self)
        offset = QtCore.QSettings().value("ui_margin_offset", -4)
        self.setContentsMargins(2 * offset, offset, offset, offset)
        layout.addWidget(self.tasks_search_view)
        layout.addWidget(self.tasks_list_view)
        self.setLayout(layout)
