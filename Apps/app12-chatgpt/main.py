
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QToolBar, QMessageBox, \
QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QStatusBar, QTextEdit
import sys
from openai import OpenAI
import openai



class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 400)

        # chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320) # distance from x - y, width for x - y
        self.chat_area.setReadOnly(True)

        # input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 335, 480, 30)

        # button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(490, 335, 75, 30)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"Me: {user_input}")
        self.input_field.clear()

        chatbot = Chatbot()
        response = chatbot.get_response(user_input)
        self.chat_area.append(f"Bot: {response}")

# # backend logic
# class Chatbot:
#     def __init__(self):
#         pass
        

#     def get_response(self, user_input):
#         response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#             "role": "system",
#             "content": "Riceverai delle domande a cui dovrai dare una risposta pertinente"
#             },
#             {
#             "role": "user",
#             "content": user_input
#             }
#         ],
#         temperature=0.5,
#         max_tokens = 4000,
#         top_p = 1
#         )
#         return response.choices[0].message["content"]
    

# client = OpenAI(api_key = "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")
app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())