from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QApplication

class CustomDialog(QDialog):
    def __init__(self, title, message, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle(title)
        
        # Message Label
        self.message_label = QLabel(message)
        
        # Layout for Dialog
        layout = QVBoxLayout()
        layout.addWidget(self.message_label)
        
        # Confirm Button
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)  # If confirmed, close with accept
        
        # Cancel Button
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)  # If canceled, close with reject
        
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)
        
        self.setLayout(layout)

# Main Code
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    
    window = None  # Main window reference
    
    # Create Dialog instance
    w = CustomDialog("Title", "This is a message notification", window)
    
    # Execute the dialog and check response
    if w.exec():
        print('Confirmed')
    else:
        print('Canceled')
    
    sys.exit(app.exec_())
