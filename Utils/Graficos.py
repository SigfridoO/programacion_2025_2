from PyQt6.QtWidgets import QLabel
import sys

class Caja(QLabel):
    def __init__(self, color:str= "white"):
        super().__init__()
        self.setStyleSheet(f"background: {color}")