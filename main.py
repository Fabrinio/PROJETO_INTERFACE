from PySide6.QtWidgets import QApplication, QMainWindow
import sys
import requests
from ui_mainwindow import Ui_MainWindow

from PySide6 import QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PAV 2023.1 Lucas Fabrinio")  # Defina o título da janela principal aqui

        self.ui.btn_user.clicked.connect(lambda: self.showPage(self.ui.pg_user))
        self.ui.btn_exercise.clicked.connect(lambda: self.showPage(self.ui.pg_exercise))
        self.ui.btn_user_exercise.clicked.connect(lambda: self.showPage(self.ui.pg_user_exercise))
        self.showPage(self.ui.pg_user)

        #User
        self.ui.btn_post_user.clicked.connect(self.userCallAPIPost)
        self.ui.btn_del_user.clicked.connect(self.userCallAPIDel)
        self.ui.btn_put_user.clicked.connect(self.userCallAPIPut)
        self.ui.btn_get_user.clicked.connect(self.userCallAPIGet)

        #Exercise
        self.ui.btn_post_exercise.clicked.connect(self.exerciseCallAPIPost)
        self.ui.btn_del_exercise.clicked.connect(self.exerciseCallAPIDel)
        self.ui.btn_put_exercise.clicked.connect(self.exerciseCallAPIPut)
        self.ui.btn_get_exercise.clicked.connect(self.exerciseCallAPIGet)

        #UserExercise
        self.ui.btn_post_userexercise.clicked.connect(self.userExerciseCallAPIPost)
        self.ui.btn_del_userexercise.clicked.connect(self.userExerciseCallAPIDel)
        self.ui.btn_put_userexercise.clicked.connect(self.userExerciseCallAPIPut)
        self.ui.btn_get_userexercise.clicked.connect(self.userExerciseCallAPIGet)

    def showPage(self, page):
        self.ui.pg_user.setVisible(page == self.ui.pg_user)
        self.ui.pg_exercise.setVisible(page == self.ui.pg_exercise)
        self.ui.pg_user_exercise.setVisible(page == self.ui.pg_user_exercise)
    
    def userCallAPIGet(self):
        userId = self.findChild(QtWidgets.QLineEdit, 'txt_userid_user')
        print(userId.text())
        response = requests.get(f"http://localhost:5000/api/user/{userId.text()}")
        data = response.json()
        name = self.findChild(QtWidgets.QLineEdit, 'txt_name_user')
        if name:
            name.setText(data.get("name", ""))
        age = self.findChild(QtWidgets.QLineEdit, 'txt_age_user')
        if age:
            age.setText(str(data.get("age", "")))
        gender = self.findChild(QtWidgets.QLineEdit, 'txt_gender_user')
        if gender:
            gender.setText(data.get("gender", ""))
        height = self.findChild(QtWidgets.QLineEdit, 'txt_height_user')
        if height:
            height.setText(str(data.get("height", "")))
        weight = self.findChild(QtWidgets.QLineEdit, 'txt_weight_user')
        if weight:
            weight.setText(str(data.get("weight", "")))

    def userCallAPIPost(self):
        name = self.findChild(QtWidgets.QLineEdit, 'txt_name_user')
        age = self.findChild(QtWidgets.QLineEdit, 'txt_age_user')
        gender = self.findChild(QtWidgets.QLineEdit, 'txt_gender_user')
        height = self.findChild(QtWidgets.QLineEdit, 'txt_height_user')
        weight = self.findChild(QtWidgets.QLineEdit, 'txt_weight_user')
        data = {
            "name": name.text(),
            "age": age.text(),
            "gender": gender.text(),
            "height": height.text(),
            "weight": weight.text()
        }
        response = requests.post("http://localhost:5000/api/user", json=data)
        print(response.text)
    
    def userCallAPIPut(self):
        userId = self.findChild(QtWidgets.QLineEdit, 'txt_userid_user')
        name = self.findChild(QtWidgets.QLineEdit, 'txt_name_user')
        age = self.findChild(QtWidgets.QLineEdit, 'txt_age_user')
        gender = self.findChild(QtWidgets.QLineEdit, 'txt_gender_user')
        height = self.findChild(QtWidgets.QLineEdit, 'txt_height_user')
        weight = self.findChild(QtWidgets.QLineEdit, 'txt_weight_user')
        data = {
            "name": name.text(),
            "age": age.text(),
            "gender": gender.text(),
            "height": height.text(),
            "weight": weight.text()
        }
        response = requests.put(f"http://localhost:5000/api/user/{userId.text()}", json=data)
        print(response.text)

    def userCallAPIDel(self):
        userID = self.ui.txt_userid_user.text()
        response = requests.delete(f"http://localhost:5000/api/user/{userID}")
        print(response.json())

    def exerciseCallAPIGet(self):
        exerciseId = self.ui.txt_exerciseid_exercise.text()
        response = requests.get(f"http://localhost:5000/api/exercise/{exerciseId}")
        data = response.json()
        print(data)
        self.ui.txt_name_exercise.setText(data.get("name", ""))
        self.ui.txt_description_exercise.setText(data.get("description", ""))
        self.ui.txt_dificulty_exercise.setText(str(data.get("dificulty", "")))
        self.ui.txt_musculargroups_exercise.setText(data.get("muscular_groups", ""))

    def exerciseCallAPIPost(self):
        name = self.findChild(QtWidgets.QLineEdit, 'txt_name_exercise')
        description = self.findChild(QtWidgets.QLineEdit, 'txt_description_exercise')
        dificulty = self.findChild(QtWidgets.QLineEdit, 'txt_dificulty_exercise')
        muscular_groups = self.findChild(QtWidgets.QLineEdit, 'txt_musculargroups_exercise')
        data = {
            "name": name.text(),
            "description": description.text(),
            "dificulty": dificulty.text(),
            "muscular_groups": muscular_groups.text(),
        }
        response = requests.post("http://localhost:5000/api/exercise", json=data)
        print(response.text)
    
    def exerciseCallAPIPut(self):
        exerciseId = self.findChild(QtWidgets.QLineEdit, 'txt_exerciseid_exercise')
        name = self.findChild(QtWidgets.QLineEdit, 'txt_name_exercise')
        description = self.findChild(QtWidgets.QLineEdit, 'txt_description_exercise')
        dificulty = self.findChild(QtWidgets.QLineEdit, 'txt_dificulty_exercise')
        muscular_groups = self.findChild(QtWidgets.QLineEdit, 'txt_musculargroups_exercise')
        data = {
            "name": name.text(),
            "description": description.text(),
            "dificulty": dificulty.text(),
            "muscular_groups": muscular_groups.text(),
        }
        response = requests.put(f"http://localhost:5000/api/exercise/{exerciseId.text()}", json=data)
        print(response.text)

    def exerciseCallAPIDel(self):
        exerciseID = self.ui.txt_exerciseid_exercise.text()
        response = requests.delete(f"http://localhost:5000/api/exercise/{exerciseID}")
        print(response.json())

    def userExerciseCallAPIGet(self):
        userexerciseId = self.findChild(QtWidgets.QLineEdit, 'txt_userexerciseId')
        print(userexerciseId.text())
        response = requests.get(f"http://localhost:5000/api/user_exercise/{userexerciseId.text()}")
        data = response.json()
        id_user = self.findChild(QtWidgets.QLineEdit, 'txt_iduser_userexercise')
        if id_user:
            id_user.setText(str(data.get("id_user", "")))
        id_exercise = self.findChild(QtWidgets.QLineEdit, 'txt_idexercise_userexercise')
        if id_exercise:
            id_exercise.setText(str(data.get("id_exercise", "")))
        date = self.findChild(QtWidgets.QLineEdit, 'txt_date_userexercise')
        if date:
            date.setText(str(data.get("date", "")))
        duration = self.findChild(QtWidgets.QLineEdit, 'txt_duration_userexercise')
        if duration:
            duration.setText(str(data.get("duration", "")))
        weight = self.findChild(QtWidgets.QLineEdit, 'txt_weight_userexercise')
        if weight:
            weight.setText(str(data.get("weight", "")))
        repetitions = self.findChild(QtWidgets.QLineEdit, 'txt_repetitions_userexercise')
        if repetitions:
            repetitions.setText(str(data.get("repetitions", "")))

    def userExerciseCallAPIPost(self):
        id_user = self.findChild(QtWidgets.QLineEdit, 'txt_iduser_userexercise')
        id_exercise = self.findChild(QtWidgets.QLineEdit, 'txt_idexercise_userexercise')
        date = self.findChild(QtWidgets.QLineEdit, 'txt_date_userexercise')
        duration = self.findChild(QtWidgets.QLineEdit, 'txt_duration_userexercise')
        weight = self.findChild(QtWidgets.QLineEdit, 'txt_weight_userexercise')
        repetitions = self.findChild(QtWidgets.QLineEdit, 'txt_repetitions_userexercise')
        data = {
            "id_user": id_user.text(),
            "id_exercise": id_exercise.text(),
            "date": date.text(),
            "duration": duration.text(),
            "weight": weight.text(),
            "repetitions": repetitions.text()
        }
        response = requests.post("http://localhost:5000/api/user_exercise", json=data)
        print(response.text)
    
    def userExerciseCallAPIPut(self):
        userexerciseId = self.findChild(QtWidgets.QLineEdit, 'txt_userexerciseId')
        id_user = self.findChild(QtWidgets.QLineEdit, 'txt_iduser_userexercise')
        id_exercise = self.findChild(QtWidgets.QLineEdit, 'txt_idexercise_userexercise')
        date = self.findChild(QtWidgets.QLineEdit, 'txt_date_userexercise')
        duration = self.findChild(QtWidgets.QLineEdit, 'txt_duration_userexercise')
        weight = self.findChild(QtWidgets.QLineEdit, 'txt_weight_userexercise')
        repetitions = self.findChild(QtWidgets.QLineEdit, 'txt_repetitions_userexercise')
        data = {
            "id_user": id_user.text(),
            "id_exercise": id_exercise.text(),
            "date": date.text(),
            "duration": duration.text(),
            "weight": weight.text(),
            "repetitions": repetitions.text()
        }
        response = requests.put(f"http://localhost:5000/api/user_exercise/{userexerciseId.text()}", json=data)
        print(response.text)

    def userExerciseCallAPIDel(self):
        userexerciseID = self.ui.txt_userexerciseId.text()
        response = requests.delete(f"http://localhost:5000/api/user_exercise/{userexerciseID}")
        print(response.json())





if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
