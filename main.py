# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot


# class Bridge(QObject):
#
#     @Slot(int, result=int)
#     def tellAngle(self, angle):
#         print(angle)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # # Instance of the Python object
    # bridge = Bridge()
    #
    # # Expose the Python object to QML
    # context = engine.rootContext()
    # context.setContextProperty("con", bridge)

    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))

#    slider = engine.rootObjects()[0].findChild(QObject, "slider")

if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec_())
