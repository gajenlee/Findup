from main import *
# from threading import Thread

# ACCESS WINDOW WORKER


class UIAccess(Access):

    # UI DEFINITONS
    def uiTitleBar(self):

        # REMOVE TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

# BACKUP WINDOW WORKER


class UIBackup(Backup):

    # UI DEFINITONS
    def uiTitleBar(self):

        # REMOVE TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.backup_window.setGraphicsEffect(self.shadow)

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())



# MAIN WINDOW WORKER
class UIFunctions(MainWindow):

    # Toggle Menu Button
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # Get Width
            twidth = self.ui.frame_top.width()
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # Set Max Width
            if width == 70 and twidth == 70:
                widthExtended = maxExtend
                self.ui.btn_Toggle.setStyleSheet(u"QPushButton {\n"
                                                 "	background-image: url(./packges/app/items/icons/main-icons/icon_arrow_left.svg);\n"
                                                 "	background-position: left center;\n"
                                                 "  background-repeat: no-repeat;\n"
                                                 "	border: none;\n"
                                                 "	border-left: 22px solid rgb(20, 20, 20);\n"
                                                 "	border-right: 5px solid rgb(20, 20, 20);\n"
                                                 "	background-color: rgb(20, 20, 20);\n"
                                                 "	text-align: left;\n"
                                                 "	padding-left: 45px;\n"
                                                 "  color: #fff;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: rgb(85, 170, 255);\n"
                                                 "	border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {	\n"
                                                 "	background-color: rgb(90, 175, 255);\n"
                                                 "	border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}"
                                                 )
            else:
                widthExtended = standard
                self.ui.btn_Toggle.setStyleSheet(u"QPushButton {\n"
                                                 "	background-image: url(./packges/app/items/icons/main-icons/menu.svg);\n"
                                                 "	background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 "	border: none;\n"
                                                 "	border-left: 22px solid rgb(20, 20, 20);\n"
                                                 "	border-right: 5px solid rgb(20, 20, 20);\n"
                                                 "	background-color: rgb(20, 20, 20);\n"
                                                 "	text-align: left;\n"
                                                 "	padding-left: 45px;\n"
                                                 "color: #fff;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: rgb(85, 170, 255);\n"
                                                 "	border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {	\n"
                                                 "	background-color: rgb(90, 175, 255);\n"
                                                 "	border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}"
                                                 )

            # ANIMATION 1
            self.animation = QPropertyAnimation(
                self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

            # ANIMATION 2
            self.animationToggle = QPropertyAnimation(
                self.ui.frame_top, b"minimumWidth")
            self.animationToggle.setDuration(500)
            self.animationToggle.setStartValue(twidth)
            self.animationToggle.setEndValue(widthExtended)
            self.animationToggle.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animationToggle.start()
    
    def settingHiddenBar(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
        if enabel:

            standard = 200
            minExtend = 45

            standard_hidden_bar = 150
            minExtend_hidden_bar = 0
            current_hidden_height = 0

            icon = QIcon()


            if current_height == 200:
                heightExtended = minExtend
                heightExtended_hidden_bar = minExtend_hidden_bar
                icon.addFile(path_icon_normal)
                
            
            else:
                heightExtended = standard
                heightExtended_hidden_bar = standard_hidden_bar
                icon.addFile(path_icon_active)

            # Set Icon
            btn_obj.setIcon(icon)

            ##### Main Bar #####
            # Minimum Size for Main Frame
            self.animation_hidden = QPropertyAnimation(frame_obj, b"minimumHeight")
            self.animation_hidden.setDuration(500)
            self.animation_hidden.setStartValue(current_height)
            self.animation_hidden.setEndValue(heightExtended)
            self.animation_hidden.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden.start()

            #  Maximum Size Main Frame
            self.animation_hidden_two = QPropertyAnimation(frame_obj, b"maximumHeight")
            self.animation_hidden_two.setDuration(500)
            self.animation_hidden_two.setStartValue(current_height)
            self.animation_hidden_two.setEndValue(heightExtended)
            self.animation_hidden_two.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_two.start()

            ##### Hidden Bar #####
            # Minimum Size For Hidden Frame
            self.animation_hidden_frame = QPropertyAnimation(hidden_frame, b"minimumHeight")
            self.animation_hidden_frame.setDuration(500)
            self.animation_hidden_frame.setStartValue(current_hidden_height)
            self.animation_hidden_frame.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_frame.start()

            # Maximum Size For Hidden Frame
            self.animation_hidden_frame_two = QPropertyAnimation(hidden_frame, b"maximumHeight")
            self.animation_hidden_frame_two.setDuration(500)
            self.animation_hidden_frame_two.setStartValue(current_hidden_height)
            self.animation_hidden_frame_two.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame_two.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_frame_two.start()

    def settingHiddenBar_two(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
        if enabel:

            standard = 250
            minExtend = 45

            standard_hidden_bar = 200
            minExtend_hidden_bar = 0
            current_hidden_height = 0

            icon = QIcon()


            if current_height == 250:
                heightExtended = minExtend
                heightExtended_hidden_bar = minExtend_hidden_bar
                icon.addFile(path_icon_normal)
                
            
            else:
                heightExtended = standard
                heightExtended_hidden_bar = standard_hidden_bar
                icon.addFile(path_icon_active)

            # Set Icon
            btn_obj.setIcon(icon)

            ##### Main Bar #####
            # Minimum Size for Main Frame
            self.animation_hidden = QPropertyAnimation(frame_obj, b"minimumHeight")
            self.animation_hidden.setDuration(500)
            self.animation_hidden.setStartValue(current_height)
            self.animation_hidden.setEndValue(heightExtended)
            self.animation_hidden.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden.start()

            #  Maximum Size Main Frame
            self.animation_hidden_two = QPropertyAnimation(frame_obj, b"maximumHeight")
            self.animation_hidden_two.setDuration(500)
            self.animation_hidden_two.setStartValue(current_height)
            self.animation_hidden_two.setEndValue(heightExtended)
            self.animation_hidden_two.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_two.start()

            ##### Hidden Bar #####
            # Minimum Size For Hidden Frame
            self.animation_hidden_frame = QPropertyAnimation(hidden_frame, b"minimumHeight")
            self.animation_hidden_frame.setDuration(500)
            self.animation_hidden_frame.setStartValue(current_hidden_height)
            self.animation_hidden_frame.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_frame.start()

            # Maximum Size For Hidden Frame
            self.animation_hidden_frame_two = QPropertyAnimation(hidden_frame, b"maximumHeight")
            self.animation_hidden_frame_two.setDuration(500)
            self.animation_hidden_frame_two.setStartValue(current_hidden_height)
            self.animation_hidden_frame_two.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame_two.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_frame_two.start()

    def userSideBar_toggle(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_super_user.width()
            maxExtend = maxWidth
            standard = 0

            if width == 0:
                widthExtended = maxExtend
                self.ui.btn_superuser.setStyleSheet("""
                    QPushButton{
                        color: rgb(255, 255, 255);
                        background-color: rgb(56, 61, 75);
                        border: 2px solid rgb(85, 170, 255);
                        border-radius: 15px;
                    }
                    QPushButton:hover{
                        background-color: rgb(85, 170, 255);
                    }
                    QPushButton:pressed{
                        background-color: rgba(85, 170, 255, 100);
                    }
                """)
            else:
                widthExtended = standard
                self.ui.btn_superuser.setStyleSheet("""
                    QPushButton{
                        color: rgb(255, 255, 255);
                        background-color: rgb(56, 61, 75);
                        border: 0px solid;
                        border-radius: 15px;
                    }
                    QPushButton:hover{
                        background-color: rgb(85, 170, 255);
                    }
                    QPushButton:pressed{
                        background-color: rgba(85, 170, 255, 100);
                    }
                """)

            self.animation = QPropertyAnimation(
                self.ui.frame_super_user, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    # Get Courrent page set

    def home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.btn_lower.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_inter.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_page_home.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/home.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(50, 53, 66);\n"
            "	border-right: 5px solid rgb(50, 53, 66);\n"
            "	background-color: rgb(50, 53, 66);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "   border-bottom-left-radius: 10px;\n"
            "   border-top-left-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_left.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/trash-2.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_search.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/search.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_setting.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/settings.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_analytics.setStyleSheet(u"QPushButton {	\n"
                                                 "	background-image: url(./packges/app/items/icons/24x24/bar-chart.png);\n"
                                                 "	background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 "	border: none;\n"
                                                 "	border-left: 22px solid rgb(20, 20, 20);\n"
                                                 "	border-right: 5px solid rgb(20, 20, 20);\n"
                                                 "	background-color: rgb(20, 20, 20);\n"
                                                 "	text-align: left;\n"
                                                 "	padding-left: 45px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: rgb(85, 170, 255);\n"
                                                 "	border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {	\n"
                                                 "	background-color: rgb(90, 175, 255);\n"
                                                 "	border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}")

    def left(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_left)
        self.ui.btn_lower.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_inter.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_page_home.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/home.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "   border-bottom-left-radius: 10px;\n"
            "   border-top-left-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_left.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/trash-2.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(50, 53, 66);\n"
            "	border-right: 5px solid rgb(50, 53, 66);\n"
            "	background-color: rgb(50, 53, 66);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "   border-bottom-left-radius: 10px;\n"
            "   border-top-left-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_search.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/search.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_setting.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/settings.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_analytics.setStyleSheet(u"QPushButton {	\n"
                                                 "	background-image: url(./packges/app/items/icons/24x24/bar-chart.png);\n"
                                                 "	background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 "	border: none;\n"
                                                 "	border-left: 22px solid rgb(20, 20, 20);\n"
                                                 "	border-right: 5px solid rgb(20, 20, 20);\n"
                                                 "	background-color: rgb(20, 20, 20);\n"
                                                 "	text-align: left;\n"
                                                 "	padding-left: 45px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: rgb(85, 170, 255);\n"
                                                 "	border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {	\n"
                                                 "	background-color: rgb(90, 175, 255);\n"
                                                 "	border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}")

    def search(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_search)
        self.ui.btn_lower.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_inter.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_page_home.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/home.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_left.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/trash-2.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_search.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/search.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(50, 53, 66);\n"
            "	border-right: 5px solid rgb(50, 53, 66);\n"
            "	background-color: rgb(50, 53, 66);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "   border-bottom-left-radius: 10px;\n"
            "   border-top-left-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_setting.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/settings.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_analytics.setStyleSheet(u"QPushButton {	\n"
                                                 "	background-image: url(./packges/app/items/icons/24x24/bar-chart.png);\n"
                                                 "	background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 "	border: none;\n"
                                                 "	border-left: 22px solid rgb(20, 20, 20);\n"
                                                 "	border-right: 5px solid rgb(20, 20, 20);\n"
                                                 "	background-color: rgb(20, 20, 20);\n"
                                                 "	text-align: left;\n"
                                                 "	padding-left: 45px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: rgb(85, 170, 255);\n"
                                                 "	border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {	\n"
                                                 "	background-color: rgb(90, 175, 255);\n"
                                                 "	border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}")

    def setting(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting)
        self.ui.btn_lower.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_inter.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_page_home.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/home.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_left.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/trash-2.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_search.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/search.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_setting.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/settings.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(50, 53, 66);\n"
            "	border-right: 5px solid rgb(50, 53, 66);\n"
            "	background-color: rgb(50, 53, 66);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "   border-bottom-left-radius: 10px;\n"
            "   border-top-left-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_analytics.setStyleSheet(u"QPushButton {	\n"
                                                 "	background-image: url(./packges/app/items/icons/24x24/bar-chart.png);\n"
                                                 "	background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 "	border: none;\n"
                                                 "	border-left: 22px solid rgb(20, 20, 20);\n"
                                                 "	border-right: 5px solid rgb(20, 20, 20);\n"
                                                 "	background-color: rgb(20, 20, 20);\n"
                                                 "	text-align: left;\n"
                                                 "	padding-left: 45px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: rgb(85, 170, 255);\n"
                                                 "	border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {	\n"
                                                 "	background-color: rgb(90, 175, 255);\n"
                                                 "	border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}")

    def analytics(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.analytics)
        self.ui.btn_lower.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_inter.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_page_analytics.setStyleSheet(u"QPushButton {	\n"
                                                 "	background-image: url(./packges/app/items/icons/24x24/bar-chart.png);\n"
                                                 "	background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 "	border: none;\n"
                                                 "	border-left: 22px solid rgb(50, 53, 66);\n"
                                                 "	border-right: 5px solid rgb(50, 53, 66);\n"
                                                 "	background-color: rgb(50, 53, 66);\n"
                                                 "	text-align: left;\n"
                                                 "	padding-left: 45px;\n"
                                                 "   border-bottom-left-radius: 10px;\n"
                                                 "   border-top-left-radius: 10px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: rgb(85, 170, 255);\n"
                                                 "	border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {	\n"
                                                 "	background-color: rgb(90, 175, 255);\n"
                                                 "	border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}")
        self.ui.btn_page_home.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/home.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_left.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/trash-2.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_search.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/search.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "   border-bottom-left-radius: 10px;\n"
            "   border-top-left-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_setting.setStyleSheet(
            u"QPushButton {	\n"
            "	background-image: url(./packges/app/items/icons/main-icons/settings.svg);\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid rgb(20, 20, 20);\n"
            "	border-right: 5px solid rgb(20, 20, 20);\n"
            "	background-color: rgb(20, 20, 20);\n"
            "	text-align: left;\n"
            "	padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "	border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(90, 175, 255);\n"
            "	border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )

    def current_page(self):
        if self.ui.stackedWidget.currentIndex() == 3:
            self.ui.btn_inter.setStyleSheet(
                u"QPushButton{\n"
                "  color: rgb(255, 255, 255);\n"
                "  background-color:  none;\n"
                "  border: 0px solid;\n"
                "  border-radius: 5px;\n"
                "}\n"
                "QPushButton:hover{\n"
                "  background-color: rgb(85, 170, 255);\n"
                "}\n"
                "QPushButton:pressed{\n"
                "  background-color: rgba(85, 170, 255, 100);\n"
                "}"
            )
            self.ui.btn_lower.setStyleSheet(
                u"QPushButton{\n"
                "  color: rgb(255, 255, 255);\n"
                "  background-color:  none;\n"
                "  border: 0px solid;\n"
                "  border-radius: 5px;\n"
                "}\n"
                "QPushButton:hover{\n"
                "  background-color: rgb(85, 170, 255);\n"
                "}\n"
                "QPushButton:pressed{\n"
                "  background-color: rgba(85, 170, 255, 100);\n"
                "}"
            )
            self.ui.btn_page_home.setStyleSheet(
                u"QPushButton {	\n"
                "	background-image: url(./packges/app/items/icons/main-icons/home.svg);\n"
                "	background-position: left center;\n"
                "    background-repeat: no-repeat;\n"
                "	border: none;\n"
                "	border-left: 22px solid rgb(50, 53, 66);\n"
                "	border-right: 5px solid rgb(50, 53, 66);\n"
                "	background-color: rgb(50, 53, 66);\n"
                "	text-align: left;\n"
                "	padding-left: 45px;\n"
                "   border-bottom-left-radius: 10px;\n"
                "   border-top-left-radius: 10px;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background-color: rgb(85, 170, 255);\n"
                "	border-left: 22px solid rgb(85, 170, 255);\n"
                "}\n"
                "QPushButton:pressed {	\n"
                "	background-color: rgb(90, 175, 255);\n"
                "	border-left: 22px solid rgb(90, 175, 255);\n"
                "}"
            )
            self.ui.btn_page_left.setStyleSheet(
                u"QPushButton {	\n"
                "	background-image: url(./packges/app/items/icons/main-icons/trash-2.svg);\n"
                "	background-position: left center;\n"
                "    background-repeat: no-repeat;\n"
                "	border: none;\n"
                "	border-left: 22px solid rgb(20, 20, 20);\n"
                "	border-right: 5px solid rgb(20, 20, 20);\n"
                "	background-color: rgb(20, 20, 20);\n"
                "	text-align: left;\n"
                "	padding-left: 45px;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background-color: rgb(85, 170, 255);\n"
                "	border-left: 22px solid rgb(85, 170, 255);\n"
                "}\n"
                "QPushButton:pressed {	\n"
                "	background-color: rgb(90, 175, 255);\n"
                "	border-left: 22px solid rgb(90, 175, 255);\n"
                "}"
            )
            self.ui.btn_page_search.setStyleSheet(
                u"QPushButton {	\n"
                "	background-image: url(./packges/app/items/icons/main-icons/search.svg);\n"
                "	background-position: left center;\n"
                "    background-repeat: no-repeat;\n"
                "	border: none;\n"
                "	border-left: 22px solid rgb(20, 20, 20);\n"
                "	border-right: 5px solid rgb(20, 20, 20);\n"
                "	background-color: rgb(20, 20, 20);\n"
                "	text-align: left;\n"
                "	padding-left: 45px;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background-color: rgb(85, 170, 255);\n"
                "	border-left: 22px solid rgb(85, 170, 255);\n"
                "}\n"
                "QPushButton:pressed {	\n"
                "	background-color: rgb(90, 175, 255);\n"
                "	border-left: 22px solid rgb(90, 175, 255);\n"
                "}"
            )
            self.ui.btn_setting.setStyleSheet(
                u"QPushButton {	\n"
                "	background-image: url(./packges/app/items/icons/main-icons/settings.svg);\n"
                "	background-position: left center;\n"
                "    background-repeat: no-repeat;\n"
                "	border: none;\n"
                "	border-left: 22px solid rgb(20, 20, 20);\n"
                "	border-right: 5px solid rgb(20, 20, 20);\n"
                "	background-color: rgb(20, 20, 20);\n"
                "	text-align: left;\n"
                "	padding-left: 45px;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background-color: rgb(85, 170, 255);\n"
                "	border-left: 22px solid rgb(85, 170, 255);\n"
                "}\n"
                "QPushButton:pressed {	\n"
                "	background-color: rgb(90, 175, 255);\n"
                "	border-left: 22px solid rgb(90, 175, 255);\n"
                "}"
            )
            self.ui.btn_page_analytics.setStyleSheet(u"QPushButton {	\n"
                                                     "	background-image: url(./packges/app/items/icons/24x24/bar-chart.png);\n"
                                                     "	background-position: left center;\n"
                                                     "    background-repeat: no-repeat;\n"
                                                     "	border: none;\n"
                                                     "	border-left: 22px solid rgb(20, 20, 20);\n"
                                                     "	border-right: 5px solid rgb(20, 20, 20);\n"
                                                     "	background-color: rgb(20, 20, 20);\n"
                                                     "	text-align: left;\n"
                                                     "	padding-left: 45px;\n"
                                                     "}\n"
                                                     "QPushButton:hover {\n"
                                                     "	background-color: rgb(85, 170, 255);\n"
                                                     "	border-left: 22px solid rgb(85, 170, 255);\n"
                                                     "}\n"
                                                     "QPushButton:pressed {	\n"
                                                     "	background-color: rgb(90, 175, 255);\n"
                                                     "	border-left: 22px solid rgb(90, 175, 255);\n"
                                                     "}")

    def addInter_page(self):
        self.ui.btn_inter.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  rgb(57, 62, 76);\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_lower.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_page_home.setStyleSheet(
            u"QPushButton { \n"
            "   background-image: url(./packges/app/items/icons/main-icons/home.svg);\n"
            "   background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "   border: none;\n"
            "   border-left: 22px solid rgb(20, 20, 20);\n"
            "   border-right: 5px solid rgb(20, 20, 20);\n"
            "   background-color: rgb(20, 20, 20);\n"
            "   text-align: left;\n"
            "   padding-left: 45px;\n"
            "   border-bottom-left-radius: 10px;\n"
            "   border-top-left-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(85, 170, 255);\n"
            "   border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {  \n"
            "   background-color: rgb(90, 175, 255);\n"
            "   border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_left.setStyleSheet(
            u"QPushButton { \n"
            "   background-image: url(./packges/app/items/icons/main-icons/trash-2.svg);\n"
            "   background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "   border: none;\n"
            "   border-left: 22px solid rgb(20, 20, 20);\n"
            "   border-right: 5px solid rgb(20, 20, 20);\n"
            "   background-color: rgb(20, 20, 20);\n"
            "   text-align: left;\n"
            "   padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(85, 170, 255);\n"
            "   border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {  \n"
            "   background-color: rgb(90, 175, 255);\n"
            "   border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_search.setStyleSheet(
            u"QPushButton { \n"
            "   background-image: url(./packges/app/items/icons/main-icons/search.svg);\n"
            "   background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "   border: none;\n"
            "   border-left: 22px solid rgb(20, 20, 20);\n"
            "   border-right: 5px solid rgb(20, 20, 20);\n"
            "   background-color: rgb(20, 20, 20);\n"
            "   text-align: left;\n"
            "   padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(85, 170, 255);\n"
            "   border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {  \n"
            "   background-color: rgb(90, 175, 255);\n"
            "   border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_setting.setStyleSheet(
            u"QPushButton { \n"
            "   background-image: url(./packges/app/items/icons/main-icons/settings.svg);\n"
            "   background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "   border: none;\n"
            "   border-left: 22px solid rgb(20, 20, 20);\n"
            "   border-right: 5px solid rgb(20, 20, 20);\n"
            "   background-color: rgb(20, 20, 20);\n"
            "   text-align: left;\n"
            "   padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(85, 170, 255);\n"
            "   border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {  \n"
            "   background-color: rgb(90, 175, 255);\n"
            "   border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_analytics.setStyleSheet(u"QPushButton {    \n"
                                                 "   background-image: url(./packges/app/items/icons/24x24/bar-chart.png);\n"
                                                 "   background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 "   border: none;\n"
                                                 "   border-left: 22px solid rgb(20, 20, 20);\n"
                                                 "   border-right: 5px solid rgb(20, 20, 20);\n"
                                                 "   background-color: rgb(20, 20, 20);\n"
                                                 "   text-align: left;\n"
                                                 "   padding-left: 45px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "   background-color: rgb(85, 170, 255);\n"
                                                 "   border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {  \n"
                                                 "   background-color: rgb(90, 175, 255);\n"
                                                 "   border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}"
                                                 )

    def addLower_page(self):
        self.ui.btn_lower.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  rgb(57, 62, 76);\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_inter.setStyleSheet(
            u"QPushButton{\n"
            "  color: rgb(255, 255, 255);\n"
            "  background-color:  none;\n"
            "  border: 0px solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "  background-color: rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  background-color: rgba(85, 170, 255, 100);\n"
            "}"
        )
        self.ui.btn_page_home.setStyleSheet(
            u"QPushButton { \n"
            "   background-image: url(./packges/app/items/icons/main-icons/home.svg);\n"
            "   background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "   border: none;\n"
            "   border-left: 22px solid rgb(20, 20, 20);\n"
            "   border-right: 5px solid rgb(20, 20, 20);\n"
            "   background-color: rgb(20, 20, 20);\n"
            "   text-align: left;\n"
            "   padding-left: 45px;\n"
            "   border-bottom-left-radius: 10px;\n"
            "   border-top-left-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(85, 170, 255);\n"
            "   border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {  \n"
            "   background-color: rgb(90, 175, 255);\n"
            "   border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_left.setStyleSheet(
            u"QPushButton { \n"
            "   background-image: url(./packges/app/items/icons/main-icons/trash-2.svg);\n"
            "   background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "   border: none;\n"
            "   border-left: 22px solid rgb(20, 20, 20);\n"
            "   border-right: 5px solid rgb(20, 20, 20);\n"
            "   background-color: rgb(20, 20, 20);\n"
            "   text-align: left;\n"
            "   padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(85, 170, 255);\n"
            "   border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {  \n"
            "   background-color: rgb(90, 175, 255);\n"
            "   border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_search.setStyleSheet(
            u"QPushButton { \n"
            "   background-image: url(./packges/app/items/icons/main-icons/search.svg);\n"
            "   background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "   border: none;\n"
            "   border-left: 22px solid rgb(20, 20, 20);\n"
            "   border-right: 5px solid rgb(20, 20, 20);\n"
            "   background-color: rgb(20, 20, 20);\n"
            "   text-align: left;\n"
            "   padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(85, 170, 255);\n"
            "   border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {  \n"
            "   background-color: rgb(90, 175, 255);\n"
            "   border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_setting.setStyleSheet(
            u"QPushButton { \n"
            "   background-image: url(./packges/app/items/icons/main-icons/settings.svg);\n"
            "   background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "   border: none;\n"
            "   border-left: 22px solid rgb(20, 20, 20);\n"
            "   border-right: 5px solid rgb(20, 20, 20);\n"
            "   background-color: rgb(20, 20, 20);\n"
            "   text-align: left;\n"
            "   padding-left: 45px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "   background-color: rgb(85, 170, 255);\n"
            "   border-left: 22px solid rgb(85, 170, 255);\n"
            "}\n"
            "QPushButton:pressed {  \n"
            "   background-color: rgb(90, 175, 255);\n"
            "   border-left: 22px solid rgb(90, 175, 255);\n"
            "}"
        )
        self.ui.btn_page_analytics.setStyleSheet(u"QPushButton {    \n"
                                                 "   background-image: url(./packges/app/items/icons/24x24/bar-chart.png);\n"
                                                 "   background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 "   border: none;\n"
                                                 "   border-left: 22px solid rgb(20, 20, 20);\n"
                                                 "   border-right: 5px solid rgb(20, 20, 20);\n"
                                                 "   background-color: rgb(20, 20, 20);\n"
                                                 "   text-align: left;\n"
                                                 "   padding-left: 45px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "   background-color: rgb(85, 170, 255);\n"
                                                 "   border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {  \n"
                                                 "   background-color: rgb(90, 175, 255);\n"
                                                 "   border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}"
                                                 )
