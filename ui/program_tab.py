# Form implementation generated from reading ui file 'D:\Projects\python\ManoMicroProgramSimulator\ManoMicroProgramSimulator\ui\program_tab.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProgramTab(object):
    def setupUi(self, ProgramTab):
        ProgramTab.setObjectName("ProgramTab")
        ProgramTab.resize(1512, 753)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ProgramTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=ProgramTab)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.codeTextEdit = QtWidgets.QTextEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codeTextEdit.sizePolicy().hasHeightForWidth())
        self.codeTextEdit.setSizePolicy(sizePolicy)
        self.codeTextEdit.setObjectName("codeTextEdit")
        self.verticalLayout_5.addWidget(self.codeTextEdit, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=ProgramTab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 400))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.frame_7)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.ARLineEdit = QtWidgets.QLineEdit(parent=self.frame_7)
        self.ARLineEdit.setObjectName("ARLineEdit")
        self.horizontalLayout_3.addWidget(self.ARLineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.DRLineEdit = QtWidgets.QLineEdit(parent=self.frame_7)
        self.DRLineEdit.setObjectName("DRLineEdit")
        self.horizontalLayout_3.addWidget(self.DRLineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.PCLineEdit = QtWidgets.QLineEdit(parent=self.frame_7)
        self.PCLineEdit.setObjectName("PCLineEdit")
        self.horizontalLayout_3.addWidget(self.PCLineEdit)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ACLineEdit = QtWidgets.QLineEdit(parent=self.frame_9)
        self.ACLineEdit.setObjectName("ACLineEdit")
        self.horizontalLayout_4.addWidget(self.ACLineEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.CARLineEdit = QtWidgets.QLineEdit(parent=self.frame_9)
        self.CARLineEdit.setObjectName("CARLineEdit")
        self.horizontalLayout_4.addWidget(self.CARLineEdit)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.SBRLineEdit = QtWidgets.QLineEdit(parent=self.frame_9)
        self.SBRLineEdit.setObjectName("SBRLineEdit")
        self.horizontalLayout_4.addWidget(self.SBRLineEdit)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.line = QtWidgets.QFrame(parent=self.frame_5)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.F1LineEdit = QtWidgets.QLineEdit(parent=self.frame_10)
        self.F1LineEdit.setObjectName("F1LineEdit")
        self.horizontalLayout_5.addWidget(self.F1LineEdit)
        self.label_8 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.F2LineEdit = QtWidgets.QLineEdit(parent=self.frame_10)
        self.F2LineEdit.setObjectName("F2LineEdit")
        self.horizontalLayout_5.addWidget(self.F2LineEdit)
        self.label_9 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.F3LineEdit = QtWidgets.QLineEdit(parent=self.frame_10)
        self.F3LineEdit.setObjectName("F3LineEdit")
        self.horizontalLayout_5.addWidget(self.F3LineEdit)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.CDLineEdit = QtWidgets.QLineEdit(parent=self.frame_11)
        self.CDLineEdit.setObjectName("CDLineEdit")
        self.horizontalLayout_6.addWidget(self.CDLineEdit)
        self.label_16 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.BRLineEdit = QtWidgets.QLineEdit(parent=self.frame_11)
        self.BRLineEdit.setObjectName("BRLineEdit")
        self.horizontalLayout_6.addWidget(self.BRLineEdit)
        self.label_17 = QtWidgets.QLabel(parent=self.frame_11)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        self.ADLineEdit = QtWidgets.QLineEdit(parent=self.frame_11)
        self.ADLineEdit.setObjectName("ADLineEdit")
        self.horizontalLayout_6.addWidget(self.ADLineEdit)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.line_2 = QtWidgets.QFrame(parent=self.frame_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.frame_12 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_18 = QtWidgets.QLabel(parent=self.frame_12)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.ILineEdit = QtWidgets.QLineEdit(parent=self.frame_12)
        self.ILineEdit.setObjectName("ILineEdit")
        self.horizontalLayout_7.addWidget(self.ILineEdit)
        self.label_19 = QtWidgets.QLabel(parent=self.frame_12)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        self.OPCodeLineEdit = QtWidgets.QLineEdit(parent=self.frame_12)
        self.OPCodeLineEdit.setObjectName("OPCodeLineEdit")
        self.horizontalLayout_7.addWidget(self.OPCodeLineEdit)
        self.label_20 = QtWidgets.QLabel(parent=self.frame_12)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_7.addWidget(self.label_20)
        self.ADDRLineEdit = QtWidgets.QLineEdit(parent=self.frame_12)
        self.ADDRLineEdit.setObjectName("ADDRLineEdit")
        self.horizontalLayout_7.addWidget(self.ADDRLineEdit)
        self.verticalLayout_3.addWidget(self.frame_12)
        self.line_3 = QtWidgets.QFrame(parent=self.frame_5)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.frame_13 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.compilePushButton = QtWidgets.QPushButton(parent=self.frame_13)
        self.compilePushButton.setObjectName("compilePushButton")
        self.horizontalLayout_8.addWidget(self.compilePushButton)
        self.runPushButton = QtWidgets.QPushButton(parent=self.frame_13)
        self.runPushButton.setObjectName("runPushButton")
        self.horizontalLayout_8.addWidget(self.runPushButton)
        self.nextPushButton = QtWidgets.QPushButton(parent=self.frame_13)
        self.nextPushButton.setObjectName("nextPushButton")
        self.horizontalLayout_8.addWidget(self.nextPushButton)
        self.resetPushButton = QtWidgets.QPushButton(parent=self.frame_13)
        self.resetPushButton.setObjectName("resetPushButton")
        self.horizontalLayout_8.addWidget(self.resetPushButton)
        self.verticalLayout_3.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_22 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_9.addWidget(self.label_22)
        self.speedHorizontalSlider = QtWidgets.QSlider(parent=self.frame_14)
        self.speedHorizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.speedHorizontalSlider.setObjectName("speedHorizontalSlider")
        self.horizontalLayout_9.addWidget(self.speedHorizontalSlider)
        self.verticalLayout_3.addWidget(self.frame_14)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.consoleTextEdit = QtWidgets.QTextEdit(parent=self.frame_6)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        self.consoleTextEdit.setPalette(palette)
        self.consoleTextEdit.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.consoleTextEdit.setReadOnly(True)
        self.consoleTextEdit.setObjectName("consoleTextEdit")
        self.verticalLayout_4.addWidget(self.consoleTextEdit, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout.addWidget(self.frame_6, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.mainMemoryTableWidget = QtWidgets.QTableWidget(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainMemoryTableWidget.sizePolicy().hasHeightForWidth())
        self.mainMemoryTableWidget.setSizePolicy(sizePolicy)
        self.mainMemoryTableWidget.setMinimumSize(QtCore.QSize(402, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.HighlightedText, brush)
        self.mainMemoryTableWidget.setPalette(palette)
        self.mainMemoryTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.mainMemoryTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.mainMemoryTableWidget.setObjectName("mainMemoryTableWidget")
        self.mainMemoryTableWidget.setColumnCount(4)
        self.mainMemoryTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mainMemoryTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainMemoryTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainMemoryTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainMemoryTableWidget.setHorizontalHeaderItem(3, item)
        self.mainMemoryTableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.mainMemoryTableWidget)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_8 = QtWidgets.QFrame(parent=ProgramTab)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.microMemoryTableWidget = QtWidgets.QTableWidget(parent=self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.microMemoryTableWidget.sizePolicy().hasHeightForWidth())
        self.microMemoryTableWidget.setSizePolicy(sizePolicy)
        self.microMemoryTableWidget.setMinimumSize(QtCore.QSize(402, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(213, 213, 213))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.HighlightedText, brush)
        self.microMemoryTableWidget.setPalette(palette)
        self.microMemoryTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.microMemoryTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.microMemoryTableWidget.setObjectName("microMemoryTableWidget")
        self.microMemoryTableWidget.setColumnCount(4)
        self.microMemoryTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.microMemoryTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.microMemoryTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.microMemoryTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.microMemoryTableWidget.setHorizontalHeaderItem(3, item)
        self.microMemoryTableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.microMemoryTableWidget)
        self.horizontalLayout.addWidget(self.frame_8)

        self.retranslateUi(ProgramTab)
        QtCore.QMetaObject.connectSlotsByName(ProgramTab)

    def retranslateUi(self, ProgramTab):
        _translate = QtCore.QCoreApplication.translate
        ProgramTab.setWindowTitle(_translate("ProgramTab", "Form"))
        self.label.setText(_translate("ProgramTab", "AR:  "))
        self.ARLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_2.setText(_translate("ProgramTab", "DR:  "))
        self.DRLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_3.setText(_translate("ProgramTab", "PC:  "))
        self.PCLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_4.setText(_translate("ProgramTab", "AC:  "))
        self.ACLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_5.setText(_translate("ProgramTab", "CAR:  "))
        self.CARLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_6.setText(_translate("ProgramTab", "SBR:  "))
        self.SBRLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_7.setText(_translate("ProgramTab", "F1:  "))
        self.F1LineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_8.setText(_translate("ProgramTab", "F2:  "))
        self.F2LineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_9.setText(_translate("ProgramTab", "F3:  "))
        self.F3LineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_15.setText(_translate("ProgramTab", "CD:  "))
        self.CDLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_16.setText(_translate("ProgramTab", "BR:  "))
        self.BRLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_17.setText(_translate("ProgramTab", "AD:  "))
        self.ADLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_18.setText(_translate("ProgramTab", "I:  "))
        self.ILineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_19.setText(_translate("ProgramTab", "OPCODE:  "))
        self.OPCodeLineEdit.setText(_translate("ProgramTab", "0000"))
        self.label_20.setText(_translate("ProgramTab", "ADDR:  "))
        self.ADDRLineEdit.setText(_translate("ProgramTab", "0000"))
        self.compilePushButton.setText(_translate("ProgramTab", "Compile"))
        self.runPushButton.setText(_translate("ProgramTab", "Run"))
        self.nextPushButton.setText(_translate("ProgramTab", "Next"))
        self.resetPushButton.setText(_translate("ProgramTab", "Reset"))
        self.label_22.setText(_translate("ProgramTab", "Speed:"))
        self.label_10.setText(_translate("ProgramTab", "Main Memory"))
        item = self.mainMemoryTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProgramTab", "Label"))
        item = self.mainMemoryTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProgramTab", "Address"))
        item = self.mainMemoryTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProgramTab", "Instruction"))
        item = self.mainMemoryTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ProgramTab", "Hex"))
        self.label_11.setText(_translate("ProgramTab", "MicroProgram Memory"))
        item = self.microMemoryTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProgramTab", "Label"))
        item = self.microMemoryTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProgramTab", "Address"))
        item = self.microMemoryTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProgramTab", "Instruction"))
        item = self.microMemoryTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ProgramTab", "Hex"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProgramTab = QtWidgets.QWidget()
    ui = Ui_ProgramTab()
    ui.setupUi(ProgramTab)
    ProgramTab.show()
    sys.exit(app.exec())
