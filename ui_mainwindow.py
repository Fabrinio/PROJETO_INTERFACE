# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(875, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(0, 0))
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 160, 425))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_user = QPushButton(self.page)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_user)

        self.btn_exercise = QPushButton(self.page)
        self.btn_exercise.setObjectName(u"btn_exercise")
        self.btn_exercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_exercise)

        self.btn_user_exercise = QPushButton(self.page)
        self.btn_user_exercise.setObjectName(u"btn_user_exercise")
        self.btn_user_exercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_user_exercise)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 160, 425))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_5.addWidget(self.textEdit)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.pg_user = QWidget()
        self.pg_user.setObjectName(u"pg_user")
        self.horizontalLayout_5 = QHBoxLayout(self.pg_user)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_3 = QFrame(self.pg_user)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_txts_user = QFrame(self.frame_4)
        self.lbl_txts_user.setObjectName(u"lbl_txts_user")
        self.lbl_txts_user.setFrameShape(QFrame.StyledPanel)
        self.lbl_txts_user.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.lbl_txts_user)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_userid_user = QLineEdit(self.lbl_txts_user)
        self.txt_userid_user.setObjectName(u"txt_userid_user")
        self.txt_userid_user.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_userid_user, 0, 0, 1, 1)

        self.txt_name_user = QLineEdit(self.lbl_txts_user)
        self.txt_name_user.setObjectName(u"txt_name_user")
        self.txt_name_user.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_name_user, 1, 0, 1, 1)

        self.txt_age_user = QLineEdit(self.lbl_txts_user)
        self.txt_age_user.setObjectName(u"txt_age_user")
        self.txt_age_user.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_age_user, 2, 0, 1, 1)

        self.txt_gender_user = QLineEdit(self.lbl_txts_user)
        self.txt_gender_user.setObjectName(u"txt_gender_user")
        self.txt_gender_user.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_gender_user, 3, 0, 1, 1)

        self.txt_height_user = QLineEdit(self.lbl_txts_user)
        self.txt_height_user.setObjectName(u"txt_height_user")
        self.txt_height_user.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_height_user, 4, 0, 1, 1)

        self.txt_weight_user = QLineEdit(self.lbl_txts_user)
        self.txt_weight_user.setObjectName(u"txt_weight_user")
        self.txt_weight_user.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_weight_user, 5, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.lbl_txts_user)

        self.lbl_buttons_user = QFrame(self.frame_4)
        self.lbl_buttons_user.setObjectName(u"lbl_buttons_user")
        self.lbl_buttons_user.setFrameShape(QFrame.StyledPanel)
        self.lbl_buttons_user.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.lbl_buttons_user)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_post_user = QPushButton(self.lbl_buttons_user)
        self.btn_post_user.setObjectName(u"btn_post_user")
        self.btn_post_user.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_post_user)

        self.btn_put_user = QPushButton(self.lbl_buttons_user)
        self.btn_put_user.setObjectName(u"btn_put_user")
        self.btn_put_user.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_put_user)

        self.btn_del_user = QPushButton(self.lbl_buttons_user)
        self.btn_del_user.setObjectName(u"btn_del_user")
        self.btn_del_user.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_del_user)

        self.btn_get_user = QPushButton(self.lbl_buttons_user)
        self.btn_get_user.setObjectName(u"btn_get_user")
        self.btn_get_user.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_get_user)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.horizontalLayout_6.addWidget(self.lbl_buttons_user)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.pages.addWidget(self.pg_user)
        self.pg_exercise = QWidget()
        self.pg_exercise.setObjectName(u"pg_exercise")
        self.verticalLayout_10 = QVBoxLayout(self.pg_exercise)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_8 = QFrame(self.pg_exercise)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_15.addWidget(self.label_6)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_txts_exercise = QFrame(self.frame_9)
        self.lbl_txts_exercise.setObjectName(u"lbl_txts_exercise")
        self.lbl_txts_exercise.setFrameShape(QFrame.StyledPanel)
        self.lbl_txts_exercise.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.lbl_txts_exercise)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.txt_exerciseid_exercise = QLineEdit(self.lbl_txts_exercise)
        self.txt_exerciseid_exercise.setObjectName(u"txt_exerciseid_exercise")
        self.txt_exerciseid_exercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.txt_exerciseid_exercise)

        self.txt_name_exercise = QLineEdit(self.lbl_txts_exercise)
        self.txt_name_exercise.setObjectName(u"txt_name_exercise")
        self.txt_name_exercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.txt_name_exercise)

        self.txt_description_exercise = QLineEdit(self.lbl_txts_exercise)
        self.txt_description_exercise.setObjectName(u"txt_description_exercise")
        self.txt_description_exercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.txt_description_exercise)

        self.txt_dificulty_exercise = QLineEdit(self.lbl_txts_exercise)
        self.txt_dificulty_exercise.setObjectName(u"txt_dificulty_exercise")
        self.txt_dificulty_exercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.txt_dificulty_exercise)

        self.txt_musculargroups_exercise = QLineEdit(self.lbl_txts_exercise)
        self.txt_musculargroups_exercise.setObjectName(u"txt_musculargroups_exercise")
        self.txt_musculargroups_exercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.txt_musculargroups_exercise)


        self.horizontalLayout_7.addWidget(self.lbl_txts_exercise)

        self.lbl_buttons_exercise = QFrame(self.frame_9)
        self.lbl_buttons_exercise.setObjectName(u"lbl_buttons_exercise")
        self.lbl_buttons_exercise.setFrameShape(QFrame.StyledPanel)
        self.lbl_buttons_exercise.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.lbl_buttons_exercise)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btn_post_exercise = QPushButton(self.lbl_buttons_exercise)
        self.btn_post_exercise.setObjectName(u"btn_post_exercise")
        self.btn_post_exercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.btn_post_exercise)

        self.btn_put_exercise = QPushButton(self.lbl_buttons_exercise)
        self.btn_put_exercise.setObjectName(u"btn_put_exercise")
        self.btn_put_exercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.btn_put_exercise)

        self.btn_del_exercise = QPushButton(self.lbl_buttons_exercise)
        self.btn_del_exercise.setObjectName(u"btn_del_exercise")
        self.btn_del_exercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.btn_del_exercise)

        self.btn_get_exercise = QPushButton(self.lbl_buttons_exercise)
        self.btn_get_exercise.setObjectName(u"btn_get_exercise")
        self.btn_get_exercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.btn_get_exercise)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)


        self.horizontalLayout_7.addWidget(self.lbl_buttons_exercise)


        self.verticalLayout_12.addWidget(self.frame_9)


        self.verticalLayout_10.addWidget(self.frame_8)

        self.pages.addWidget(self.pg_exercise)
        self.pg_user_exercise = QWidget()
        self.pg_user_exercise.setObjectName(u"pg_user_exercise")
        self.horizontalLayout_9 = QHBoxLayout(self.pg_user_exercise)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_12 = QFrame(self.pg_user_exercise)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_txts_userexercise = QFrame(self.frame_14)
        self.lbl_txts_userexercise.setObjectName(u"lbl_txts_userexercise")
        self.lbl_txts_userexercise.setFrameShape(QFrame.StyledPanel)
        self.lbl_txts_userexercise.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.lbl_txts_userexercise)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.txt_userexerciseId = QLineEdit(self.lbl_txts_userexercise)
        self.txt_userexerciseId.setObjectName(u"txt_userexerciseId")
        self.txt_userexerciseId.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.txt_userexerciseId)

        self.txt_iduser_userexercise = QLineEdit(self.lbl_txts_userexercise)
        self.txt_iduser_userexercise.setObjectName(u"txt_iduser_userexercise")
        self.txt_iduser_userexercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.txt_iduser_userexercise)

        self.txt_idexercise_userexercise = QLineEdit(self.lbl_txts_userexercise)
        self.txt_idexercise_userexercise.setObjectName(u"txt_idexercise_userexercise")
        self.txt_idexercise_userexercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.txt_idexercise_userexercise)

        self.txt_date_userexercise = QLineEdit(self.lbl_txts_userexercise)
        self.txt_date_userexercise.setObjectName(u"txt_date_userexercise")
        self.txt_date_userexercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.txt_date_userexercise)

        self.txt_duration_userexercise = QLineEdit(self.lbl_txts_userexercise)
        self.txt_duration_userexercise.setObjectName(u"txt_duration_userexercise")
        self.txt_duration_userexercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.txt_duration_userexercise)

        self.txt_weight_userexercise = QLineEdit(self.lbl_txts_userexercise)
        self.txt_weight_userexercise.setObjectName(u"txt_weight_userexercise")
        self.txt_weight_userexercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.txt_weight_userexercise)

        self.txt_repetitions_userexercise = QLineEdit(self.lbl_txts_userexercise)
        self.txt_repetitions_userexercise.setObjectName(u"txt_repetitions_userexercise")
        self.txt_repetitions_userexercise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.txt_repetitions_userexercise)


        self.horizontalLayout_10.addWidget(self.lbl_txts_userexercise)

        self.lbl_buttons_userexercise = QFrame(self.frame_14)
        self.lbl_buttons_userexercise.setObjectName(u"lbl_buttons_userexercise")
        self.lbl_buttons_userexercise.setFrameShape(QFrame.StyledPanel)
        self.lbl_buttons_userexercise.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.lbl_buttons_userexercise)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.btn_post_userexercise = QPushButton(self.lbl_buttons_userexercise)
        self.btn_post_userexercise.setObjectName(u"btn_post_userexercise")
        self.btn_post_userexercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.btn_post_userexercise)

        self.btn_put_userexercise = QPushButton(self.lbl_buttons_userexercise)
        self.btn_put_userexercise.setObjectName(u"btn_put_userexercise")
        self.btn_put_userexercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.btn_put_userexercise)

        self.btn_del_userexercise = QPushButton(self.lbl_buttons_userexercise)
        self.btn_del_userexercise.setObjectName(u"btn_del_userexercise")
        self.btn_del_userexercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.btn_del_userexercise)

        self.btn_get_userexercise = QPushButton(self.lbl_buttons_userexercise)
        self.btn_get_userexercise.setObjectName(u"btn_get_userexercise")
        self.btn_get_userexercise.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.btn_get_userexercise)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)


        self.horizontalLayout_10.addWidget(self.lbl_buttons_userexercise)


        self.verticalLayout_11.addWidget(self.frame_14)


        self.horizontalLayout_9.addWidget(self.frame_12)

        self.pages.addWidget(self.pg_user_exercise)

        self.verticalLayout_6.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAV 2023.1", None))
        self.btn_user.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.btn_exercise.setText(QCoreApplication.translate("MainWindow", u"Exerc\u00edcios", None))
        self.btn_user_exercise.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio Exerc\u00edcio", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Feito por Lucas Fabrinio com o objetivo de obter a nota na m\u00e1teria de PAV do professor Douglas.</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.txt_userid_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserID", None))
        self.txt_name_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_age_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Idade", None))
        self.txt_gender_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.txt_height_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Altura", None))
        self.txt_weight_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.btn_post_user.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_put_user.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_del_user.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_get_user.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Exerc\u00edcio", None))
        self.txt_exerciseid_exercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ExerciseID", None))
        self.txt_name_exercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_description_exercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.txt_dificulty_exercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dificuldade", None))
        self.txt_musculargroups_exercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Grupo Muscular", None))
        self.btn_post_exercise.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_put_exercise.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_del_exercise.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_get_exercise.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio Exerc\u00edcio", None))
        self.txt_userexerciseId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserExerciseID", None))
        self.txt_iduser_userexercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IdUser", None))
        self.txt_idexercise_userexercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IdExercise", None))
        self.txt_date_userexercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.txt_duration_userexercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dura\u00e7\u00e3o", None))
        self.txt_weight_userexercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.txt_repetitions_userexercise.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repeti\u00e7\u00f5es", None))
        self.btn_post_userexercise.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_put_userexercise.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_del_userexercise.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_get_userexercise.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Lucas Fabrinio Lima Santana", None))
    # retranslateUi

