# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSlot

if __name__ == "__main__":

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('main.qml')
    root_obj = engine.rootObjects()[0]

    slider = root_obj.findChild(QObject, "slider")
    axisComboBox = root_obj.findChild(QObject, "axisComboBox")
    angleText = root_obj.findChild(QObject, "angleText")
    resetBtn = root_obj.findChild(QObject, "resetBtn")

    print(slider)
    print(axisComboBox)
    print(angleText)
    print(resetBtn)

    @pyqtSlot()
    def receive_angle():
        angle = slider.property("value")
        print(f"{angle} Degree")
        angleText.setProperty("text", int(angle*2))

    slider.moved.connect(receive_angle)

    @pyqtSlot(int)
    def receive_axis(combo_box_index):
        print(combo_box_index)
        print(axisComboBox.property("currentText"))

    axisComboBox.activated.connect(receive_axis)

    @pyqtSlot()
    def receive_angel_text():
        new_angle = angleText.property("text")
        print(new_angle)
        slider.setProperty("value", int(new_angle)/2)

    angleText.editingFinished.connect(receive_angel_text)

    @pyqtSlot()
    def receive_reset_button_clicked():
        print("reset")
        slider.setProperty("value", 0)
        angleText.setProperty("text", "0")

    resetBtn.clicked.connect(receive_reset_button_clicked)




    sys.exit(app.exec())
