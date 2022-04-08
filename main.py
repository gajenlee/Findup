from tabnanny import check
from packges.importer.importer import *
from packges.app.uis.access import ui_access
from packges.app.uis.backup import ui_backup
from packges.app.uis.create import ui_create
from packges.app.uis.login import ui_login
from packges.app.uis.main import ui_main
from packges.active.activer import *
from packges.store.store import *
from packges.circular_progress.circular_progress import *


# GLOBAL VALUES
secure = Secure()
SUPERUSER = 'Super-User'
INTERUSER = 'Inter-User'
LOWERUSERORDINARY = 'Lower-User-Ordinary'
LOWERUSERADVANCED = "Lower-User-Advanced"
LOWERUSERPRIMARY = "Lower-User-Primary"


# Global Path
PATH_SAVE_FILE = os.path.join(f"C:/Users/{os.getlogin()}/")

# Search Name Store Index and Level
NAME_SEARCH_INTER_ACTIVE = []
NAME_SEARCH_LOWER_ACTIVE = []
NAME_SEARCH_INTER_LEFT = []
NAME_SEARCH_LOWER_LEFT = []

# Search Roll Store Index and Level
ROLL_SEARCH_INTER_ACTIVE = []
ROLL_SEARCH_LOWER_ACTIVE = []
ROLL_SEARCH_INTER_LEFT = []
ROLL_SEARCH_LOWER_LEFT = []

# Search Name Store Index and Level For Advance Lowers
NAME_SEARCH_ADVANCE_LOWER = []
NAME_SEARCH_ADVANCE_LOWER_LEFT = []

NAME_SEARCH_PRIMARY_LOWER = []
NAME_SEARCH_PRIMARY_LOWER_LEFT = []


# Search Roll Store Index and levels
ROLL_SEARCH_ADVANCED_LOWER = []
ROLL_SEARCH_ADVANCED_LOWER_LEFT = []

ROLL_SEARCH_PRIMARY_LOWER = []
ROLL_SEARCH_PRIMARY_LOWER_LEFT = []


# Find user for active status
randomzies_number_for_inter = []
randomzies_number_for_lower = []

# Find user for left active status
randomzies_number_for_inter_left = []
randomzies_number_for_lower_left = []


# Random Lower User List
ABLE_PRIMARY_LOWER = []
ABLE_ODRINARY_LOWER = []
ABLE_ADVANCED_LOWER = []

RANDOM_LOWER_PRIMARY = []
RANDOM_LOWER_ODRINAEY = []
RANDOM_INTER = []
RANDOM_LOWER_ADVANCED = []

RANDOM_LOWER_PRIMARY_LEFT = []
RANDOM_LOWER_ODRINAEY_LEFT = []
RANDOM_INTER_LEFT = []
RANDOM_LOWER_ADVANCED_LEFT = []

# Check Email ID


def email_check(email):
    if email != '':
        listEmails = re.findall('\S+@\S+', email)
        if listEmails == []:
            return 'none'
        else:
            if len(listEmails) == 1:
                return email
    else:
        email = None
    return email

# Check Phone Number


def phone_number_checker(number_of_user):
    if number_of_user != '':
        t = re.compile(r"[0-9]+")
        check_number = t.findall(number_of_user)
        if check_number:
            if len(check_number[-1]) == 10 or len(check_number[-1]) == 11:
                if check_number[-1][:2] == '07' or (check_number[-1][:2] == '94' and check_number[-1][2:4][0] == '7'):
                    if len(check_number[-1]) == 11:
                        check_number[-1] = "+" + check_number[-1]
                    return check_number[-1]
    return False

#############################################################################################
# ACCESS DIALOG WINDOW


class Access(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Findup | Access")
        self.ui = ui_access.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        icon = QIcon()
        icon.addFile(u"./packges/app/items/img/findupnew_window.png")
        self.setWindowIcon(icon)

        def moveWindow(event):

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.frame_title_bar.mouseMoveEvent = moveWindow
        # SET DEFINITIONS
        UIAccess.uiTitleBar(self)

        # Set Icons
        setIcon_line(self.ui.lineEdit_current_password,
                     u"./packges/app/items/icons/16x16/cil-lock-locked.png")

        # btn value
        self.ui.btn_verify.clicked.connect(lambda: self.check_password())

        # SHOW -- GUI
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def check_password(self):
        data = Store.read_json()
        userInput = self.ui.lineEdit_current_password.text()


####################################################################################
# LOGIN DIALOG WINDOW

counter = 0


class Login(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle(u"Findup | Login")
        self.ui = ui_login.Ui_MainWindow()
        self.ui.setupUi(self)

        self.__path = os.path.join(os.getcwd())
        if "packges" in os.listdir(self.__path):
            self.ui.label_logo.setText(
                f"<html><head/><body><p><img src=\"./packges/app/items/img/findupnew.png\"/></p></body></html>"
            )

        icon = QIcon()
        icon.addFile(u"./packges/app/items/img/findupnew_window.png")
        self.setWindowIcon(icon)

        # Remove frame
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set Progress Bar
        self.progress = CircularProgress()
        self.progress.width = 258
        self.progress.height = 258
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 25
        self.progress.add_shadow(True)
        self.progress.progress_width = 5
        self.progress.progress_color = QColor("#31446b")
        self.progress.text_color = QColor("#E6E6E6")
        self.progress.bg_color = QColor("#222222")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()

        # Set Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.background.setGraphicsEffect(self.shadow)

        # Icon For Name
        setIcon_line(self.ui.lineEdit_name,
                     u"./packges/app/items/icons/16x16/cil-user.png")

        # Icon For Password
        setIcon_line(self.ui.lineEdit_pass,
                     u"./packges/app/items/icons/16x16/cil-lock-locked.png")

        # Set Window Event
        self.keyPressEvent = self.check_login_btn

        self.show()

    def check_login_btn(self, event):

        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.lineEdit_name.text()
            password = self.ui.lineEdit_pass.text()

            __data = Store.read_super_user()
            __username = secure.decrypt(
                __data[SUPERUSER][-1]['Name'][-2], __data[SUPERUSER][-1]['Name'][-1])
            __password = secure.decrypt(
                __data[SUPERUSER][-1]['Password'][-2], __data[SUPERUSER][-1]['Password'][-1])
            __email = secure.decrypt(
                __data[SUPERUSER][-1]['E-Mail'][-2], __data[SUPERUSER][-1]['E-Mail'][-1])

            def prosses():
                self.animation_login()
                self.timer = QTimer()
                self.timer.timeout.connect(self.update)
                self.timer.start(35)

            if (username == __username or username == __email) and __password == password:
                QTimer.singleShot(1200, lambda: prosses())

            else:
                self.shacke_window()
                self.ui.lineEdit_name.setStyleSheet("#lineEdit_name {\n"
                                                    "    border: 0px solid;\n"
                                                    "    background-color: rgb(37, 38, 48);\n"
                                                    "    border-radius: 10px;\n"
                                                    "    padding-left: 10px;\n"
                                                    "    color: white;\n"
                                                    "}\n"
                                                    "#lineEdit_name:hover {border: 3px solid rgb(39, 53, 84);}\n"
                                                    "#lineEdit_name:focus {border: 3px solid rgb(255, 61, 77);}"
                                                    )
                self.ui.lineEdit_pass.setStyleSheet("#lineEdit_pass {\n"
                                                    "    border: 0px solid;\n"
                                                    "    background-color: rgb(37, 38, 48);\n"
                                                    "    border-radius: 10px;\n"
                                                    "    padding-left: 10px;\n"
                                                    "    color: white;\n"
                                                    "}\n"
                                                    "#lineEdit_pass:hover {border: 3px solid rgb(39, 53, 84);}\n"
                                                    "#lineEdit_pass:focus {border: 3px solid rgb(255, 61, 77);}"
                                                    )
        elif event.key() == Qt.Key_Escape or event.key == Qt.Key_Enter:
            self.close()

    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()
            main = MainWindow()
            self.close()

        # INCREASE COUNTER
        counter += 1

    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(
            QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(
            QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def shacke_window(self):
        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(
            actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(
            actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(
            actual_pos.x(), actual_pos.y()))

###############################################################################
# CREATE WINDOW DIALOG


class Create(QMainWindow):

    counter = 0

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle(u"Findup | Create")
        self.ui = ui_create.Ui_MainWindow()
        self.ui.setupUi(self)

        self.__path = os.path.join(os.getcwd())
        if "packges" in os.listdir(self.__path):
            self.ui.label_logo.setText(
                f"<html><head/><body><p><img src=\"./packges/app/items/img/findupnew.png\"/></p></body></html>"
            )

        icon = QIcon()
        icon.addFile(u"./packges/app/items/img/findupnew_window.png")
        self.setWindowIcon(icon)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Progress
        self.progress = CircularProgress()
        self.progress.width = 258
        self.progress.height = 258
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 25
        self.progress.add_shadow(True)
        self.progress.progress_width = 5
        self.progress.progress_color = QColor("#31446b")
        self.progress.text_color = QColor("#E6E6E6")
        self.progress.bg_color = QColor("#222222")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()

        # Shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.background.setGraphicsEffect(self.shadow)

        # Icon For Name
        setIcon_line(self.ui.lineEdit_name,
                     u"./packges/app/items/icons/16x16/cil-user.png")

        # Icon For Password
        setIcon_line(self.ui.lineEdit_pass,
                     u"./packges/app/items/icons/16x16/cil-lock-locked.png")
        setIcon_line(self.ui.lineEdit_con_pass,
                     u"./packges/app/items/icons/16x16/cil-lock-locked.png")

        # Icon For Contact Number
        setIcon_line(self.ui.lineEdit_contact,
                     u"./packges/app/items/icons/16x16/phone-39-16.png")

        # Icon For Contact Number
        setIcon_line(self.ui.lineEdit_email,
                     u"./packges/app/items/icons/16x16/email-11-16.png")

        self.keyPressEvent = self.cheked_userInput

        # SHOW
        self.show()

    # CAEKED USER INPUT
    def cheked_userInput(self, event):

        if event.key() == Qt.Key_Return or event.key() == Qt.Key() == Qt.Key_Enter:

            # CHAKE USER NAME ===> ERROR
            if self.checkUserName(self.ui.lineEdit_name.text()) != True:
                self.shacke_window()
                self.ui.lineEdit_name.setStyleSheet("#lineEdit_name {\n"
                                                    "    border: 0px solid;\n"
                                                    "    background-color: rgb(37, 38, 48);\n"
                                                    "    border-radius: 10px;\n"
                                                    "    padding-left: 10px;\n"
                                                    "    color: white;\n"
                                                    "}\n"
                                                    "#lineEdit_name:hover {border: 3px solid rgb(39, 53, 84);}\n"
                                                    "#lineEdit_name:focus {border: 3px solid rgb(255, 61, 77);}"
                                                    )

            # CAEKE USER PASSWORD ===> ERROR
            elif len(self.ui.lineEdit_pass.text()) < 6:
                self.shacke_window()
                self.ui.lineEdit_pass.setStyleSheet("#lineEdit_pass {\n"
                                                    "    border: 0px solid;\n"
                                                    "    background-color: rgb(37, 38, 48);\n"
                                                    "    border-radius: 10px;\n"
                                                    "    padding-left: 10px;\n"
                                                    "    color: white;\n"
                                                    "}\n"
                                                    "#lineEdit_pass:hover {border: 3px solid rgb(39, 53, 84);}\n"
                                                    "#lineEdit_pass:focus {border: 3px solid rgb(255, 61, 77);}"
                                                    )

            # CAKED USER PASSWORD AND CONFIRM PASSWORD ==> ERROR
            elif self.ui.lineEdit_pass.text() != self.ui.lineEdit_con_pass.text():
                self.shacke_window()
                self.ui.lineEdit_con_pass.setStyleSheet("#lineEdit_con_pass {\n"
                                                        "    border: 0px solid;\n"
                                                        "    background-color: rgb(37, 38, 48);\n"
                                                        "    border-radius: 10px;\n"
                                                        "    padding-left: 10px;\n"
                                                        "    color: white;\n"
                                                        "}\n"
                                                        "#lineEdit_con_pass:hover {border: 3px solid rgb(39, 53, 84);}\n"
                                                        "#lineEdit_con_pass:focus {border: 3px solid rgb(255, 61, 77);}"
                                                        )

            # EMAIL ID ===> ERROR
            elif self.checkEmailID(self.ui.lineEdit_email.text()) != False:
                self.shacke_window()
                self.ui.lineEdit_email.setStyleSheet("#lineEdit_email {\n"
                                                     "    border: 0px solid;\n"
                                                     "    background-color: rgb(37, 38, 48);\n"
                                                     "    border-radius: 10px;\n"
                                                     "    padding-left: 10px;\n"
                                                     "    color: white;\n"
                                                     "}\n"
                                                     "#lineEdit_email:hover {border: 3px solid rgb(39, 53, 84);}\n"
                                                     "#lineEdit_email:focus {border: 3px solid rgb(255, 61, 77);}"
                                                     )

            else:
                def updater():

                    global __data
                    ReadBinary.write_binary_file('True')

                    # Get all information
                    __userName = self.ui.lineEdit_name.text()
                    __password = self.ui.lineEdit_pass.text()
                    __email = self.ui.lineEdit_email.text()
                    __contact_number = self.ui.lineEdit_contact.text()

                    # Encrypt data
                    __userName, __userNameKey = secure.encrypt(__userName)
                    __password, __passwordKey = secure.encrypt(__password)
                    __email, __emailKey = secure.encrypt(__email)
                    __contact_number, __contact_numberKey = secure.encrypt(
                        __contact_number)

                    # Set Super User Data
                    __data = {
                        'Name': [__userName, __userNameKey],
                        'Password': [__password, __passwordKey],
                        'E-Mail': [__email, __emailKey],
                        'Contact-Number': [__contact_number, __contact_numberKey]
                    }

                updaterThread = Thread(target=updater)
                updaterThread.start()
                updaterThread.join()

                # set init function
                tread_ = Thread(target=Store.init)
                tread_.start()
                tread_.join()

                write_thread = Thread(target=Store.update_super_user,
                                      args=[__data])
                write_thread.start()
                write_thread.join()

                # Set Config into True
                binary_thread = Thread(
                    target=ReadBinary.write_binary_file, args=['True'])
                binary_thread.start()
                binary_thread.join()

                self.animation_login()
                self.timer = QTimer()
                self.timer.timeout.connect(self.update)
                self.timer.start(35)

        elif event.key() == Qt.Key_Escape or event.key == Qt.Key_Enter:
            self.close()

    def shacke_window(self):
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(
            actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(
            actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(
            actual_pos.x(), actual_pos.y()))

    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(
            QRect(0, 30, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(
            QRect(0, -410, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def update(self):
        self.progress.set_value(self.counter)
        if self.counter >= 100:
            self.timer.stop()
            main = MainWindow()
            self.close()

        self.counter += 1

    # CHECK EMAIL ID
    def checkEmailID(self, email):
        if email == '':
            return True
        else:
            email_confirm = re.findall('\S+@\S+', email)
            if email_confirm == []:
                return True
            else:
                if len(email) == 1:
                    return True
        return False

    # CHECK USER NAME
    def checkUserName(self, userName):
        if userName != '':
            if 97 <= ord(userName[0]) <= 122:
                if len(userName) >= 5:
                    return True
        return False


#############################################################################
# Backup Window
class Backup(QDialog):

    # Backup data save path
    path_of_backup = os.path.join(
        f"C:/Users/{os.getlogin()}/Documents/Findup/")

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle(u"Findup | Backup")
        self.ui = ui_backup.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        icon = QIcon()
        icon.addFile(u"./packges/app/items/img/findupnew_window.png")
        self.setWindowIcon(icon)

        self.ui.lineEdit_path.setText(self.path_of_backup)

        def moveWindow(event):

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.frame_titile_bar.mouseMoveEvent = moveWindow

        # Item add
        self.ui.comboBox.addItem("Backup All Data In CSV")
        self.ui.comboBox.addItem("Backup Inter Data Only In CSV")

        self.ui.comboBox.addItem("Backup Lower Ordinary Data Only In CSV")
        self.ui.comboBox.addItem("Backup Lower Advanced Data Only In CSV")
        self.ui.comboBox.addItem("BAckup Lower Primary Data Only In CSV")

        self.ui.comboBox.addItem("Backup Inter Left Data Only In CSV")

        self.ui.comboBox.addItem("Backup Lower Ordinary Left Data Only In CSV")
        self.ui.comboBox.addItem("Backup Lower Primary Left Data Only In CSV ")
        self.ui.comboBox.addItem("Backup Lower Advanced Left Data Only In CSV")

        # get current page
        UIBackup.uiTitleBar(self)

        # Connect into Backup Fuction
        self.ui.btn_backup.clicked.connect(
            lambda: Thread(self.backupMain()).start())

        self.ui.open_folder.clicked.connect(lambda: self.setPath_entry())

        # SHOW window
        self.show()

    # APP MOVE EVENTS
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def setPath_entry(self):
        path = QFileDialog.getExistingDirectory(
            None, 'Select Backup Folder: ', "C:\\Users\\Documents\\", QFileDialog.ShowDirsOnly)
        if path != "" or path != None:
            self.ui.lineEdit_path.setText(path)
        else:
            self.ui.lineEdit_path.setText(self.path_of_backup)

    # Create the Backup File
    def makeDirsForBackupData(self):

        getPath = self.ui.lineEdit_path.text()
        getPath = os.path.join(getPath)
        try:
            listDir = [
                'Backup', 'Inter',  'Inter-Left', 'Inter-Active', "Lower", 'Lower-Active', "Lower-Left", 'Lower-Ordinary',
                "Lower-Primary",  "Lower-Advanced", 'Level - 0', 'Level - '
            ]

            def createPath(file, supFile, supsupFile, supsupsup=None, lastFile=None):
                if lastFile != None and supsupsup != None:
                    path = os.path.join(
                        getPath + f"/{file}/{supFile}/{supsupFile}/{supsupsup}/{lastFile}")
                elif supsupsup != None:
                    path = os.path.join(
                        getPath + f"/{file}/{supFile}/{supsupFile}/{supsupsup}")
                else:
                    path = os.path.join(
                        getPath + f"/{file}/{supFile}/{supsupFile}")
                os.makedirs(path)

            # File Create
            createPath(listDir[0], listDir[1], listDir[2])
            createPath(listDir[0], listDir[1], listDir[3])

            # lower ordinary
            createPath(listDir[0], listDir[4], listDir[5], listDir[7])
            createPath(listDir[0], listDir[4], listDir[6], listDir[7])

            # lower primary
            createPath(listDir[0], listDir[4], listDir[5], listDir[8])
            createPath(listDir[0], listDir[4], listDir[6], listDir[8])

            # lower advanced
            createPath(listDir[0], listDir[4], listDir[5], listDir[9])
            createPath(listDir[0], listDir[4], listDir[6], listDir[9])

            for count in range(1, 14):
                if count > 0 and count < 6:
                    createPath(listDir[0], listDir[4], listDir[5],
                               listDir[8], listDir[10] + f"{count:01}")

                elif count > 5:
                    if count == 10 or count == 11:
                        createPath(listDir[0], listDir[4], listDir[5],
                                   listDir[7], listDir[11] + str(count))
                    elif count == 12 or count == 13:
                        createPath(listDir[0], listDir[4], listDir[5],
                                   listDir[9], listDir[11] + str(count))
                    else:
                        createPath(listDir[0], listDir[4], listDir[5],
                                   listDir[7], listDir[10] + f"{count:01}")

            data = Store.read_json()
            levelsOfAdvanced = [name for name in data[LOWERUSERADVANCED]]
            streemsOfAdvanced = [
                name for name in data[LOWERUSERADVANCED][levelsOfAdvanced[-1]]]
            path = os.path.join(
                getPath + "/Backup/Lower/Lower-Active/Lower-Advanced")
            for level in levelsOfAdvanced:
                for streem in streemsOfAdvanced:
                    os.makedirs(path + "/" + level + "/" + streem)

        except FileExistsError as a:
            pass

    # Backup File Main
    def backupMain(self):

        getCurrentIndex = self.ui.comboBox.currentIndex()
        main = Thread(target=self.makeDirsForBackupData)
        main.start()
        if getCurrentIndex == 0:
            main.join()
            Thread(target=self.backupAllDataIntoCSV).start()
        elif getCurrentIndex == 1:
            main.join()
            Thread(target=self.backupInterDataIntoCSV).start()
        elif getCurrentIndex == 2:
            main.join()
            Thread(target=self.backupLowerOrdinaryDataIntoCSV).start()
        elif getCurrentIndex == 3:
            main.join()
            Thread(target=self.backupLowerAdvancedDataIntoCSV).start()

        elif getCurrentIndex == 4:
            main.join()
            Thread(target=self.backupLowerPrimaryDataIntoCSV).start()
        elif getCurrentIndex == 5:
            main.join()
            Thread(target=self.backupInterLeftDataIntoCSV).start()
        elif getCurrentIndex == 6:
            main.join()
            Thread(target=self.backupLowerOrdinaryLeftDataIntoCSV).start()
        elif getCurrentIndex == 7:
            main.join()
            Thread(target=self.backupLowerPrimaryLeftDataIntoCSV).start()
        else:
            main.join()
            Thread(target=self.backupLowerAdvancedLeftDataIntoCSV).start()

    # Backup All Data
    def backupAllDataIntoCSV(self):
        Thread(target=self.backupInterDataIntoCSV).start()
        Thread(target=self.backupLowerOrdinaryDataIntoCSV).start()
        Thread(target=self.backupInterLeftDataIntoCSV).start()
        Thread(target=self.backupLowerOrdinaryLeftDataIntoCSV).start()
        Thread(target=self.backupLowerPrimaryDataIntoCSV).start()
        Thread(target=self.backupLowerAdvancedDataIntoCSV).start()
        Thread(target=self.backupLowerPrimaryLeftDataIntoCSV).start()
        Thread(target=self.backupLowerAdvancedLeftDataIntoCSV).start()

    def backupLowerPrimaryDataIntoCSV(self):
        getPath = self.ui.lineEdit_path.text()
        __fileName = "Lower-Primary.csv"
        path = os.path.join(
            getPath + "/Backup/Lower/Lower-Active/Lower-Primary")

        if "data.json" in os.listdir(PATH_STORE_DATA_DIR):
            data = Store.read_json()
            listOfPrimaryLower = data[LOWERUSERPRIMARY]
            levelsOfPrimaryList = [name for name in listOfPrimaryLower]
            for levels in levelsOfPrimaryList:
                if listOfPrimaryLower[levels] != []:
                    for count in range(len(listOfPrimaryLower[levels])):
                        if listOfPrimaryLower[levels][count]["E-Mail"] == None:
                            __email = None
                        else:
                            __email = secure.decrypt(
                                listOfPrimaryLower[levels][count]["E-Mail"][-2], listOfPrimaryLower[levels][count]["E-Mail"][-1])

                        __name = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Name"][-2], listOfPrimaryLower[levels][count]["Name"][-1])
                        __roll = listOfPrimaryLower[levels][count]["Roll"]
                        __address = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Address"][-2], listOfPrimaryLower[levels][count]["Address"][-1])
                        __level = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Level"][-2], listOfPrimaryLower[levels][count]["Level"][-1])
                        __father_name = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Father-Name"][-2], listOfPrimaryLower[levels][count]["Father-Name"][-1])
                        __mather_name = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Mather-Name"][-2], listOfPrimaryLower[levels][count]["Mather-Name"][-1])
                        __parent_conta = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Contact-Number"][-2], listOfPrimaryLower[levels][count]["Contact-Number"][-1])
                        __dob = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Date-of-Birth"][-2], listOfPrimaryLower[levels][count]["Date-of-Birth"][-1])
                        __relig_num = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Registration-Number"][-2], listOfPrimaryLower[levels][count]["Registration-Number"][-1])
                        __religion = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Religion"][-2], listOfPrimaryLower[levels][count]["Religion"][-1])
                        __gender = secure.decrypt(
                            listOfPrimaryLower[levels][count]["Gender"][-2], listOfPrimaryLower[levels][count]["Gender"][-1])

                        if __fileName not in os.listdir(path):
                            with open(os.path.join(path+'/'+levels+'/'+__fileName), 'w') as file:
                                writeCsv = csv.writer(file)
                                writeCsv.writerow(['Roll', 'Name', 'Address', 'E-Mail', 'Level', 'Father-Name', 'Mather-Name',
                                                   'Contact-Number', 'Date-of-Birth', 'Registration-Number', 'Religion', 'Gender']
                                                  )
                                writeCsv.writerow(
                                    [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                        __parent_conta, __dob, __relig_num, __religion, __gender]
                                )
                        else:
                            with open(os.path.join(path+'/'+levels+'/'+__fileName), 'a') as file:
                                writeCsv = csv.writer(file)
                                writeCsv.writerow(
                                    [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                        __parent_conta, __dob, __relig_num, __religion, __gender]
                                )

        # Analtices For Backup Data
        path = os.path.join(path + '/')
        if __fileName in os.listdir(path):
            file_path = os.path.join(path + __fileName)
            dataFrame = pd.read_csv(file_path)
            dataFrame.drop_duplicates(inplace=True)
            dataFrame.to_csv(file_path, index=False)

    def backupLowerAdvancedDataIntoCSV(self):
        getPath = self.ui.lineEdit_path.text()
        __fileName = "Lower-Advanced.csv"
        path = os.path.join(
            getPath + "/Backup/Lower/Lower-Active/Lower-Advanced")

        if "data.json" in os.listdir(PATH_STORE_DATA_DIR):
            data = Store.read_json()
            listOfAdvancedLower = data[LOWERUSERADVANCED]
            levelsOfPrimaryList = [name for name in listOfAdvancedLower]
            streemsOfAdvancdList = [
                streem for streem in listOfAdvancedLower[levelsOfPrimaryList[-1]]]
            for levels in levelsOfPrimaryList:
                for streemOfLower in streemsOfAdvancdList:
                    if listOfAdvancedLower[levels][streemOfLower] != []:
                        for count in range(len(listOfAdvancedLower[levels][streemOfLower])):

                            if listOfAdvancedLower[levels][streemOfLower][count]["E-Mail"] == None:
                                __email = None
                            else:
                                __email = secure.decrypt(
                                    listOfAdvancedLower[levels][streemOfLower][count]["E-Mail"][-2], listOfAdvancedLower[levels][streemOfLower][count]["E-Mail"][-1])

                            __name = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Name"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Name"][-1])
                            __roll = listOfAdvancedLower[levels][streemOfLower][count]["Roll"]
                            __address = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Address"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Address"][-1])
                            __level = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Level"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Level"][-1])
                            __father_name = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Father-Name"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Father-Name"][-1])
                            __mather_name = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Mather-Name"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Mather-Name"][-1])
                            __parent_conta = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Contact-Number"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Contact-Number"][-1])
                            __dob = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Date-of-Birth"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Date-of-Birth"][-1])
                            __relig_num = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Registration-Number"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Registration-Number"][-1])
                            __religion = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Religion"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Religion"][-1])
                            __gender = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Gender"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Gender"][-1])
                            __streem = secure.decrypt(
                                listOfAdvancedLower[levels][streemOfLower][count]["Stream"][-2], listOfAdvancedLower[levels][streemOfLower][count]["Stream"][-1])

                            if __fileName not in os.listdir(path):
                                with open(os.path.join(path+'/'+levels+'/'+streemOfLower+'/'+__fileName), 'w') as file:
                                    writeCsv = csv.writer(file)
                                    writeCsv.writerow(['Roll', 'Name', 'Address', 'E-Mail', 'Level', 'Father-Name', 'Mather-Name',
                                                       'Contact-Number', 'Date-of-Birth', 'Registration-Number', 'Religion', 'Gender', 'Stream']
                                                      )
                                    writeCsv.writerow(
                                        [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                            __parent_conta, __dob, __relig_num, __religion, __gender, __streem]
                                    )
                            else:
                                with open(os.path.join(path+'/'+levels+'/'+streemOfLower+'/'+__fileName), 'a') as file:
                                    writeCsv = csv.writer(file)
                                    writeCsv.writerow(
                                        [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                            __parent_conta, __dob, __relig_num, __religion, __gender, __streem]
                                    )
        # Analtices For Backup Data
        path = os.path.join(path + '/')
        if __fileName in os.listdir(path):
            file_path = os.path.join(path + __fileName)
            dataFrame = pd.read_csv(file_path)
            dataFrame.drop_duplicates(inplace=True)
            dataFrame.to_csv(file_path, index=False)

    def backupLowerPrimaryLeftDataIntoCSV(self):
        getPath = self.ui.lineEdit_path.text()
        __fileName = "Left-Lower-Primary.csv"

        if "recycleBin.json" in os.listdir(PATH_STORE_DATA_DIR):
            data = Store.read_json_for_left()
            listOfPrimaryLowerLeft = data[LOWERUSERPRIMARY]
            path = os.path.join(
                getPath + "/Backup/Lower/Lower-Left/Lower-Primary")

            if listOfPrimaryLowerLeft != []:
                for count in range(len(listOfPrimaryLowerLeft)):
                    if listOfPrimaryLowerLeft[count]["E-Mail"] == None:
                        __email = None
                    else:
                        __email = secure.decrypt(
                            listOfPrimaryLowerLeft[count]["E-Mail"][-2], listOfPrimaryLowerLeft[count]["E-Mail"][-1])

                    __name = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Name"][-2], listOfPrimaryLowerLeft[count]["Name"][-1])
                    __roll = listOfPrimaryLowerLeft[count]["Roll"]
                    __address = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Address"][-2], listOfPrimaryLowerLeft[count]["Address"][-1])
                    __level = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Level"][-2], listOfPrimaryLowerLeft[count]["Level"][-1])
                    __father_name = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Father-Name"][-2], listOfPrimaryLowerLeft[count]["Father-Name"][-1])
                    __mather_name = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Mather-Name"][-2], listOfPrimaryLowerLeft[count]["Mather-Name"][-1])
                    __parent_conta = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Contact-Number"][-2], listOfPrimaryLowerLeft[count]["Contact-Number"][-1])
                    __dob = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Date-of-Birth"][-2], listOfPrimaryLowerLeft[count]["Date-of-Birth"][-1])
                    __relig_num = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Registration-Number"][-2], listOfPrimaryLowerLeft[count]["Registration-Number"][-1])
                    __religion = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Religion"][-2], listOfPrimaryLowerLeft[count]["Religion"][-1])
                    __gender = secure.decrypt(
                        listOfPrimaryLowerLeft[count]["Gender"][-2], listOfPrimaryLowerLeft[count]["Gender"][-1])

                    if __fileName not in os.listdir(path):
                        with open(os.path.join(path + '/'+__fileName), 'w') as file:
                            writeCsv = csv.writer(file)
                            writeCsv.writerow(['Roll', 'Name', 'Address', 'E-Mail', 'Level', 'Father-Name', 'Mather-Name',
                                               'Contact-Number', 'Date-of-Birth', 'Registration-Number', 'Religion', 'Gender']
                                              )
                            writeCsv.writerow(
                                [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                    __parent_conta, __dob, __relig_num, __religion, __gender]
                            )
                    else:
                        with open(os.path.join(path+'/'+__fileName), 'a') as file:
                            writeCsv = csv.writer(file)
                            writeCsv.writerow(
                                [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                    __parent_conta, __dob, __relig_num, __religion, __gender]
                            )
        # Analtices For Backup Data
        path = os.path.join(path + '/')
        if __fileName in os.listdir(path):
            file_path = os.path.join(path + __fileName)
            dataFrame = pd.read_csv(file_path)
            dataFrame.drop_duplicates(inplace=True)
            dataFrame.to_csv(file_path, index=False)

    def backupLowerAdvancedLeftDataIntoCSV(self):
        getPath = self.ui.lineEdit_path.text()
        __fileName = "Left-Lower-Advanced.csv"
        path = os.path.join(
            getPath + "/Backup/Lower/Lower-Left/Lower-Advanced")

        if "recycleBin.json" in os.listdir(PATH_STORE_DATA_DIR):
            data = Store.read_json_for_left()
            listOfAdvancedLowerLeft = data[LOWERUSERADVANCED]
            for count in range(len(listOfAdvancedLowerLeft)):

                if listOfAdvancedLowerLeft[count]["E-Mail"] == None:
                    __email = None
                else:
                    __email = secure.decrypt(
                        listOfAdvancedLowerLeft[count]["E-Mail"][-2], listOfAdvancedLowerLeft[count]["E-Mail"][-1])

                __name = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Name"][-2], listOfAdvancedLowerLeft[count]["Name"][-1])
                __roll = listOfAdvancedLowerLeft[count]["Roll"]
                __address = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Address"][-2], listOfAdvancedLowerLeft[count]["Address"][-1])
                __level = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Level"][-2], listOfAdvancedLowerLeft[count]["Level"][-1])
                __father_name = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Father-Name"][-2], listOfAdvancedLowerLeft[count]["Father-Name"][-1])
                __mather_name = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Mather-Name"][-2], listOfAdvancedLowerLeft[count]["Mather-Name"][-1])
                __parent_conta = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Contact-Number"][-2], listOfAdvancedLowerLeft[count]["Contact-Number"][-1])
                __dob = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Date-of-Birth"][-2], listOfAdvancedLowerLeft[count]["Date-of-Birth"][-1])
                __relig_num = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Registration-Number"][-2], listOfAdvancedLowerLeft[count]["Registration-Number"][-1])
                __religion = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Religion"][-2], listOfAdvancedLowerLeft[count]["Religion"][-1])
                __gender = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Gender"][-2], listOfAdvancedLowerLeft[count]["Gender"][-1])
                __streem = secure.decrypt(
                    listOfAdvancedLowerLeft[count]["Stream"][-2], listOfAdvancedLowerLeft[count]["Stream"][-1])

                if __fileName not in os.listdir(path):
                    with open(os.path.join(path+'/'+__fileName), 'w') as file:
                        writeCsv = csv.writer(file)
                        writeCsv.writerow(['Roll', 'Name', 'Address', 'E-Mail', 'Level', 'Father-Name', 'Mather-Name',
                                           'Contact-Number', 'Date-of-Birth', 'Registration-Number', 'Religion', 'Gender', 'Stream']
                                          )
                        writeCsv.writerow(
                            [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                __parent_conta, __dob, __relig_num, __religion, __gender, __streem]
                        )
                else:
                    with open(os.path.join(path+'/'+__fileName), 'a') as file:
                        writeCsv = csv.writer(file)
                        writeCsv.writerow(
                            [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                __parent_conta, __dob, __relig_num, __religion, __gender, __streem]
                        )
        # Analtices For Backup Data
        path = os.path.join(path + '/')
        if __fileName in os.listdir(path):
            file_path = os.path.join(path + __fileName)
            dataFrame = pd.read_csv(file_path)
            dataFrame.drop_duplicates(inplace=True)
            dataFrame.to_csv(file_path, index=False)

    # Backup Inter data only
    def backupInterDataIntoCSV(self):

        getPath = self.ui.lineEdit_path.text()
        __fileName = "Inter.csv"
        data = Store.read_json()
        listOfInter = data[INTERUSER]

        path = os.path.join(getPath + "/Backup/Inter/Inter-Active")
        if 'data.json' in os.listdir(PATH_STORE_DATA_DIR):
            for index in range(len(listOfInter)):
                if listOfInter[index]['Subject'] != None:
                    __sub = secure.decrypt(
                        listOfInter[index]['Subject'][-2], listOfInter[index]['Subject'][-1])
                else:
                    __sub = None
                if listOfInter[index]['E-Mail'] != None:
                    __email = secure.decrypt(
                        listOfInter[index]['E-Mail'][-2], listOfInter[index]['E-Mail'][-1])
                else:
                    __email = None

                if listOfInter[index]['Level'] != None:
                    __level = secure.decrypt(
                        listOfInter[index]['Level'][-2], listOfInter[index]['Level'][-1])
                else:
                    __level = None

                __roll = listOfInter[index]["Roll"]
                __name = secure.decrypt(
                    listOfInter[index]['Name'][-2], listOfInter[index]['Name'][-1])
                __addr = secure.decrypt(
                    listOfInter[index]['Address'][-2], listOfInter[index]['Address'][-1])
                __gender = secure.decrypt(
                    listOfInter[index]['Gender'][-2], listOfInter[index]['Gender'][-1])
                __cont_num = secure.decrypt(
                    listOfInter[index]['Contact-Number'][-2], listOfInter[index]['Contact-Number'][-1])

                if __fileName not in os.listdir(path):
                    with open(os.path.join(path+'/'+__fileName), 'w') as file:
                        writeCsv = csv.writer(file)
                        writeCsv.writerow(
                            ['Roll', 'Name', 'Address', 'Subject', 'E-Mail',
                                'Contact-Number', 'Level', 'Gender']
                        )
                        writeCsv.writerow(
                            [__roll, __name, __addr, __sub, __email, __cont_num, __level, __gender])
                else:
                    with open(os.path.join(path+'/'+__fileName), 'a') as file:
                        writeCsv = csv.writer(file)
                        writeCsv.writerow(
                            [__roll, __name, __addr, __sub, __email,
                                __cont_num, __level, __gender]
                        )

        # Analtices For Backup Data
        path = os.path.join(path + '/')
        if __fileName in os.listdir(path):
            file_path = os.path.join(path + __fileName)
            dataFrame = pd.read_csv(file_path)
            dataFrame.drop_duplicates(inplace=True)
            dataFrame.to_csv(file_path, index=False)

    # Backup Lower data only

    def backupLowerOrdinaryDataIntoCSV(self):

        getPath = self.ui.lineEdit_path.text()
        __fileName = "Lower-Ordinary.csv"
        data = Store.read_json()

        levelList = [
            'Level - 06', 'Level - 07', 'Level - 08', 'Level - 09', 'Level - 10', 'Level - 11'
        ]

        if 'data.json' in os.listdir(PATH_STORE_DATA_DIR):
            listOfLower = data[LOWERUSERORDINARY]
            path = os.path.join(
                getPath + '/Backup/Lower/Lower-Active/Lower-Ordinary')
            for level in levelList:
                if listOfLower[level] != []:
                    for count in range(len(listOfLower[level])):
                        if listOfLower[level][count]["E-Mail"] != None:
                            __email = secure.decrypt(
                                listOfLower[level][count]["E-Mail"][-2], listOfLower[level][count]["E-Mail"][-1])
                        else:
                            __email = None

                        __roll = listOfLower[level][count]["Roll"]
                        __name = secure.decrypt(
                            listOfLower[level][count]["Name"][-2], listOfLower[level][count]["Name"][-1])
                        __address = secure.decrypt(
                            listOfLower[level][count]["Address"][-2], listOfLower[level][count]["Address"][-1])
                        __level = secure.decrypt(
                            listOfLower[level][count]["Level"][-2], listOfLower[level][count]["Level"][-1])
                        __father_name = secure.decrypt(
                            listOfLower[level][count]["Father-Name"][-2], listOfLower[level][count]["Father-Name"][-1])
                        __mather_name = secure.decrypt(
                            listOfLower[level][count]["Mather-Name"][-2], listOfLower[level][count]["Mather-Name"][-1])
                        __parent_conta = secure.decrypt(
                            listOfLower[level][count]["Contact-Number"][-2], listOfLower[level][count]["Contact-Number"][-1])
                        __dob = secure.decrypt(
                            listOfLower[level][count]["Date-of-Birth"][-2], listOfLower[level][count]["Date-of-Birth"][-1])
                        __relig_num = secure.decrypt(
                            listOfLower[level][count]["Registration-Number"][-2], listOfLower[level][count]["Registration-Number"][-1])
                        __religion = secure.decrypt(
                            listOfLower[level][count]["Religion"][-2], listOfLower[level][count]["Religion"][-1])
                        __gender = secure.decrypt(
                            listOfLower[level][count]["Gender"][-2], listOfLower[level][count]["Gender"][-1])

                        if __fileName not in os.listdir(path):
                            with open(os.path.join(path+'/'+level+'/'+__fileName), 'w') as file:
                                writeCsv = csv.writer(file)
                                writeCsv.writerow(['Roll', 'Name', 'Address', 'E-Mail', 'Level', 'Father-Name', 'Mather-Name',
                                                   'Contact-Number', 'Date-of-Birth', 'Registration-Number', 'Religion', 'Gender']
                                                  )
                                writeCsv.writerow(
                                    [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                     __parent_conta, __dob, __relig_num, __religion, __gender]
                                )
                        else:
                            with open(os.path.join(path+'/'+level+'/'+__fileName), 'a') as file:
                                writeCsv = csv.writer(file)
                                writeCsv.writerow(
                                    [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                     __parent_conta, __dob, __relig_num, __religion, __gender]
                                )
            # Analtices For Backup Data
            if __fileName in os.listdir(os.path.join(path + "/" + level + '/')):
                dataFrame = pd.read_csv(os.path.join(
                    path + "/" + level + '/') + __fileName)
                dataFrame.drop_duplicates(inplace=True)
                dataFrame.to_csv(os.path.join(
                    path + "/" + level + '/') + __fileName, index=False)

    # Backup Inter left data only
    def backupInterLeftDataIntoCSV(self):
        getPath = self.ui.lineEdit_path.text()
        __fileName = "Left-Inter.csv"
        data = Store.read_json_for_left()
        listOfInter = data[INTERUSER]
        path = os.path.join(getPath + '/Backup/Inter/Inter-Left')
        if 'recycleBin.json' in os.listdir(PATH_STORE_DATA_DIR):
            if listOfInter != []:
                for index in range(len(listOfInter)):
                    if listOfInter[index]["Subject"] != None:
                        __sub = secure.decrypt(
                            listOfInter[index]["Subject"][-2], listOfInter[index]["Subject"][-1])
                    else:
                        __sub = None
                    if listOfInter[index]["E-Mail"] != None:
                        __email = secure.decrypt(
                            listOfInter[index]["E-Mail"][-2], listOfInter[index]["E-Mail"][-1])
                    else:
                        __email = None
                    if listOfInter[index]["Level"] != None:
                        __level = secure.decrypt(
                            listOfInter[index]["Level"][-2], listOfInter[index]["Level"][-1])
                    else:
                        __level = None

                    __roll = listOfInter[index]["Roll"]
                    __name = secure.decrypt(
                        listOfInter[index]["Name"][-2], listOfInter[index]["Name"][-1])
                    __addr = secure.decrypt(
                        listOfInter[index]["Address"][-2], listOfInter[index]["Address"][-1])
                    __cont_num = secure.decrypt(
                        listOfInter[index]["Contact-Number"][-2], listOfInter[index]["Contact-Number"][-1])
                    __gender = secure.decrypt(
                        listOfInter[index]["Gender"][-2], listOfInter[index]["Gender"][-1])

                    if __fileName not in os.listdir(path):
                        with open(os.path.join(path+'/'+__fileName), 'w') as file:
                            writeCsv = csv.writer(file)
                            writeCsv.writerow(
                                ['Roll', 'Name', 'Address', 'Subject',
                                    'E-Mail', 'Contact-Number', 'Level', 'Gender']
                            )
                            writeCsv.writerow(
                                [__roll, __name, __addr, __sub, __email, __cont_num, __level, __gender])

                    else:
                        with open(os.path.join(path+'/'+__fileName), 'a') as file:
                            writeCsv = csv.writer(file)
                            writeCsv.writerow(
                                [__roll, __name, __addr, __sub, __email,
                                    __cont_num, __level, __gender]
                            )
        # Analtices For Backup Data
        path = os.path.join(path + '/')
        if __fileName in os.listdir(path):
            file_path = os.path.join(path + __fileName)
            dataFrame = pd.read_csv(file_path)
            dataFrame.drop_duplicates(inplace=True)
            dataFrame.to_csv(file_path, index=False)

    # Backup Lower Left data only
    def backupLowerOrdinaryLeftDataIntoCSV(self):
        getPath = self.ui.lineEdit_path.text()
        __fileName = "Left-Lower-Ordinary.csv"
        data = Store.read_json_for_left()
        listOfLower = data[LOWERUSERORDINARY]

        path = os.path.join(
            getPath + '/Backup/Lower/Lower-Left/Lower-Ordinary')
        if 'recycleBin.json' in os.listdir(PATH_STORE_DATA_DIR):
            if listOfLower != []:
                for index in range(len(listOfLower)):

                    if listOfLower[index]["E-Mail"] != None:
                        __email = secure.decrypt(
                            listOfLower[index]["E-Mail"][-2], listOfLower[index]["E-Mail"][-1])
                    else:
                        __email = None

                    __roll = listOfLower[index]["Roll"]
                    __name = secure.decrypt(
                        listOfLower[index]["Name"][-2], listOfLower[index]["Name"][-1])
                    __address = secure.decrypt(
                        listOfLower[index]["Address"][-2], listOfLower[index]["Address"][-1])
                    __level = secure.decrypt(
                        listOfLower[index]["Level"][-2], listOfLower[index]["Level"][-1])
                    __father_name = secure.decrypt(
                        listOfLower[index]["Father-Name"][-2], listOfLower[index]["Father-Name"][-1])
                    __mather_name = secure.decrypt(
                        listOfLower[index]["Mather-Name"][-2], listOfLower[index]["Mather-Name"][-1])
                    __parent_conta = secure.decrypt(
                        listOfLower[index]["Contact-Number"][-2], listOfLower[index]["Contact-Number"][-1])
                    __dob = secure.decrypt(
                        listOfLower[index]["Date-of-Birth"][-2], listOfLower[index]["Date-of-Birth"][-1])
                    __relig_num = secure.decrypt(
                        listOfLower[index]["Registration-Number"][-2], listOfLower[index]["Registration-Number"][-1])
                    __religion = secure.decrypt(
                        listOfLower[index]["Religion"][-2], listOfLower[index]["Religion"][-1])
                    __gender = secure.decrypt(
                        listOfLower[index]["Gender"][-2], listOfLower[index]["Gender"][-1])

                    if __fileName not in os.listdir(path):
                        with open(os.path.join(path+'/'+__fileName), 'w') as file:
                            writeCsv = csv.writer(file)
                            writeCsv.writerow(
                                ['Roll', 'Name', 'Address', 'E-Mail', 'Level', 'Father-Name', 'Mather-Name',
                                 'Parent-Contact', 'Date-of-Birth', 'Registration-Number', 'Religion', 'Gender']
                            )
                            writeCsv.writerow(
                                [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                 __parent_conta, __dob, __relig_num, __religion, __gender]
                            )

                    else:
                        with open(os.path.join(path+'/'+__fileName), 'a') as file:
                            writeCsv = csv.writer(file)
                            writeCsv.writerow(
                                [__roll, __name, __address, __email, __level, __father_name, __mather_name,
                                 __parent_conta, __dob, __relig_num,  __religion, __gender]
                            )
        # Analtices For Backup Data
        path = os.path.join(path + '/')
        if __fileName in os.listdir(path):
            file_path = os.path.join(path + __fileName)
            dataFrame = pd.read_csv(file_path)
            dataFrame.drop_duplicates(inplace=True)
            dataFrame.to_csv(file_path, index=False)

#############################################################################
# MAIN WINDOW


class MainWindow(QMainWindow):

    hidden_count = False

    # Find Access Frame
    active_frame_inter = 0
    active_frame_lower = 0
    left_frame_inter = 0
    left_frame_lower = 0

    # Serach Frame
    actionsOfFrame = False

    # Search Resalt Frame var and btns var
    vars_names = {}

    counter_inter = 0
    counter_lower = 0
    counter_inter_l = 0
    counter_lower_l = 0

    btn_click_event = False

    barChart_active_inter = False
    barChart_active_lower = False
    barChart_active_lower_ad = False
    barChart_active_lower_pr = False
    barChart_active_lower_ad_12 = False
    barChart_active_lower_ad_13 = False

    interUserCount = 0

    gender = "none"

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(u"Findup")
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        # Set Window Icon
        icon = QIcon()
        icon.addFile(u"./packges/app/items/img/findupnew_window.png")
        self.setWindowIcon(icon)

        self.ui.label_icon_inter.setText(
            u"<html><head/><body><p align=\"center\"><img src=\"./packges/app/items/img/user100.png\"/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ADD TEACHERS</span></p></body></html>"
        )
        self.ui.label_icon_lower.setText(
            u"<html><head/><body><p align=\"center\"><img src=\"./packges/app/items/img/user100.png\"/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ADD STUDENTS</span></p></body></html>"
        )
        self.ui.label_dateofbirth_info.setText(
            u"<p>&nbsp;<img src=\"./packges/app/items/icons/16x16/cil-calendar-check.png\">&nbsp; &nbsp;<b>Date Of Birth</b></p>"
        )
        self.ui.label.setText(
            "<html><head/><body><p align=\"center\"><img src=\"./packges/app/items/img/user100.png\"/></p><p align=\"center\"><span style=\" font-weight:600;\">Edit Profile</span></p></body></html>")

        self.ui.label_icon_.setText(
            u"<html><head/><body><p align=\"center\"><img src=\"./packges/app/items/img/user100.png\"/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ADD STUDENTS</span></p></body></html>"
        )

        self.ui.label_inforem_date_of_birth_ad.setText(
            u"<p>&nbsp;<img src=\"./packges/app/items/icons/16x16/cil-calendar-check.png\">&nbsp; &nbsp;<b>Date Of Birth</b></p>"
        )
        self.ui.label_icon_primary.setText(
            u"<html><head/><body><p align=\"center\"><img src=\"./packges/app/items/img/user100.png\"/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ADD STUDENTS</span></p></body></html>"
        )
        self.ui.label_inforem_date_of_birth_ad_2.setText(
            u"<p>&nbsp;<img src=\"./packges/app/items/icons/16x16/cil-calendar-check.png\">&nbsp; &nbsp;<b>Date Of Birth</b></p>"
        )

        # Font For Info Label
        self.font_info = QFont()
        self.font_info.setBold(True)
        self.font_info.setPointSize(10)
        self.font_info.setFamily("monospace, sans-serif")

        # Setting Add Icons
        # Username Icon Hidden Button
        icon_hidden = QIcon()
        icon_hidden.addFile(
            "./packges/app/items/icons/main-icons/chevron-up.svg")
        self.ui.btn_hidden_username_bar.setIcon(icon_hidden)

        # Email Icon Hidden Button
        self.ui.btn_hidden_email_bar.setIcon(icon_hidden)

        # Contact Number Icon Hidden Button
        self.ui.btn_hidden_contact_number_bar.setIcon(icon_hidden)

        # Password Icon Hidden Button
        self.ui.btn_hidden_passowd_changer_bar.setIcon(icon_hidden)

        # More Options Icon Hidden button
        self.ui.btn_hidden_options.setIcon(icon_hidden)

        # Adout
        self.ui.btn_hidden_adout.setIcon(icon_hidden)

        # Setting Bar Animation
        normal_path = "./packges/app/items/icons/main-icons/chevron-up.svg"
        active_path = "./packges/app/items/icons/main-icons/chevron-down.svg"

        self.ui.btn_hidden_username_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar(self,  self.ui.frame_user_name_changer.height(
        ), self.ui.frame_user_name_changer, self.ui.frame_name_changer_content_page, True, self.ui.btn_hidden_username_bar, normal_path, active_path))
        self.ui.btn_hidden_email_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar(self,  self.ui.frame_email_changer.height(
        ), self.ui.frame_email_changer, self.ui.frame_email_changer_content_bar, True, self.ui.btn_hidden_email_bar, normal_path, active_path))
        self.ui.btn_hidden_contact_number_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar(self,  self.ui.frame_contect_number_changer.height(
        ), self.ui.frame_contect_number_changer, self.ui.frame_contect_number_changer_content_bar, True, self.ui.btn_hidden_contact_number_bar, normal_path, active_path))
        self.ui.btn_hidden_passowd_changer_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar(self,  self.ui.frame_password_changer.height(
        ), self.ui.frame_password_changer, self.ui.frame_password_changer_content_bar, True, self.ui.btn_hidden_passowd_changer_bar, normal_path, active_path))
        self.ui.btn_hidden_options.clicked.connect(lambda: UIFunctions.settingHiddenBar_two(self,  self.ui.frame_more_options.height(
        ), self.ui.frame_more_options, self.ui.frame_more_options_contect_bar, True, self.ui.btn_hidden_options, normal_path, active_path))
        self.ui.btn_hidden_adout.clicked.connect(lambda: UIFunctions.settingHiddenBar_two(self, self.ui.frame_adout.height(
        ), self.ui.frame_adout, self.ui.frame_content_adout, True, self.ui.btn_hidden_adout, normal_path, active_path))

        # Toggle Burguer Menu
        self.ui.btn_Toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 200, True))

        self.ui.btn_superuser.clicked.connect(
            lambda: UIFunctions.userSideBar_toggle(self, 300, True))
        self.ui.btn_go_home_ad.clicked.connect(lambda: UIFunctions.home(self))

        UIFunctions.current_page(self)

        self.ui.btn_page_home.clicked.connect(lambda: UIFunctions.home(self))
        self.ui.btn_page_left.clicked.connect(lambda: UIFunctions.left(self))
        self.ui.btn_page_search.clicked.connect(
            lambda: UIFunctions.search(self))
        self.ui.btn_setting.clicked.connect(lambda: UIFunctions.setting(self))
        self.ui.btn_page_analytics.clicked.connect(
            lambda: UIFunctions.analytics(self))
        self.ui.btn_go_home.clicked.connect(lambda: UIFunctions.home(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home(self))

        # Super User Btn
        self.ui.btn_edit_setting.clicked.connect(
            lambda: UIFunctions.setting(self))

        # inter btn
        self.ui.btn_inter.clicked.connect(lambda: self.callInterWindow())
        # lower btn
        self.ui.btn_lower.clicked.connect(lambda: self.callLowerWindow())
        # Backup btn
        self.ui.btn_backup.clicked.connect(lambda: self.callBackupWindow())

        # Connect into btn_ordinary
        self.ui.btn_ordinary.clicked.connect(
            lambda: self.call_input_menu(self.ui.page_add_lower))

        # Connect into btn_advanced
        self.ui.btn_advanced.clicked.connect(
            lambda: self.call_input_menu(self.ui.page_add_advan))

        # Connect into btn_primary
        self.ui.btn_primary.clicked.connect(
            lambda: self.call_input_menu(self.ui.page))

        # read json data
        data = Store.read_super_user()

        # Set current User Name
        __name, __nameKey = data[SUPERUSER][-1]['Name'][-2], data[SUPERUSER][-1]['Name'][-1]
        __name = secure.decrypt(__name, __nameKey)
        self.ui.label_show_current_username.setText(f"""
			<p><spen style=\" font-size:12pt; font-weight:600;\">Current Name: <b>{__name}</b></spen></p>
		""")
        # Set current E-Mail
        __email, __emailKey = data[SUPERUSER][-1]['E-Mail'][-2], data[SUPERUSER][-1]['E-Mail'][-1]
        __email = secure.decrypt(__email, __emailKey)
        self.ui.label_current_email.setText(f"""
			<p><spen style=\" font-size:12pt; font-weight:600;\">Current E-Mail: <b>{__email}</b></spen></p>
		""")
        # Set current Contact Number
        __Contact_Number, __Contact_NumberKey = data[
            SUPERUSER][-1]['Contact-Number'][-2], data[SUPERUSER][-1]['Contact-Number'][-1]
        __Contact_Number = secure.decrypt(
            __Contact_Number, __Contact_NumberKey)
        self.ui.label_show_current_contact_number.setText(f"""
			<p><spen style=\" font-size:12pt; font-weight:600;\">Current Contact Number: <b>{__Contact_Number}</b></spen></p>
		""")

        # Set Acitve status Inter
        self.connect_inter()
        self.connect_inter_left()

        # Set Acitve Status Lower odrinary
        self.connect_lower_odrinary()
        self.connect_lower_odrinary_left()

        # set Active Status Lower Primary
        self.connect_lower_primary()
        self.connect_lower_primary_Left()

        # set Active Status Lower Advanced
        self.connect_lower_advanced()
        self.connect_lower_advanced_left()

        font_for = QFont()
        font_for.setFamily("Segoe UI")
        font_for.setPointSize(10)

        # Call the more options
        # Action
        self.ui.btn_reset.clicked.connect(lambda: self.reset())
        self.ui.btn_logout.clicked.connect(lambda: self.logout())
        self.ui.btn_reload.clicked.connect(lambda: self.reload())

        # Side Bar Super User
        self.ui.label_infor_super.setFont(font_for)
        self.ui.label_infor_super.setText(f"""
            <html>
                <head/>
                <body>
                    <p align=\"center\"> About <p>
                    <p>
                        <span>
                            &nbsp;User Name:<br>
                            &nbsp;&nbsp;&nbsp;{__name.title()}
                        </span><br/><br/>
                        <span>
                            &nbsp;Email:<br>
                            &nbsp;&nbsp;&nbsp;{__email}
                        </span><br/><br/>
                        <span>
                            &nbsp;Number:<br>
                            &nbsp;&nbsp;&nbsp;{__Contact_Number}
                        </span><br/><br/>
                    </p>
                </body>
            </html>
        """)
        self.ui.label_super_icon.setText(f"""
            <html>
                <head/>
                <body>
                    <p align=\"center\"><img src=\"./packges/app/items/img/user100.png\"/></p>
                    <p align=\"center\" font>{__name.title()}</p>
                </body>
            </html>
        """)

        # Verify password for Change Name
        self.ui.btn_save_username.clicked.connect(lambda: self.access_name())

        # Verify password for Change E - Mail
        self.ui.btn_save_change_email.clicked.connect(
            lambda: self.access_email())

        # Verify Password for Change Contact Number
        self.ui.btn_save_contact_number.clicked.connect(
            lambda: self.access_contactNumber())

        # Verify Password for change Password
        self.ui.btn_save_password.clicked.connect(
            lambda: self.access_password())

        # Get Delete btns
        self.ui.btn_delete_inter_1.clicked.connect(
            lambda: self.deleteInterForActive())
        self.ui.btn_delete_lower_1.clicked.connect(
            lambda: self.deleteLowerOdrnaryForActive())
        self.ui.btn_delete_lower_pri.clicked.connect(
            lambda: self.deleteLowerPrimaryForActive()
        )
        self.ui.btn_delete_lower_advan.clicked.connect(
            lambda: self.deleteLowerAdvancedForActive()
        )

        # Get Delete btns for left
        self.ui.btn_delete_inter_left_1.clicked.connect(
            lambda: self.deleteInterForLeft())
        self.ui.btn_delete_lower_left_1.clicked.connect(
            lambda: self.deleteLowerOdrinaryForLeft())
        self.ui.btn_delete_lower_left_pri.clicked.connect(
            lambda: self.deleteLowerPrimaryForLeft()
        )
        self.ui.btn_delete_lower_left_advan.clicked.connect(
            lambda: self.deleteLowerAdvancedForLeft()
        )

        # Set Icons
        setIcon_line(self.ui.lineEdit_username_change_input,
                     u"./packges/app/items/icons/main-icons/user.svg")
        setIcon_line(self.ui.lineEdit_change_email_input,
                     u"./packges/app/items/icons/16x16/cil-at.png")
        setIcon_line(self.ui.lineEdit_contact_number_input,
                     u"./packges/app/items/icons/main-icons/phone.svg")
        setIcon_line(self.ui.lineEdit_passord_input,
                     u"./packges/app/items/icons/main-icons/lock.svg")
        setIcon_line(self.ui.lineEdit_repassword_input,
                     u"./packges/app/items/icons/main-icons/lock.svg")
        setIcon_line(self.ui.lineEdit_nameSearch,
                     u"./packges/app/items/icons/main-icons/search.svg")
        setIcon_line(self.ui.lineEdit_rollSearch,
                     u"./packges/app/items/icons/main-icons/search.svg")

        # Search Name And Search Roll
        self.ui.btn_nameSearch.clicked.connect(
            lambda: self.connectIntoNameSearch())
        self.ui.btn_rollSearch.clicked.connect(
            lambda: self.connectIntoRollSearch())

        # Set Copy Event For Active
        self.ui.label_info_lower_1.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_info_lower_1.installEventFilter(self)
        self.ui.label_info_lower_1.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.label_info_lower_1.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui.label_info_Inter_1.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_info_Inter_1.installEventFilter(self)
        self.ui.label_info_Inter_1.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.label_info_Inter_1.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        # Set Copy Event For Left
        self.ui.info_inter_left_1.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.info_inter_left_1.installEventFilter(self)
        self.ui.info_inter_left_1.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.info_inter_left_1.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui.info_lower_1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.ui.info_lower_1.installEventFilter(self)
        self.ui.info_lower_1.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.info_lower_1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.ui.info_lower_left_pri.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.info_lower_left_pri.installEventFilter(self)
        self.ui.info_lower_left_pri.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.info_lower_left_pri.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui.label_info_lower_pri.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_info_lower_pri.installEventFilter(self)
        self.ui.label_info_lower_pri.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.label_info_lower_pri.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui.label_info_lower_advan.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_info_lower_advan.installEventFilter(self)
        self.ui.label_info_lower_advan.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.label_info_lower_advan.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui.info_lower_left_advan.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.info_lower_left_advan.installEventFilter(self)
        self.ui.info_lower_left_advan.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.info_lower_left_advan.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        # FOR ADD INTER PAGE
        self.ui.label_show_roll_number.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_show_roll_number.installEventFilter(self)
        self.ui.label_show_roll_number.setCursor(QCursor(Qt.IBeamCursor))

        # FOR ADD LOWER PAGE
        self.ui.label_show_roll_number_lower.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_show_roll_number_lower.installEventFilter(self)
        self.ui.label_show_roll_number_lower.setCursor(QCursor(Qt.IBeamCursor))

        self.ui.label_show_roll_primary.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_show_roll_primary.installEventFilter(self)
        self.ui.label_show_roll_primary.setCursor(QCursor(Qt.IBeamCursor))

        self.ui.label_show_roll_ad.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_show_roll_ad.installEventFilter(self)
        self.ui.label_show_roll_ad.setCursor(QCursor(Qt.IBeamCursor))

        # ANALYTICS FOR LOWER AND INTER
        self.data_frame()

        # ADD INTER USER PAGE ICONS
        setIcon_line(self.ui.lineEdit_name,
                     u"./packges/app/items/icons/16x16/cil-user.png")
        setIcon_line(self.ui.lineEdit_address,
                     u"./packges/app/items/icons/16x16/cil-location-pin.png")
        setIcon_line(self.ui.lineEdit_subject,
                     u"./packges/app/items/icons/16x16/cil-lightbulb.png")
        setIcon_line(self.ui.lineEdit_email,
                     u"./packges/app/items/icons/16x16/cil-at.png")
        setIcon_line(self.ui.lineEdit_contect,
                     u"./packges/app/items/icons/16x16/phone-39-16.png")
        setIcon_line(self.ui.lineEdit_level,
                     u"./packges/app/items/icons/16x16/cil-level-up.png")

        # ADD LOWER USER PAGE ICONS
        setIcon_line(self.ui.lineEdit_name_lower,
                     u"./packges/app/items/icons/16x16/cil-user.png")
        setIcon_line(self.ui.lineEdit_address_lower,
                     u"./packges/app/items/icons/16x16/cil-location-pin.png")
        setIcon_line(self.ui.lineEdit_father,
                     u"./packges/app/items/icons/16x16/cil-people.png")
        setIcon_line(self.ui.lineEdit_mather,
                     u"./packges/app/items/icons/16x16/cil-people.png")
        setIcon_line(self.ui.lineEdit_contect_lower,
                     u"./packges/app/items/icons/16x16/phone-39-16.png")
        setIcon_line(self.ui.lineEdit_ragis_number,
                     u"./packges/app/items/icons/16x16/cil-dialpad.png")
        setIcon_line(self.ui.lineEdit_email_lower,
                     u"./packges/app/items/icons/16x16/cil-at.png")
        setIcon_line(self.ui.lineEdit_religion,
                     u"./packges/app/items/icons/16x16/cil-input.png")

        # ADD LOWER USER PAGE ICONS FOR ADVANS
        setIcon_line(self.ui.lineEdit_name_ad,
                     u"./packges/app/items/icons/16x16/cil-user.png")
        setIcon_line(self.ui.lineEdit_address_ad,
                     u"./packges/app/items/icons/16x16/cil-location-pin.png")
        setIcon_line(self.ui.lineEdit_father_ad,
                     u"./packges/app/items/icons/16x16/cil-people.png")
        setIcon_line(self.ui.lineEdit_mather_ad,
                     u"./packges/app/items/icons/16x16/cil-people.png")
        setIcon_line(self.ui.lineEdit_contect_ad,
                     u"./packges/app/items/icons/16x16/phone-39-16.png")
        setIcon_line(self.ui.lineEdit_registration_ad,
                     u"./packges/app/items/icons/16x16/cil-dialpad.png")
        setIcon_line(self.ui.lineEdit_email_ad,
                     u"./packges/app/items/icons/16x16/cil-at.png")
        setIcon_line(self.ui.lineEdit_religion_ad,
                     u"./packges/app/items/icons/16x16/cil-input.png")

        # ADD LOWER USER PAGE ICONS FOR PRIMARY
        setIcon_line(self.ui.lineEdit_name_primary,
                     u"./packges/app/items/icons/16x16/cil-user.png")
        setIcon_line(self.ui.lineEdit_address_primary,
                     u"./packges/app/items/icons/16x16/cil-location-pin.png")
        setIcon_line(self.ui.lineEdit_father_primary,
                     u"./packges/app/items/icons/16x16/cil-people.png")
        setIcon_line(self.ui.lineEdit_mather_primary,
                     u"./packges/app/items/icons/16x16/cil-people.png")
        setIcon_line(self.ui.lineEdit_contect_primary,
                     u"./packges/app/items/icons/16x16/phone-39-16.png")
        setIcon_line(self.ui.lineEdit_registration_primary,
                     u"./packges/app/items/icons/16x16/cil-dialpad.png")
        setIcon_line(self.ui.lineEdit_email_primary,
                     u"./packges/app/items/icons/16x16/cil-at.png")
        setIcon_line(self.ui.lineEdit_religion_primary,
                     u"./packges/app/items/icons/16x16/cil-input.png")

        self.ui.comboBox_stream.setStyleSheet("QComboBox{\n"
                                              "    background-color: #1D222E;\n"
                                              "    border-radius: 10px;\n"
                                              "    border: 2px solid  #1D222E;\n"
                                              "    padding: 5px;\n"
                                              "    padding-left: 10px;\n"
                                              "    color: white;\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox:hover{\n"
                                              "    border: 2px solid rgb(49, 50, 63);\n"
                                              "}\n"
                                              "\n"
                                              "QComboBox::drop-down {\n"
                                              "    subcontrol-origin: padding;\n"
                                              "    subcontrol-position: top right;\n"
                                              "    width: 25px;\n"
                                              "    border-left-width: 3px;\n"
                                              "    border-left-color: rgba(39, 44, 54, 150);\n"
                                              "    border-left-style: solid;\n"
                                              "    border-top-right-radius: 3px;\n"
                                              "    border-bottom-right-radius: 3px;\n"
                                              "    background-image: url(./packges/app/items/icons/16x16/cil-arrow-bottom.png);\n"
                                              "    background-position: center;\n"
                                              "    background-repeat: no-reperat;\n"
                                              "}\n"
                                              "QComboBox QAbstractItemView {\n"
                                              "    color: rgb(85, 170, 255);\n"
                                              "    background-color: #1D222E;\n"
                                              "    padding: 10px;\n"
                                              "    selection-background-color: rgb(39, 44, 54);\n"
                                              "}")

        self.ui.dateEdit_date_of_birth_ad.setStyleSheet("QDateEdit{\n"
                                                        "     color:white;\n"
                                                        "     background-color: #1D222E;\n"
                                                        "    padding-left: 10px;\n"
                                                        "    border: none;\n"
                                                        "    border-radius: 10px;\n"
                                                        "}\n"
                                                        "QDateEdit::down-button{\n"
                                                        "       image: url(packges/app/items/icons/main-icons/chevron-down.svg);\n"
                                                        "       margin-right: 6px;\n"
                                                        "}\n"
                                                        " QDateEdit::up-button{\n"
                                                        "        image: url(packges/app/items/icons/main-icons/chevron-up.svg);\n"
                                                        "        margin-right: 6px;\n"
                                                        "}\n"
                                                        "QDateEdit::up-button:pressed{background-color: rgb(26, 114, 255);\n"
                                                        "        border-radius: 5px;}\n"
                                                        "QDateEdit::down-button:pressed{background-color: rgb(26, 114, 255);\n"
                                                        "        border-radius: 5px;}")

        self.ui.dateEdit_data_of_birth.setStyleSheet(u"QDateEdit{\n"
                                                     "color:white;\n"
                                                     "background-color: #1D222E;\n"
                                                     "padding-left: 10px;\n"
                                                     "border: none;\n"
                                                     "border-radius: 10px;\n"
                                                     "}\n"
                                                     "QDateEdit::down-button{\n"
                                                     "image: url(packges/app/items/icons/main-icons/chevron-down.svg);\n"
                                                     "margin-right: 6px;\n"
                                                     "}\n"
                                                     "QDateEdit::up-button{\n"
                                                     "image: url(packges/app/items/icons/main-icons/chevron-up.svg);\n"
                                                     "margin-right: 6px;\n"
                                                     "}\n"
                                                     "QDateEdit::up-button:pressed{background-color: rgb(26, 114, 255);\n"
                                                     "border-radius: 5px;}\n"
                                                     "QDateEdit::down-button:pressed{background-color: rgb(26, 114, 255);\n"
                                                     "border-radius: 5px;}")

        # SET ADD INTER GENDER AND LOWER
        self.ui.radioButton_female.clicked.connect(lambda: self.female_set())
        self.ui.radioButton_male.clicked.connect(lambda: self.male_set())
        self.ui.radioButton_other.clicked.connect(lambda: self.other_set())

        self.ui.radioButton_female_ad.clicked.connect(
            lambda: self.female_set())
        self.ui.radioButton_male_ad.clicked.connect(lambda: self.male_set())
        self.ui.radioButton_other_ad.clicked.connect(lambda: self.other_set())

        self.ui.radioButton_female_primary.clicked.connect(
            lambda: self.female_set())
        self.ui.radioButton_male_primary.clicked.connect(
            lambda: self.male_set())
        self.ui.radioButton_other_primary.clicked.connect(
            lambda: self.other_set())

        self.ui.radioButton_male_lower.clicked.connect(lambda: self.male_set())
        self.ui.radioButton_female_lower.clicked.connect(
            lambda: self.female_set())
        self.ui.radioButton_other_lower.clicked.connect(
            lambda: self.other_set())

        # STORE BUTTON FOR INTER
        self.ui.btn_addInter.clicked.connect(
            lambda: self.store_interData_thread())

        # STORE BUTTON FOR LOWER
        self.ui.btn_addlower.clicked.connect(lambda: self.search_thread())
        self.ui.btn_addLower_adv.clicked.connect(lambda: self.storeThread())
        self.ui.btn_addLower_primary.clicked.connect(
            lambda: self.storeThread_primary())

        # SET ICON FOR BTNS
        icon9 = QIcon()
        icon9.addFile(u"./packges/app/items/icons/main-icons/icon_arrow_left.svg",
                      QSize(), QIcon.Normal, QIcon.Off)

        icon8 = QIcon()
        icon8.addFile(u"./packges/app/items/icons/main-icons/user-plus.svg",
                      QSize(), QIcon.Normal, QIcon.Off)

        icon_arrow = QIcon()
        icon_arrow.addFile(
            "./packges/app/items/icons/main-icons/icon_arrow_left.svg")

        icon1 = QIcon()
        icon1.addFile(u"./packges/app/items/icons/main-icons/user-plus.svg",
                      QSize(), QIcon.Normal, QIcon.Off)

        icon_sup = QIcon()
        icon_sup.addFile(u"./packges/app/items/icons/main-icons/user.svg")

        icon4 = QIcon()
        icon4.addFile(u"./packges/app/items/icons/main-icons/search.svg",
                      QSize(), QIcon.Normal, QIcon.Off)

        icon6 = QIcon()
        icon6.addFile(u"./packges/app/items/icons/main-icons/user-x.svg",
                      QSize(), QIcon.Normal, QIcon.Off)

        self.ui.btn_delete_inter_1.setIcon(icon6)
        self.ui.btn_delete_lower_1.setIcon(icon6)
        self.ui.btn_delete_inter_left_1.setIcon(icon6)
        self.ui.btn_delete_lower_left_1.setIcon(icon6)

        self.ui.btn_addLower_primary.setIcon(icon1)
        self.ui.btn_go_home_primary.setIcon(icon_arrow)

        self.ui.btn_superuser.setIcon(icon_sup)

        self.ui.btn_inter.setIcon(icon1)
        self.ui.btn_lower.setIcon(icon1)

        self.ui.btn_edit_setting.setIcon(icon_arrow)

        self.ui.btn_go_home_ad.setIcon(icon9)
        self.ui.btn_go_home.setIcon(icon9)

        self.ui.btn_addInter.setIcon(icon8)
        self.ui.btn_addLower_adv.setIcon(icon8)

        self.ui.btn_addlower.setIcon(icon8)
        self.ui.btn_go_home_lower.setIcon(icon9)

        self.ui.btn_nameSearch.setIcon(icon4)
        self.ui.btn_rollSearch.setIcon(icon4)

        icon5 = QIcon()
        icon5.addFile(u"packges/app/items/icons/main-icons/settings.svg",
                      QSize(), QIcon.Normal, QIcon.Off)

        self.ui.btn_Toggle.setStyleSheet(u"QPushButton {\n"
                                         " background-image: url(./packges/app/items/icons/main-icons/menu.svg);\n"
                                         " background-position: left center;\n"
                                         " background-repeat: no-repeat;\n"
                                         " border: none;\n"
                                         " border-left: 22px solid rgb(20, 20, 20);\n"
                                         " border-right: 5px solid rgb(20, 20, 20);\n"
                                         " background-color: rgb(20, 20, 20);\n"
                                         " text-align: left;\n"
                                         " padding-left: 45px;\n"
                                         " color: #fff;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         " background-color: rgb(85, 170, 255);\n"
                                         " border-left: 22px solid rgb(85, 170, 255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         " background-color: rgb(90, 175, 255);\n"
                                         " border-left: 22px solid rgb(90, 175, 255);\n"
                                         "}")

        self.ui.btn_page_left.setStyleSheet(u"QPushButton {    \n"
                                            "  background-image: url(./packges/app/items/icons/main-icons/trash-2.svg);\n"
                                            "  background-position: left center;\n"
                                            "    background-repeat: no-repeat;\n"
                                            "  border: none;\n"
                                            "  border-left: 22px solid rgb(20, 20, 20);\n"
                                            "  border-right: 5px solid rgb(20, 20, 20);\n"
                                            "  background-color: rgb(20, 20, 20);\n"
                                            "  text-align: left;\n"
                                            "  padding-left: 45px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "  background-color: rgb(85, 170, 255);\n"
                                            "  border-left: 22px solid rgb(85, 170, 255);\n"
                                            "}\n"
                                            "QPushButton:pressed { \n"
                                            "  background-color: rgb(90, 175, 255);\n"
                                            "  border-left: 22px solid rgb(90, 175, 255);\n"
                                            "}")
        self.ui.btn_page_search.setStyleSheet(u"QPushButton {  \n"
                                              "    background-image: url(./packges/app/items/icons/main-icons/search.svg);\n"
                                              "    background-position: left center;\n"
                                              "    background-repeat: no-repeat;\n"
                                              "    border: none;\n"
                                              "    border-left: 22px solid rgb(20, 20, 20);\n"
                                              "    border-right: 5px solid rgb(20, 20, 20);\n"
                                              "    background-color: rgb(20, 20, 20);\n"
                                              "    text-align: left;\n"
                                              "    padding-left: 45px;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(85, 170, 255);\n"
                                              "    border-left: 22px solid rgb(85, 170, 255);\n"
                                              "}\n"
                                              "QPushButton:pressed {   \n"
                                              "    background-color: rgb(90, 175, 255);\n"
                                              "    border-left: 22px solid rgb(90, 175, 255);\n"
                                              "}")
        self.ui.btn_page_analytics.setStyleSheet(u"QPushButton {   \n"
                                                 " background-image: url(./packges/app/items/icons/24x24/bar-chart.png);\n"
                                                 " background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 " border: none;\n"
                                                 " border-left: 22px solid rgb(20, 20, 20);\n"
                                                 " border-right: 5px solid rgb(20, 20, 20);\n"
                                                 " background-color: rgb(20, 20, 20);\n"
                                                 " text-align: left;\n"
                                                 " padding-left: 45px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 " background-color: rgb(85, 170, 255);\n"
                                                 " border-left: 22px solid rgb(85, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {    \n"
                                                 " background-color: rgb(90, 175, 255);\n"
                                                 " border-left: 22px solid rgb(90, 175, 255);\n"
                                                 "}")
        self.ui.btn_setting.setStyleSheet(u"QPushButton {  \n"
                                          "    background-image: url(./packges/app/items/icons/main-icons/settings.svg);\n"
                                          "    background-position: left center;\n"
                                          "    background-repeat: no-repeat;\n"
                                          "    border: none;\n"
                                          "    border-left: 22px solid rgb(20, 20, 20);\n"
                                          "    border-right: 5px solid rgb(20, 20, 20);\n"
                                          "    background-color: rgb(20, 20, 20);\n"
                                          "    text-align: left;\n"
                                          "    padding-left: 45px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(85, 170, 255);\n"
                                          "    border-left: 22px solid rgb(85, 170, 255);\n"
                                          "}\n"
                                          "QPushButton:pressed {   \n"
                                          "    background-color: rgb(90, 175, 255);\n"
                                          "    border-left: 22px solid rgb(90, 175, 255);\n"
                                          "}")
        self.ui.label_logo_adout.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><img src=\"packges\\app\\items\\img\\findupnew.png\"/>TextLabel</p></body></html>"))

        # Show ==> Main Window
        self.show()

    # Call add User Menu
    def call_input_menu(self, obj):
        self.ui.stackedWidget.setCurrentWidget(obj)

    # Active Status For Delete
    def deleteInterForActive(self):
        data = Store.read_json()
        ldata = Store.read_json_for_left()

        if data[INTERUSER] != [] and RANDOM_INTER != []:
            ldata[INTERUSER].append(data[INTERUSER][RANDOM_INTER[-1]])
            del data[INTERUSER][RANDOM_INTER[-1]]
            t = Thread(target=Store.write_json_for_left, args=[ldata])
            t.start()
            t.join()
            t1 = Thread(target=Store.write_json, args=[data])
            t1.start()
            t1.join()
            self.connect_inter()
            self.connect_inter_left()
            self.data_frame()

    def deleteLowerOdrnaryForActive(self):
        data = Store.read_json()
        ldata = Store.read_json_for_left()

        if RANDOM_LOWER_ODRINAEY != []:
            ldata[LOWERUSERORDINARY].append(
                data[LOWERUSERORDINARY][RANDOM_LOWER_ODRINAEY[-1][0]][RANDOM_LOWER_ODRINAEY[-1][-1]])
            del data[LOWERUSERORDINARY][RANDOM_LOWER_ODRINAEY[-1]
                                        [0]][RANDOM_LOWER_ODRINAEY[-1][-1]]
            t = Thread(target=Store.write_json_for_left, args=[ldata])
            t.start()
            t.join()
            t1 = Thread(target=Store.write_json, args=[data])
            t1.start()
            t1.join()
            self.connect_lower_odrinary()
            self.connect_lower_odrinary_left()
            self.data_frame()

    def deleteLowerPrimaryForActive(self):
        data = Store.read_json()
        ldata = Store.read_json_for_left()

        if RANDOM_LOWER_PRIMARY != []:
            level = RANDOM_LOWER_PRIMARY[-1][0]
            index = RANDOM_LOWER_PRIMARY[-1][-1]

            user = data[LOWERUSERPRIMARY][level][index]
            ldata[LOWERUSERPRIMARY].append(user)
            del data[LOWERUSERPRIMARY][level][index]

            t = Thread(target=Store.write_json, args=[data])
            t.start()
            t.join()
            t1 = Thread(target=Store.write_json_for_left, args=[ldata])
            t1.start()
            t1.join()

            self.connect_lower_primary()
            self.connect_lower_primary_Left()
            self.data_frame()

    def deleteLowerAdvancedForActive(self):
        data = Store.read_json()
        ldata = Store.read_json_for_left()

        if RANDOM_LOWER_ADVANCED != []:
            level = RANDOM_LOWER_ADVANCED[-1][0]
            index = RANDOM_LOWER_ADVANCED[-1][-1]
            stream = RANDOM_LOWER_ADVANCED[-1][-2]

            ldata[LOWERUSERADVANCED].append(
                data[LOWERUSERADVANCED][level][stream][index])
            del data[LOWERUSERADVANCED][level][stream][index]

            t = Thread(target=Store.write_json, args=[data])
            t.start()
            t.join()
            t2 = Thread(target=Store.write_json_for_left, args=[ldata])
            t2.start()
            t2.join()

            self.connect_lower_advanced()
            self.connect_lower_advanced_left()
            self.data_frame()

    # Left Status For Delete

    def deleteInterForLeft(self):
        ldata = Store.read_json_for_left()

        if ldata[INTERUSER] != [] and RANDOM_INTER_LEFT != []:
            del ldata[INTERUSER][RANDOM_INTER_LEFT[-1]]
            t1 = Thread(target=Store.write_json_for_left, args=[ldata])
            t1.start()
            t1.join()
            self.connect_inter_left()

    def deleteLowerOdrinaryForLeft(self):
        ldata = Store.read_json_for_left()

        if RANDOM_LOWER_ODRINAEY_LEFT != [] and ldata[LOWERUSERORDINARY] != []:

            del ldata[LOWERUSERORDINARY][RANDOM_LOWER_ODRINAEY_LEFT[-1]]

            t1 = Thread(target=Store.write_json_for_left, args=[ldata])
            t1.start()
            t1.join()
            self.connect_lower_odrinary_left()

    def deleteLowerPrimaryForLeft(self):
        ldata = Store.read_json_for_left()

        if RANDOM_LOWER_PRIMARY_LEFT != [] and ldata[LOWERUSERPRIMARY] != []:
            del ldata[LOWERUSERPRIMARY][RANDOM_LOWER_PRIMARY_LEFT[-1]]

            t1 = Thread(target=Store.write_json_for_left, args=[ldata])
            t1.start()
            t1.join()
            self.connect_lower_primary_Left()

    def deleteLowerAdvancedForLeft(self):
        ldata = Store.read_json_for_left()

        if RANDOM_LOWER_ADVANCED_LEFT != [] and ldata[LOWERUSERADVANCED] != []:
            del ldata[LOWERUSERADVANCED][RANDOM_LOWER_ADVANCED_LEFT[-1]]

            t1 = Thread(target=Store.write_json_for_left, args=[ldata])
            t1.start()
            t1.join()
            self.connect_lower_advanced_left()

    # Main Frame For Base Search
    def main_frame_for_base_search(self):
        if self.actionsOfFrame == False:
            self.frame_resalt = QFrame(self.ui.scrollAreaWidgetContents_2)
            self.frame_resalt.setObjectName(u"frame_resalt")
            self.frame_resalt.setStyleSheet(u"QFrame{\n"
                                            "	border: none;\n"
                                            "	background-color: rgb(26, 27, 34);\n"
                                            "	border-radius: 10px;\n"
                                            "}\n"
                                            "QFrame:hover{\n"
                                            "	border: 2px solid rgb(0, 126, 225);\n"
                                            "}")
            self.frame_resalt.setFrameShape(QFrame.StyledPanel)
            self.frame_resalt.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_16 = QVBoxLayout(self.frame_resalt)
            self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
            self.ui.verticalLayout_26.addWidget(self.frame_resalt)
            self.actionsOfFrame = True
        else:
            self.frame_resalt.deleteLater()
            self.frame_resalt = QFrame(self.ui.scrollAreaWidgetContents_2)
            self.frame_resalt.setObjectName(u"frame_resalt")
            self.frame_resalt.setStyleSheet(u"QFrame{\n"
                                            "	border: none;\n"
                                            "	background-color: rgb(26, 27, 34);\n"
                                            "	border-radius: 10px;\n"
                                            "}\n"
                                            "QFrame:hover{\n"
                                            "	border: 2px solid rgb(0, 126, 225);\n"
                                            "}")
            self.frame_resalt.setFrameShape(QFrame.StyledPanel)
            self.frame_resalt.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_16 = QVBoxLayout(self.frame_resalt)
            self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
            self.ui.verticalLayout_26.addWidget(self.frame_resalt)

    # Not Fount info frame

    def not_found_frame(self):
        font2 = QFont()
        font2.setFamily(u"MesloLGL Nerd Font")
        font2.setPointSize(20)

        self.frame_search_1 = QFrame(self.frame_resalt)
        self.frame_search_1.setObjectName(u"frame_search_1")
        self.frame_search_1.setStyleSheet(u"QFrame{\n"
                                          "	background-color: none;\n"
                                          "	border: 0px solid;\n"
                                          "	border-radius: 0px;\n"
                                          "}")
        self.frame_search_1.setFrameShape(QFrame.StyledPanel)
        self.frame_search_1.setFrameShadow(QFrame.Raised)
        self.frame_search_1.setMinimumSize(QSize(16777215, 200))
        self.frame_search_1.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_27 = QVBoxLayout(self.frame_search_1)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_info_search_1 = QLabel(self.frame_search_1)
        self.label_info_search_1.setObjectName(u"label_info_search_1")
        self.label_info_search_1.setFont(font2)
        self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                               "border: none;\n"
                                               "padding-left: 15px;\n"
                                               "color: white;")
        self.label_info_search_1.setText("""
                <html>
                    </head>
                    <body>
                        <h2 align=\"center\"> NOT FOUND </h2>
                        <p align=\"center\"><img src = \"./packges/app/items/img/notFound100.png\"></p>
                    <body>
                </html>
            """)

        self.verticalLayout_27.addWidget(self.label_info_search_1)
        self.horizontalLayout_16.addWidget(self.frame_search_1)

    # inti frame for search resalt
    def inti_frame_for_search_resalt(self, targetText, objectName=None):
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)

        font2 = QFont()
        font2.setFamily(u"MesloLGL Nerd Font")
        font2.setPointSize(10)

        font3 = QFont()
        font3.setFamily(u"MesloLGM NF")
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setWeight(50)

        icon6 = QIcon()
        icon6.addFile(u"./packges/app/items/icons/24x24/cil-user-unfollow.png",
                      QSize(), QIcon.Normal, QIcon.Off)

        if objectName != None:
            if objectName == "inter":
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter)].setObjectName(u"frame_search_1")
                self.vars_names["frame_" + objectName + "_" + str(self.counter_inter)].setStyleSheet(u"QFrame{\n"
                                                                                                     "	background-color: none;\n"
                                                                                                     "	border: 1px solid rgb(0, 127, 226);\n"
                                                                                                     "	border-radius: 10px;\n"
                                                                                                     "}")
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter)].setFrameShape(QFrame.StyledPanel)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter)].setFrameShadow(QFrame.Raised)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter)].setMinimumSize(QSize(16777215, 400))
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter)].setMaximumSize(QSize(16777215, 400))
                self.verticalLayout_27 = QVBoxLayout(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_inter)])
                self.verticalLayout_27.setObjectName(u"verticalLayout_27")
                self.label_info_search_1 = QLabel(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_inter)])
                self.label_info_search_1.setObjectName(u"label_info_search_1")
                self.label_info_search_1.setFont(self.font_info)
                self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                                       "border: none;\n"
                                                       "padding-left: 15px;\n"
                                                       "color: white;")
                self.label_info_search_1.setText(targetText)

                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.label_info_search_1.installEventFilter(self)
                self.label_info_search_1.setCursor(QCursor(Qt.IBeamCursor))

                self.frame_search_delet_bar_6 = QFrame(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_inter)])
                self.frame_search_delet_bar_6.setObjectName(
                    u"frame_search_delet_bar_6")
                self.frame_search_delet_bar_6.setMaximumSize(
                    QSize(16777215, 40))
                self.frame_search_delet_bar_6.setStyleSheet(
                    u"border: none;\n background-color: rgb(40, 41, 52);")
                self.frame_search_delet_bar_6.setFrameShape(QFrame.StyledPanel)
                self.frame_search_delet_bar_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_17 = QHBoxLayout(
                    self.frame_search_delet_bar_6)
                self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
                self.label_info_user_search = QLabel(
                    self.frame_search_delet_bar_6)
                self.label_info_user_search.setObjectName(
                    u"label_info_user_search")
                self.label_info_user_search.setFont(font3)
                self.label_info_user_search.setStyleSheet(
                    u"color: white;\n padding-left: 20px;")
                self.label_info_user_search.setAlignment(Qt.AlignLeft)
                self.label_info_user_search.setText(
                    u"This <b>\"Delete\"</b> is Add in to Recycle Bin ")

                self.horizontalLayout_17.addWidget(self.label_info_user_search)

                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter)] = QPushButton(self.frame_search_delet_bar_6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter)].setMinimumSize(QSize(100, 25))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter)].setMaximumSize(QSize(100, 40))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter)].setFont(font4)
                self.vars_names["btn_"+objectName+"_"+str(self.counter_inter)].setStyleSheet(u"QPushButton{\n"
                                                                                             "	color: rgb(255, 255, 255);\n"
                                                                                             "	background-color: rgb(0, 127, 226);\n"
                                                                                             "	border: 0px solid;\n"
                                                                                             "	border-radius: 5px;\n"
                                                                                             "}\n"
                                                                                             "QPushButton:hover{\n"
                                                                                             "	background-color: rgb(85, 170, 255);\n"
                                                                                             "}\n"
                                                                                             "QPushButton:pressed{\n"
                                                                                             "	background-color: rgba(85, 170, 255, 100);\n"
                                                                                             "}")
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter)].setIcon(icon6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter)].setText(u" Delete")

                self.horizontalLayout_17.addWidget(
                    self.vars_names["btn_"+objectName+"_"+str(self.counter_inter)])
                self.verticalLayout_27.addWidget(self.frame_search_delet_bar_6)
                self.horizontalLayout_16.addWidget(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_inter)])
                self.counter_inter += 1

            elif objectName == "lower":
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower)].setObjectName(u"frame_search_1")
                self.vars_names["frame_" + objectName + "_" + str(self.counter_lower)].setStyleSheet(u"QFrame{\n"
                                                                                                     "	background-color: none;\n"
                                                                                                     "	border: 1px solid rgb(0, 127, 226);\n"
                                                                                                     "	border-radius: 10px;\n"
                                                                                                     "}")
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower)].setFrameShape(QFrame.StyledPanel)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower)].setFrameShadow(QFrame.Raised)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower)].setMinimumSize(QSize(16777215, 400))
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower)].setMaximumSize(QSize(16777215, 400))
                self.verticalLayout_27 = QVBoxLayout(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_lower)])
                self.verticalLayout_27.setObjectName(u"verticalLayout_27")
                self.label_info_search_1 = QLabel(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_lower)])
                self.label_info_search_1.setObjectName(u"label_info_search_1")
                self.label_info_search_1.setFont(font2)
                self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                                       "border: none;\n"
                                                       "padding-left: 15px;\n"
                                                       "color: white;")
                self.label_info_search_1.setText(targetText)

                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.label_info_search_1.setTextInteractionFlags(
                    Qt.TextSelectableByMouse)
                self.label_info_search_1.installEventFilter(self)
                self.label_info_search_1.setCursor(QCursor(Qt.IBeamCursor))

                self.frame_search_delet_bar_6 = QFrame(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_lower)])
                self.frame_search_delet_bar_6.setObjectName(
                    u"frame_search_delet_bar_6")
                self.frame_search_delet_bar_6.setMaximumSize(
                    QSize(16777215, 40))
                self.frame_search_delet_bar_6.setStyleSheet(
                    u"border: none;\n background-color: rgb(40, 41, 52);")
                self.frame_search_delet_bar_6.setFrameShape(QFrame.StyledPanel)
                self.frame_search_delet_bar_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_17 = QHBoxLayout(
                    self.frame_search_delet_bar_6)
                self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
                self.label_info_user_search = QLabel(
                    self.frame_search_delet_bar_6)
                self.label_info_user_search.setObjectName(
                    u"label_info_user_search")
                self.label_info_user_search.setFont(font3)
                self.label_info_user_search.setStyleSheet(
                    u"color: white;\n padding-left: 20px;")
                self.label_info_user_search.setAlignment(Qt.AlignLeft)
                self.label_info_user_search.setText(
                    u"This <b>\"Delete\"</b> is Add in to Recycle Bin ")

                self.horizontalLayout_17.addWidget(self.label_info_user_search)

                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower)] = QPushButton(self.frame_search_delet_bar_6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower)].setMinimumSize(QSize(100, 25))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower)].setMaximumSize(QSize(100, 40))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower)].setFont(font4)
                self.vars_names["btn_"+objectName+"_"+str(self.counter_lower)].setStyleSheet(u"QPushButton{\n"
                                                                                             "	color: rgb(255, 255, 255);\n"
                                                                                             "	background-color: rgb(0, 127, 226);\n"
                                                                                             "	border: 0px solid;\n"
                                                                                             "	border-radius: 5px;\n"
                                                                                             "}\n"
                                                                                             "QPushButton:hover{\n"
                                                                                             "	background-color: rgb(85, 170, 255);\n"
                                                                                             "}\n"
                                                                                             "QPushButton:pressed{\n"
                                                                                             "	background-color: rgba(85, 170, 255, 100);\n"
                                                                                             "}")
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower)].setIcon(icon6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower)].setText(u" Delete")

                self.horizontalLayout_17.addWidget(
                    self.vars_names["btn_"+objectName+"_"+str(self.counter_lower)])
                self.verticalLayout_27.addWidget(self.frame_search_delet_bar_6)
                self.horizontalLayout_16.addWidget(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_lower)])

                self.counter_lower += 1

            elif objectName == "inter_l":
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter_l)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter_l)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" + str(self.counter_inter_l)].setStyleSheet(u"QFrame{\n"
                                                                                                       "	background-color: none;\n"
                                                                                                       "	border: 1px solid rgb(0, 127, 226);\n"
                                                                                                       "	border-radius: 10px;\n"
                                                                                                       "}")
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter_l)].setFrameShape(QFrame.StyledPanel)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter_l)].setFrameShadow(QFrame.Raised)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter_l)].setMinimumSize(QSize(16777215, 400))
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_inter_l)].setMaximumSize(QSize(16777215, 400))
                self.verticalLayout_27 = QVBoxLayout(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_inter_l)])
                self.verticalLayout_27.setObjectName(u"verticalLayout_27")
                self.label_info_search_1 = QLabel(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_inter_l)])
                self.label_info_search_1.setObjectName(u"label_info_search_1")
                self.label_info_search_1.setFont(font2)
                self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                                       "border: none;\n"
                                                       "padding-left: 15px;\n"
                                                       "color: white;")
                self.label_info_search_1.setText(targetText)

                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.label_info_search_1.setTextInteractionFlags(
                    Qt.TextSelectableByMouse)
                self.label_info_search_1.installEventFilter(self)
                self.label_info_search_1.setCursor(QCursor(Qt.IBeamCursor))

                self.frame_search_delet_bar_6 = QFrame(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_inter_l)])
                self.frame_search_delet_bar_6.setObjectName(
                    u"frame_search_delet_bar_6")
                self.frame_search_delet_bar_6.setMaximumSize(
                    QSize(16777215, 40))
                self.frame_search_delet_bar_6.setStyleSheet(
                    u"border: none;\n background-color: rgb(40, 41, 52);")
                self.frame_search_delet_bar_6.setFrameShape(QFrame.StyledPanel)
                self.frame_search_delet_bar_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_17 = QHBoxLayout(
                    self.frame_search_delet_bar_6)
                self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
                self.label_info_user_search = QLabel(
                    self.frame_search_delet_bar_6)
                self.label_info_user_search.setObjectName(
                    u"label_info_user_search")
                self.label_info_user_search.setFont(font3)
                self.label_info_user_search.setStyleSheet(
                    u"color: white;\n padding-left: 20px;")
                self.label_info_user_search.setAlignment(Qt.AlignLeft)
                self.label_info_user_search.setText(
                    u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>")

                self.horizontalLayout_17.addWidget(self.label_info_user_search)

                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter_l)] = QPushButton(self.frame_search_delet_bar_6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter_l)].setMinimumSize(QSize(100, 25))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter_l)].setMaximumSize(QSize(100, 40))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter_l)].setFont(font4)
                self.vars_names["btn_"+objectName+"_"+str(self.counter_inter_l)].setStyleSheet(u"QPushButton{\n"
                                                                                               "	color: rgb(255, 255, 255);\n"
                                                                                               "	background-color: rgb(0, 127, 226);\n"
                                                                                               "	border: 0px solid;\n"
                                                                                               "	border-radius: 5px;\n"
                                                                                               "}\n"
                                                                                               "QPushButton:hover{\n"
                                                                                               "	background-color: rgb(85, 170, 255);\n"
                                                                                               "}\n"
                                                                                               "QPushButton:pressed{\n"
                                                                                               "	background-color: rgba(85, 170, 255, 100);\n"
                                                                                               "}")
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter_l)].setIcon(icon6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_inter_l)].setText(u" Delete")

                self.horizontalLayout_17.addWidget(
                    self.vars_names["btn_"+objectName+"_"+str(self.counter_inter_l)])
                self.verticalLayout_27.addWidget(self.frame_search_delet_bar_6)
                self.horizontalLayout_16.addWidget(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_inter_l)])

                self.counter_inter_l += 1
            elif objectName == "adv_lower":
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower)].setStyleSheet(u"QFrame{\n"
                                                                                                        "    background-color: none;\n"
                                                                                                        "    border: 1px solid rgb(0, 127, 226);\n"
                                                                                                        "    border-radius: 10px;\n"
                                                                                                        "}")
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower)].setFrameShape(QFrame.StyledPanel)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower)].setFrameShadow(QFrame.Raised)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower)].setMinimumSize(QSize(16777215, 500))
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower)].setMaximumSize(QSize(16777215, 500))
                self.verticalLayout_27 = QVBoxLayout(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower)])
                self.verticalLayout_27.setObjectName(u"verticalLayout_27")
                self.label_info_search_1 = QLabel(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower)])
                self.label_info_search_1.setObjectName(u"label_info_search_1")
                self.label_info_search_1.setFont(font2)
                self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                                       "border: none;\n"
                                                       "padding-left: 15px;\n"
                                                       "color: white;")
                self.label_info_search_1.setText(targetText)

                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.label_info_search_1.setTextInteractionFlags(
                    Qt.TextSelectableByMouse)
                self.label_info_search_1.installEventFilter(self)
                self.label_info_search_1.setCursor(QCursor(Qt.IBeamCursor))

                self.frame_search_delet_bar_6 = QFrame(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower)])
                self.frame_search_delet_bar_6.setObjectName(
                    u"frame_search_delet_bar_6")
                self.frame_search_delet_bar_6.setMaximumSize(
                    QSize(16777215, 40))
                self.frame_search_delet_bar_6.setStyleSheet(
                    u"border: none;\n background-color: rgb(40, 41, 52);")
                self.frame_search_delet_bar_6.setFrameShape(QFrame.StyledPanel)
                self.frame_search_delet_bar_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_17 = QHBoxLayout(
                    self.frame_search_delet_bar_6)
                self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
                self.label_info_user_search = QLabel(
                    self.frame_search_delet_bar_6)
                self.label_info_user_search.setObjectName(
                    u"label_info_user_search")
                self.label_info_user_search.setFont(font3)
                self.label_info_user_search.setStyleSheet(
                    u"color: white;\n padding-left: 20px;")
                self.label_info_user_search.setAlignment(Qt.AlignLeft)
                self.label_info_user_search.setText(
                    u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>")

                self.horizontalLayout_17.addWidget(self.label_info_user_search)

                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower)] = QPushButton(self.frame_search_delet_bar_6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower)].setMinimumSize(QSize(100, 25))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower)].setMaximumSize(QSize(100, 40))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower)].setFont(font4)
                self.vars_names["btn_"+objectName+"_"+str(self.counter_ad_lower)].setStyleSheet(u"QPushButton{\n"
                                                                                                "    color: rgb(255, 255, 255);\n"
                                                                                                "    background-color: rgb(0, 127, 226);\n"
                                                                                                "    border: 0px solid;\n"
                                                                                                "    border-radius: 5px;\n"
                                                                                                "}\n"
                                                                                                "QPushButton:hover{\n"
                                                                                                "    background-color: rgb(85, 170, 255);\n"
                                                                                                "}\n"
                                                                                                "QPushButton:pressed{\n"
                                                                                                "    background-color: rgba(85, 170, 255, 100);\n"
                                                                                                "}")
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower)].setIcon(icon6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower)].setText(u" Delete")

                self.horizontalLayout_17.addWidget(
                    self.vars_names["btn_"+objectName+"_"+str(self.counter_ad_lower)])
                self.verticalLayout_27.addWidget(self.frame_search_delet_bar_6)
                self.horizontalLayout_16.addWidget(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower)])

                self.counter_ad_lower += 1
            elif objectName == "adv_lower_l":
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower_l)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower_l)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower_l)].setStyleSheet(u"QFrame{\n"
                                                                                                          "    background-color: none;\n"
                                                                                                          "    border: 1px solid rgb(0, 127, 226);\n"
                                                                                                          "    border-radius: 10px;\n"
                                                                                                          "}")
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower_l)].setFrameShape(QFrame.StyledPanel)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower_l)].setFrameShadow(QFrame.Raised)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower_l)].setMinimumSize(QSize(16777215, 500))
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_ad_lower_l)].setMaximumSize(QSize(16777215, 500))
                self.verticalLayout_27 = QVBoxLayout(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower_l)])
                self.verticalLayout_27.setObjectName(u"verticalLayout_27")
                self.label_info_search_1 = QLabel(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower_l)])
                self.label_info_search_1.setObjectName(u"label_info_search_1")
                self.label_info_search_1.setFont(font2)
                self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                                       "border: none;\n"
                                                       "padding-left: 15px;\n"
                                                       "color: white;")
                self.label_info_search_1.setText(targetText)

                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.label_info_search_1.setTextInteractionFlags(
                    Qt.TextSelectableByMouse)
                self.label_info_search_1.installEventFilter(self)
                self.label_info_search_1.setCursor(QCursor(Qt.IBeamCursor))

                self.frame_search_delet_bar_6 = QFrame(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower_l)])
                self.frame_search_delet_bar_6.setObjectName(
                    u"frame_search_delet_bar_6")
                self.frame_search_delet_bar_6.setMaximumSize(
                    QSize(16777215, 40))
                self.frame_search_delet_bar_6.setStyleSheet(
                    u"border: none;\n background-color: rgb(40, 41, 52);")
                self.frame_search_delet_bar_6.setFrameShape(QFrame.StyledPanel)
                self.frame_search_delet_bar_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_17 = QHBoxLayout(
                    self.frame_search_delet_bar_6)
                self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
                self.label_info_user_search = QLabel(
                    self.frame_search_delet_bar_6)
                self.label_info_user_search.setObjectName(
                    u"label_info_user_search")
                self.label_info_user_search.setFont(font3)
                self.label_info_user_search.setStyleSheet(
                    u"color: white;\n padding-left: 20px;")
                self.label_info_user_search.setAlignment(Qt.AlignLeft)
                self.label_info_user_search.setText(
                    u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>")

                self.horizontalLayout_17.addWidget(self.label_info_user_search)

                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower_l)] = QPushButton(self.frame_search_delet_bar_6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower_l)].setMinimumSize(QSize(100, 25))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower_l)].setMaximumSize(QSize(100, 40))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower_l)].setFont(font4)
                self.vars_names["btn_"+objectName+"_"+str(self.counter_ad_lower_l)].setStyleSheet(u"QPushButton{\n"
                                                                                                  "    color: rgb(255, 255, 255);\n"
                                                                                                  "    background-color: rgb(0, 127, 226);\n"
                                                                                                  "    border: 0px solid;\n"
                                                                                                  "    border-radius: 5px;\n"
                                                                                                  "}\n"
                                                                                                  "QPushButton:hover{\n"
                                                                                                  "    background-color: rgb(85, 170, 255);\n"
                                                                                                  "}\n"
                                                                                                  "QPushButton:pressed{\n"
                                                                                                  "    background-color: rgba(85, 170, 255, 100);\n"
                                                                                                  "}")
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower_l)].setIcon(icon6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_ad_lower_l)].setText(u" Delete")

                self.horizontalLayout_17.addWidget(
                    self.vars_names["btn_"+objectName+"_"+str(self.counter_ad_lower_l)])
                self.verticalLayout_27.addWidget(self.frame_search_delet_bar_6)
                self.horizontalLayout_16.addWidget(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_ad_lower_l)])

                self.counter_ad_lower_l += 1

            elif objectName == "pri_lower":
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower)].setStyleSheet(u"QFrame{\n"
                                                                                                         "    background-color: none;\n"
                                                                                                         "    border: 1px solid rgb(0, 127, 226);\n"
                                                                                                         "    border-radius: 10px;\n"
                                                                                                         "}")
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower)].setFrameShape(QFrame.StyledPanel)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower)].setFrameShadow(QFrame.Raised)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower)].setMinimumSize(QSize(16777215, 500))
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower)].setMaximumSize(QSize(16777215, 500))
                self.verticalLayout_27 = QVBoxLayout(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower)])
                self.verticalLayout_27.setObjectName(u"verticalLayout_27")
                self.label_info_search_1 = QLabel(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower
                                                                      )])
                self.label_info_search_1.setObjectName(u"label_info_search_1")
                self.label_info_search_1.setFont(font2)
                self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                                       "border: none;\n"
                                                       "padding-left: 15px;\n"
                                                       "color: white;")
                self.label_info_search_1.setText(targetText)

                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.label_info_search_1.setTextInteractionFlags(
                    Qt.TextSelectableByMouse)
                self.label_info_search_1.installEventFilter(self)
                self.label_info_search_1.setCursor(QCursor(Qt.IBeamCursor))

                self.frame_search_delet_bar_6 = QFrame(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower)])
                self.frame_search_delet_bar_6.setObjectName(
                    u"frame_search_delet_bar_6")
                self.frame_search_delet_bar_6.setMaximumSize(
                    QSize(16777215, 40))
                self.frame_search_delet_bar_6.setStyleSheet(
                    u"border: none;\n background-color: rgb(40, 41, 52);")
                self.frame_search_delet_bar_6.setFrameShape(QFrame.StyledPanel)
                self.frame_search_delet_bar_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_17 = QHBoxLayout(
                    self.frame_search_delet_bar_6)
                self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
                self.label_info_user_search = QLabel(
                    self.frame_search_delet_bar_6)
                self.label_info_user_search.setObjectName(
                    u"label_info_user_search")
                self.label_info_user_search.setFont(font3)
                self.label_info_user_search.setStyleSheet(
                    u"color: white;\n padding-left: 20px;")
                self.label_info_user_search.setAlignment(Qt.AlignLeft)
                self.label_info_user_search.setText(
                    u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>")

                self.horizontalLayout_17.addWidget(self.label_info_user_search)

                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower)] = QPushButton(self.frame_search_delet_bar_6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower)].setMinimumSize(QSize(100, 25))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower)].setMaximumSize(QSize(100, 40))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower)].setFont(font4)
                self.vars_names["btn_"+objectName+"_"+str(self.counter_pri_lower)].setStyleSheet(u"QPushButton{\n"
                                                                                                 "    color: rgb(255, 255, 255);\n"
                                                                                                 "    background-color: rgb(0, 127, 226);\n"
                                                                                                 "    border: 0px solid;\n"
                                                                                                 "    border-radius: 5px;\n"
                                                                                                 "}\n"
                                                                                                 "QPushButton:hover{\n"
                                                                                                 "    background-color: rgb(85, 170, 255);\n"
                                                                                                 "}\n"
                                                                                                 "QPushButton:pressed{\n"
                                                                                                 "    background-color: rgba(85, 170, 255, 100);\n"
                                                                                                 "}")
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower)].setIcon(icon6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower)].setText(u" Delete")

                self.horizontalLayout_17.addWidget(
                    self.vars_names["btn_"+objectName+"_"+str(self.counter_pri_lower)])
                self.verticalLayout_27.addWidget(self.frame_search_delet_bar_6)
                self.horizontalLayout_16.addWidget(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower)])

                self.counter_pri_lower += 1

            elif objectName == "pri_lower_l":
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower_left)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower_left)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower_left)].setStyleSheet(u"QFrame{\n"
                                                                                                              "    background-color: none;\n"
                                                                                                              "    border: 1px solid rgb(0, 127, 226);\n"
                                                                                                              "    border-radius: 10px;\n"
                                                                                                              "}")
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower_left)].setFrameShape(QFrame.StyledPanel)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower_left)].setFrameShadow(QFrame.Raised)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower_left)].setMinimumSize(QSize(16777215, 500))
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_pri_lower_left)].setMaximumSize(QSize(16777215, 500))
                self.verticalLayout_27 = QVBoxLayout(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower_left)])
                self.verticalLayout_27.setObjectName(u"verticalLayout_27")
                self.label_info_search_1 = QLabel(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower_left
                                                                      )])
                self.label_info_search_1.setObjectName(u"label_info_search_1")
                self.label_info_search_1.setFont(font2)
                self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                                       "border: none;\n"
                                                       "padding-left: 15px;\n"
                                                       "color: white;")
                self.label_info_search_1.setText(targetText)

                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.label_info_search_1.setTextInteractionFlags(
                    Qt.TextSelectableByMouse)
                self.label_info_search_1.installEventFilter(self)
                self.label_info_search_1.setCursor(QCursor(Qt.IBeamCursor))

                self.frame_search_delet_bar_6 = QFrame(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower_left)])
                self.frame_search_delet_bar_6.setObjectName(
                    u"frame_search_delet_bar_6")
                self.frame_search_delet_bar_6.setMaximumSize(
                    QSize(16777215, 40))
                self.frame_search_delet_bar_6.setStyleSheet(
                    u"border: none;\n background-color: rgb(40, 41, 52);")
                self.frame_search_delet_bar_6.setFrameShape(QFrame.StyledPanel)
                self.frame_search_delet_bar_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_17 = QHBoxLayout(
                    self.frame_search_delet_bar_6)
                self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
                self.label_info_user_search = QLabel(
                    self.frame_search_delet_bar_6)
                self.label_info_user_search.setObjectName(
                    u"label_info_user_search")
                self.label_info_user_search.setFont(font3)
                self.label_info_user_search.setStyleSheet(
                    u"color: white;\n padding-left: 20px;")
                self.label_info_user_search.setAlignment(Qt.AlignLeft)
                self.label_info_user_search.setText(
                    u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>")

                self.horizontalLayout_17.addWidget(self.label_info_user_search)

                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower_left)] = QPushButton(self.frame_search_delet_bar_6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower_left)].setMinimumSize(QSize(100, 25))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower_left)].setMaximumSize(QSize(100, 40))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower_left)].setFont(font4)
                self.vars_names["btn_"+objectName+"_"+str(self.counter_pri_lower_left)].setStyleSheet(u"QPushButton{\n"
                                                                                                      "    color: rgb(255, 255, 255);\n"
                                                                                                      "    background-color: rgb(0, 127, 226);\n"
                                                                                                      "    border: 0px solid;\n"
                                                                                                      "    border-radius: 5px;\n"
                                                                                                      "}\n"
                                                                                                      "QPushButton:hover{\n"
                                                                                                      "    background-color: rgb(85, 170, 255);\n"
                                                                                                      "}\n"
                                                                                                      "QPushButton:pressed{\n"
                                                                                                      "    background-color: rgba(85, 170, 255, 100);\n"
                                                                                                      "}")
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower_left)].setIcon(icon6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_pri_lower_left)].setText(u" Delete")

                self.horizontalLayout_17.addWidget(
                    self.vars_names["btn_"+objectName+"_"+str(self.counter_pri_lower_left)])
                self.verticalLayout_27.addWidget(self.frame_search_delet_bar_6)
                self.horizontalLayout_16.addWidget(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_pri_lower_left)])

                self.counter_pri_lower_left += 1

            else:
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower_l)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower_l)] = QFrame(self.frame_resalt)
                self.vars_names["frame_" + objectName + "_" + str(self.counter_lower_l)].setStyleSheet(u"QFrame{\n"
                                                                                                       "	background-color: none;\n"
                                                                                                       "	border: 1px solid rgb(0, 127, 226);\n"
                                                                                                       "	border-radius: 10px;\n"
                                                                                                       "}")
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower_l)].setFrameShape(QFrame.StyledPanel)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower_l)].setFrameShadow(QFrame.Raised)
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower_l)].setMinimumSize(QSize(16777215, 400))
                self.vars_names["frame_" + objectName + "_" +
                                str(self.counter_lower_l)].setMaximumSize(QSize(16777215, 400))
                self.verticalLayout_27 = QVBoxLayout(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_lower_l)])
                self.verticalLayout_27.setObjectName(u"verticalLayout_27")
                self.label_info_search_1 = QLabel(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_lower_l)])
                self.label_info_search_1.setObjectName(u"label_info_search_1")
                self.label_info_search_1.setFont(font2)
                self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                                       "border: none;\n"
                                                       "padding-left: 15px;\n"
                                                       "color: white;")
                self.label_info_search_1.setText(targetText)

                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.verticalLayout_27.addWidget(self.label_info_search_1)
                self.label_info_search_1.setTextInteractionFlags(
                    Qt.TextSelectableByMouse)
                self.label_info_search_1.installEventFilter(self)
                self.label_info_search_1.setCursor(QCursor(Qt.IBeamCursor))

                self.frame_search_delet_bar_6 = QFrame(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_lower_l)])
                self.frame_search_delet_bar_6.setMaximumSize(
                    QSize(16777215, 40))
                self.frame_search_delet_bar_6.setStyleSheet(
                    u"border: none;\n background-color: rgb(40, 41, 52);")
                self.frame_search_delet_bar_6.setFrameShape(QFrame.StyledPanel)
                self.frame_search_delet_bar_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_17 = QHBoxLayout(
                    self.frame_search_delet_bar_6)
                self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
                self.label_info_user_search = QLabel(
                    self.frame_search_delet_bar_6)
                self.label_info_user_search.setFont(font3)
                self.label_info_user_search.setStyleSheet(
                    u"color: white;\n padding-left: 20px;")
                self.label_info_user_search.setAlignment(Qt.AlignLeft)
                self.label_info_user_search.setText(
                    u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>")

                self.horizontalLayout_17.addWidget(self.label_info_user_search)

                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower_l)] = QPushButton(self.frame_search_delet_bar_6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower_l)].setMinimumSize(QSize(100, 25))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower_l)].setMaximumSize(QSize(100, 40))
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower_l)].setFont(font4)
                self.vars_names["btn_"+objectName+"_"+str(self.counter_lower_l)].setStyleSheet(u"QPushButton{\n"
                                                                                               "	color: rgb(255, 255, 255);\n"
                                                                                               "	background-color: rgb(0, 127, 226);\n"
                                                                                               "	border: 0px solid;\n"
                                                                                               "	border-radius: 5px;\n"
                                                                                               "}\n"
                                                                                               "QPushButton:hover{\n"
                                                                                               "	background-color: rgb(85, 170, 255);\n"
                                                                                               "}\n"
                                                                                               "QPushButton:pressed{\n"
                                                                                               "	background-color: rgba(85, 170, 255, 100);\n"
                                                                                               "}")
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower_l)].setIcon(icon6)
                self.vars_names["btn_"+objectName+"_" +
                                str(self.counter_lower_l)].setText(u" Delete")

                self.horizontalLayout_17.addWidget(
                    self.vars_names["btn_"+objectName+"_"+str(self.counter_lower_l)])
                self.verticalLayout_27.addWidget(self.frame_search_delet_bar_6)
                self.horizontalLayout_16.addWidget(
                    self.vars_names["frame_" + objectName + "_" + str(self.counter_lower_l)])

                self.counter_lower_l += 1

        else:
            self.frame_result_roll = QFrame(self.frame_resalt)
            self.frame_result_roll.setStyleSheet(u"QFrame{\n"
                                                 "	background-color: none;\n"
                                                 "	border: 1px solid rgb(0, 127, 226);\n"
                                                 "	border-radius: 10px;\n"
                                                 "}")
            self.frame_result_roll.setFrameShape(QFrame.StyledPanel)
            self.frame_result_roll.setFrameShadow(QFrame.Raised)
            self.frame_result_roll.setMinimumSize(QSize(16777215, 500))
            self.frame_result_roll.setMaximumSize(QSize(16777215, 500))
            self.verticalLayout_27 = QVBoxLayout(self.frame_result_roll)
            self.verticalLayout_27.setObjectName(u"verticalLayout_27")
            self.label_info_search_1 = QLabel(self.frame_result_roll)
            self.label_info_search_1.setObjectName(u"label_info_search_1")
            self.label_info_search_1.setFont(font2)
            self.label_info_search_1.setStyleSheet(u"background-color: none;\n"
                                                   "border: none;\n"
                                                   "padding-left: 15px;\n"
                                                   "color: white;")
            self.label_info_search_1.setText(targetText)

            self.verticalLayout_27.addWidget(self.label_info_search_1)
            self.verticalLayout_27.addWidget(self.label_info_search_1)
            self.label_info_search_1.setTextInteractionFlags(
                Qt.TextSelectableByMouse)
            self.label_info_search_1.installEventFilter(self)
            self.label_info_search_1.setCursor(QCursor(Qt.IBeamCursor))

            self.frame_search_delet_bar_6 = QFrame(self.frame_result_roll)
            self.frame_search_delet_bar_6.setObjectName(
                u"frame_search_delet_bar_6")
            self.frame_search_delet_bar_6.setMaximumSize(
                QSize(16777215, 40))
            self.frame_search_delet_bar_6.setStyleSheet(
                u"border: none;\n background-color: rgb(40, 41, 52);")
            self.frame_search_delet_bar_6.setFrameShape(QFrame.StyledPanel)
            self.frame_search_delet_bar_6.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_17 = QHBoxLayout(
                self.frame_search_delet_bar_6)
            self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
            self.label_info_user_search = QLabel(
                self.frame_search_delet_bar_6)
            self.label_info_user_search.setObjectName(
                u"label_info_user_search")
            self.label_info_user_search.setFont(font3)
            self.label_info_user_search.setStyleSheet(
                u"color: white;\n padding-left: 20px;")
            self.label_info_user_search.setAlignment(Qt.AlignLeft)
            self.label_info_user_search.setText(
                u"This <b>\"Delete\"</b> is Add in to Recycle Bin ")

            self.horizontalLayout_17.addWidget(self.label_info_user_search)

            self.btn_roll_deleter = QPushButton(self.frame_search_delet_bar_6)
            self.btn_roll_deleter.setMinimumSize(QSize(100, 25))
            self.btn_roll_deleter.setMaximumSize(QSize(100, 40))
            self.btn_roll_deleter.setFont(font4)
            self.btn_roll_deleter.setStyleSheet(u"QPushButton{\n"
                                                "	color: rgb(255, 255, 255);\n"
                                                "	background-color: rgb(0, 127, 226);\n"
                                                "	border: 0px solid;\n"
                                                "	border-radius: 5px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "	background-color: rgb(85, 170, 255);\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                "	background-color: rgba(85, 170, 255, 100);\n"
                                                "}")
            self.btn_roll_deleter.setIcon(icon6)
            self.btn_roll_deleter.setText(u" Delete")

            self.horizontalLayout_17.addWidget(self.btn_roll_deleter)
            self.verticalLayout_27.addWidget(self.frame_search_delet_bar_6)
            self.horizontalLayout_16.addWidget(self.frame_result_roll)

    # show lower on left active status

    def showLowerOnLeft(self, show_text_label):
        data = Store.read_json_for_left()

        if data[LOWERUSERORDINARY] != []:
            if randomzies_number_for_lower_left == []:

                radndomize_number = random.randint(
                    0, len(data[LOWERUSERORDINARY]) - 1)
                __target = self.decryptForLowerLeft(radndomize_number)

                # Append user Number
                randomzies_number_for_lower_left.append(radndomize_number)

                show_text_label.setFont(self.font_info)

                # Show inter detils
                show_text_label.setText(f"""
					<html>
						<head/>
						<body>
							<p align=\"center\"> <b>STUDENTS TYPE | Recycle Bin </b> </p>
							<br>
							<p>
								<pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
								<pre><spen>Name                 :   {__target[1].title()}</spen></pre>
								<pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
								<pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
								<pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
								<pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
								<pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
								<pre><spen>Level                :   {__target[7]}</spen></pre>
								<pre><spen>E-Mail               :   {__target[8]}</spen></pre>
								<pre><spen>Religion             :   {__target[9].title()}</spen></pre>
								<pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
								<pre><spen>Gender               :   {__target[11]}</spen></pre>
							</p>
						</body>
					</html>
				""")
            else:
                while len(randomzies_number_for_lower_left) < len(data[LOWERUSERORDINARY]):
                    radndomize_number = random.randint(
                        0, len(data[LOWERUSERORDINARY]) - 1)
                    if radndomize_number not in randomzies_number_for_lower_left:
                        __target = self.decryptForLowerLeft(radndomize_number)

                        # Append user Number
                        randomzies_number_for_lower_left.append(
                            radndomize_number)

                        show_text_label.setFont(self.font_info)

                        # Show inter detils
                        show_text_label.setText(f"""
						<html>
							<head/>
							<body>
								<p align=\"center\"> <b>STUDENTS TYPE | Recycle Bin </b> </p>
								<br>
								<p>
									<pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
									<pre><spen>Name                 :   {__target[1].title()}</spen></pre>
									<pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
									<pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
									<pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
									<pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
									<pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
									<pre><spen>Level                :   {__target[7]}</spen></pre>
									<pre><spen>E-Mail               :   {__target[8]}</spen></pre>
									<pre><spen>Religion             :   {__target[9].title()}</spen></pre>
									<pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
									<pre><spen>Gender               :   {__target[11]}</spen></pre>
								</p>
								<br>
							</body>
						</html>
						""")
                        break
                else:

                    show_text_label.setText("""
						<h2 align=\"center\"> <b>Students Not Available in Recycle Bin</b> </h2>
					""")
        else:

            show_text_label.setText("""
				<h2 align=\"center\"> <b>Students Not Available in Recycle Bin</b> </h2>
			""")

    # decrypt for inter user in left
    def decryptForInterLeft(self, randNumber):
        data = Store.read_json_for_left()

        if data[INTERUSER][randNumber]["Level"] != None:
            __level = secure.decrypt(
                data[INTERUSER][randNumber]["Level"][-2], data[INTERUSER][randNumber]["Level"][-1])
        else:
            __level = data[INTERUSER][randNumber]["Level"]

        if data[INTERUSER][randNumber]["Subject"] != None:
            __subject = secure.decrypt(
                data[INTERUSER][randNumber]["Subject"][-2], data[INTERUSER][randNumber]["Subject"][-1])
        else:
            __subject = data[INTERUSER][randNumber]["Subject"]

        if data[INTERUSER][randNumber]["E-Mail"] != None:
            __email = secure.decrypt(
                data[INTERUSER][randNumber]["E-Mail"][-2], data[INTERUSER][randNumber]["E-Mail"][-1])
        else:
            __email = data[INTERUSER][randNumber]["E-Mail"]

        __roll = data[INTERUSER][randNumber]["Roll"]
        __name = secure.decrypt(
            data[INTERUSER][randNumber]["Name"][-2], data[INTERUSER][randNumber]["Name"][-1])
        __address = secure.decrypt(
            data[INTERUSER][randNumber]["Address"][-2], data[INTERUSER][randNumber]["Address"][-1])
        __contact_number = secure.decrypt(
            data[INTERUSER][randNumber]["Contact-Number"][-2], data[INTERUSER][randNumber]["Contact-Number"][-1])
        __gender = secure.decrypt(
            data[INTERUSER][randNumber]["Gender"][-2], data[INTERUSER][randNumber]["Gender"][-1])

        __target = [__roll, __name, __address, __subject,
                    __email, __contact_number, __level, __gender]

        return __target

    # Decrypt for lower user in left
    def decryptForLowerLeft(self, randNumber):
        data = Store.read_json_for_left()
        __roll = data[LOWERUSERORDINARY][randNumber]['Roll']
        __name = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Name'][-2], data[LOWERUSERORDINARY][randNumber]['Name'][-1])
        __address = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Address'][-2], data[LOWERUSERORDINARY][randNumber]['Address'][-1])
        __fatherName = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Father-Name'][-2], data[LOWERUSERORDINARY][randNumber]['Father-Name'][-1])
        __matherName = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Mather-Name'][-2], data[LOWERUSERORDINARY][randNumber]['Mather-Name'][-1])
        __contact_number = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Contact-Number'][-2], data[LOWERUSERORDINARY][randNumber]['Contact-Number'][-1])
        __ragistartion_number = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Registration-Number'][-2], data[LOWERUSERORDINARY][randNumber]['Registration-Number'][-1])
        __level = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Level'][-2], data[LOWERUSERORDINARY][randNumber]['Level'][-1])
        __religion = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Religion'][-2], data[LOWERUSERORDINARY][randNumber]['Religion'][-1])
        __dateOfBirth = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Date-of-Birth'][-2], data[LOWERUSERORDINARY][randNumber]['Date-of-Birth'][-1])
        __gender = secure.decrypt(
            data[LOWERUSERORDINARY][randNumber]['Gender'][-2], data[LOWERUSERORDINARY][randNumber]['Gender'][-1])

        if data[LOWERUSERORDINARY][randNumber]['E-Mail'] != None:
            __email = secure.decrypt(
                data[LOWERUSERORDINARY][randNumber]['E-Mail'][-2], data[LOWERUSERORDINARY][randNumber]['E-Mail'][-1])
        else:
            __email = data[LOWERUSERORDINARY][randNumber]['E-Mail']

        __target = [__roll, __name, __address, __fatherName, __matherName, __contact_number,
                    __ragistartion_number, __level, __email, __religion, __dateOfBirth, __gender]
        return __target

    # Decrypt for Advance lower user in left
    def decryptForAdvanceLowerLeft(self, randNumber, level=None, stream=None):

        if level != None and stream != None:
            data = Store.read_json()

            __roll = data[LOWERUSERADVANCED][level][stream][randNumber]['Roll']
            __name = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Name'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Name'][-1])
            __address = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Address'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Address'][-1])
            __fatherName = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Father-Name'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Father-Name'][-1])
            __matherName = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Mather-Name'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Mather-Name'][-1])
            __contact_number = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Contact-Number'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Contact-Number'][-1])
            __ragistartion_number = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Registration-Number'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Registration-Number'][-1])
            __level = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Level'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Level'][-1])
            __religion = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Religion'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Religion'][-1])
            __dateOfBirth = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Date-of-Birth'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Date-of-Birth'][-1])
            __gender = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Gender'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Gender'][-1])

            __stream = secure.decrypt(
                data[LOWERUSERADVANCED][level][stream][randNumber]['Stream'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['Stream'][-1])

            if data[LOWERUSERADVANCED][level][stream][randNumber]['E-Mail'] != None:
                __email = secure.decrypt(
                    data[LOWERUSERADVANCED][level][stream][randNumber]['E-Mail'][-2], data[LOWERUSERADVANCED][level][stream][randNumber]['E-Mail'][-1])
            else:
                __email = data[LOWERUSERADVANCED][level][stream][randNumber]['E-Mail']
        else:
            data = Store.read_json_for_left()
            __roll = data[LOWERUSERADVANCED][randNumber]['Roll']
            __name = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Name'][-2], data[LOWERUSERADVANCED][randNumber]['Name'][-1])
            __address = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Address'][-2], data[LOWERUSERADVANCED][randNumber]['Address'][-1])
            __fatherName = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Father-Name'][-2], data[LOWERUSERADVANCED][randNumber]['Father-Name'][-1])
            __matherName = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Mather-Name'][-2], data[LOWERUSERADVANCED][randNumber]['Mather-Name'][-1])
            __contact_number = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Contact-Number'][-2], data[LOWERUSERADVANCED][randNumber]['Contact-Number'][-1])
            __ragistartion_number = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Registration-Number'][-2], data[LOWERUSERADVANCED][randNumber]['Registration-Number'][-1])
            __level = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Level'][-2], data[LOWERUSERADVANCED][randNumber]['Level'][-1])
            __religion = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Religion'][-2], data[LOWERUSERADVANCED][randNumber]['Religion'][-1])
            __dateOfBirth = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Date-of-Birth'][-2], data[LOWERUSERADVANCED][randNumber]['Date-of-Birth'][-1])
            __gender = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Gender'][-2], data[LOWERUSERADVANCED][randNumber]['Gender'][-1])

            __stream = secure.decrypt(
                data[LOWERUSERADVANCED][randNumber]['Stream'][-2], data[LOWERUSERADVANCED][randNumber]['Stream'][-1])

            if data[LOWERUSERADVANCED][randNumber]['E-Mail'] != None:
                __email = secure.decrypt(
                    data[LOWERUSERADVANCED][randNumber]['E-Mail'][-2], data[LOWERUSERADVANCED][randNumber]['E-Mail'][-1])
            else:
                __email = data[LOWERUSERADVANCED][randNumber]['E-Mail']

        __target = [__roll, __name, __address, __fatherName, __matherName, __contact_number,
                    __ragistartion_number, __level, __email, __religion, __dateOfBirth, __gender, __stream]
        return __target

    # Open access window for Name Changes

    def access_name(self):
        __newName = self.ui.lineEdit_username_change_input.text()
        if __newName != '':
            self.ui.label_username_title.setText("""
				<html>
				<head/>
				<body>
					<p style = \"font-size:10pt; font-weight:600;\"> Change Name </p>
				</body>
				</html>
			""")
            access = Access()
            access.ui.btn_verify.clicked.connect(lambda: self.verify_password(
                access, self.ui.label_username_title, self.ui.label_show_current_username, "Current Name: ", self.ui.lineEdit_username_change_input, 'Name', 'Change Name'))
        else:
            self.ui.label_username_title.setText("""
				<html>
				<head/>
				<body>
					<p style=\"color: red; font-size:10pt; font-weight:600;\"> Something Empty </p>
				</body>
				</html>
			""")

    # Open access window for E - Mail Cheanges
    def access_email(self):
        __newEmail = self.ui.lineEdit_change_email_input.text()
        if __newEmail != '':
            self.ui.label_change_email_title.setText("""
				<html>
				<head/>
				<body>
					<p style = \"font-size:10pt; font-weight:600;\"> Change E-Mail </p>
				</body>
				</html>
			""")
            access = Access()
            access.ui.btn_verify.clicked.connect(lambda: self.verify_password(
                access, self.ui.label_change_email_title, self.ui.label_current_email, "Current E-Mail: ", self.ui.lineEdit_change_email_input, 'E-Mail', 'Change E-Mail'))
        else:
            self.ui.label_change_email_title.setText("""
				<html>
				<head/>
				<body>
					<p style=\"color: red; font-size:10pt; font-weight:600;\"> Something Empty </p>
				</body>
				</html>
			""")
    # Open access window for Contact Number

    def access_contactNumber(self):
        __newContactNumber = self.ui.lineEdit_contact_number_input.text()
        if __newContactNumber != '':
            # remove errors with users
            self.ui.label_change_contact_number_title.setText("""
				<html>
				<head/>
				<body>
					<p style = \"font-size:10pt; font-weight:600;\"> Change Contact Number </p>
				</body>
				</html>
			""")
            access = Access()
            access.ui.btn_verify.clicked.connect(lambda: self.verify_password(access, self.ui.label_change_contact_number_title, self.ui.label_show_current_contact_number,
                                                 "Current Contact-Number: ", self.ui.lineEdit_contact_number_input, 'Contact-Number', 'Change Contact-Number'))
        else:
            # show errors with users
            self.ui.label_change_contact_number_title.setText("""
				<html>
				<head/>
				<body>
					<p style=\"color: red; font-size:10pt; font-weight:600;\"> Something Empty </p>
				</body>
				</html>
			""")

    # Open Access Window for Password
    def access_password(self):
        __newPassword = self.ui.lineEdit_passord_input.text()
        __conPassword = self.ui.lineEdit_repassword_input.text()
        if __newPassword == '' and __conPassword == '':
            # show errors with users
            self.ui.label_change_password_title.setText("""
				<html>
				<head/>
				<body>
				<p style=\"color: red; font-size:10pt; font-weight:600;\"> Something Empty </p>
				</body>
				</html>
			""")
        # Password lenght
        elif len(self.ui.lineEdit_passord_input.text()) < 6:
            self.ui.label_change_password_title.setText("""
				<html>
				<head/>
				<body>
					<p style=\"color: red; font-size:10pt; font-weight:600;\"> Password Lenght Is Smole </p>
				</body>
				</html>
			""")
        # Incorrect Password
        elif self.ui.lineEdit_passord_input.text() != self.ui.lineEdit_repassword_input.text():
            self.ui.label_change_password_title.setText("""
			<html>
				<head/>
				<body>
					<p style=\"color: red; font-size:10pt; font-weight:600;\"> Password is Macth </p>
				</body>
			</html>
			""")
        else:
            # remove errors with users
            self.ui.label_change_password_title.setText("""
				<html>
				<head/>
				<body>
				<p style = \"font-size:10pt; font-weight:600;\">Change Password</p>
				</body>
				</html>
			""")
            access = Access()
            access.ui.btn_verify.clicked.connect(
                lambda: self.setPassword(access))

    # Verify Password and Set New Password
    def setPassword(self, obj):
        __userinputpassword = obj.ui.lineEdit_current_password.text()
        data = Store.read_super_user()
        __password, __passwordKey = data[SUPERUSER][-1]['Password'][-2], data[SUPERUSER][-1]['Password'][-1]
        __password = secure.decrypt(__password, __passwordKey)

        if __userinputpassword != '':
            if __userinputpassword == __password:
                self.ui.label_change_password_title.setText("""
				<html>
				<head/>
				<body>
					<p style=\" font-size:10pt; font-weight:600;\">Change Password</p>
				</body>
				</html>
				""")
                __newPassword, __newPasswordKey = secure.encrypt(
                    self.ui.lineEdit_passord_input.text())
                data[SUPERUSER][-1]['Password'][-2], data[SUPERUSER][-1]['Password'][-1] = __newPassword, __newPasswordKey
                self.ui.lineEdit_passord_input.clear()
                self.ui.lineEdit_repassword_input.clear()
                Store.write_json(data)
                obj.close()

            # Verify password getter
            else:
                obj.ui.label_change_password_title.setText("""
					<html>
					<head/>
						<body>
							<p style=\"color: red; font-size:10pt; font-weight:600;\"> Incorrect Password </p>
						</body>
					</html>
				""")
        else:
            obj.ui.label_change_password_title.setText("""
			<html>
				<head/>
				<body>
					<p style=\"color: red; font-size:10pt; font-weight:600;\"> Incorrect Password </p>
				</body>
			</html>
			""")

    # Verify Password in to change data key values

    def verify_password(self, class_obj, changes_show_label, show_info_label, verify_show_text, getChangesInput, accessKey, show_title_name):
        __userinputpassword = class_obj.ui.lineEdit_current_password.text()
        data = Store.read_super_user()

        # Verfiy Password
        __password, __passwordKey = data[SUPERUSER][-1]['Password'][-2], data[SUPERUSER][-1]['Password'][-1]
        __password = secure.decrypt(__password, __passwordKey)
        if __userinputpassword != '':
            if __userinputpassword == __password:
                __newContent = getChangesInput.text()

                changes_show_label.setText(f"""
					<html>
					<head/>
					<body>
						<p style=\" font-size:10pt; font-weight:600;\">{show_title_name}</p>
					</body>
					</html>
				""")

                # Set New Content On Data
                show_info_label.setText(f"""
                <p><spen style=\" font-size:12pt; font-weight:600;\">{verify_show_text + __newContent}</spen></p>
                """)
                __newContent, __newContentKey = secure.encrypt(__newContent)
                data[SUPERUSER][-1][accessKey][-2], data[SUPERUSER][-1][accessKey][-1] = __newContent, __newContentKey
                Store.write_super_user(data)
                getChangesInput.clear()
                class_obj.close()

            else:
                # show errors with user
                class_obj.ui.label_user_info.setText("""
					<html>
					<head/>
						<body>
							<p style=\"color: red; font-size:10pt; font-weight:600;\"> Incorrect Password </p>
						</body>
					</html>
				""")
        else:
            # show errors with user
            class_obj.ui.label_user_info.setText("""
					<html>
					<head/>
						<body>
							<p style=\"color: red; font-size:10pt; font-weight:600;\"> Something Empty </p>
						</body>
					</html>
			""")

    # Call Inter Window
    def callInterWindow(self):
        UIFunctions.addInter_page(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_inter)

    # STORE INTER DATA INTO JSON
    # Store Thread

    def store_interData_thread(self):
        storeThread = Thread(target=self.store_interData)
        storeThread.start()
        storeThread.join()

        # rerun the programe
        self.connect_inter()

    # Store Inter Data

    def store_interData(self):

        # Get Inter User Data
        __name = self.ui.lineEdit_name.text()
        __address = self.ui.lineEdit_address.text()
        __supject = self.ui.lineEdit_subject.text()
        __email = self.ui.lineEdit_email.text()
        __contact_number = self.ui.lineEdit_contect.text()
        __level = self.ui.lineEdit_level.text()

        # Check Email
        __email = email_check(__email)

        # Check Phone Number
        __contact_number = phone_number_checker(__contact_number)

        # Check Subject
        if __supject == '':
            __supject = None
        if __level == '':
            __level = None

        # check rquist
        if __name != '' and __address != '' and __contact_number != False and self.gender != 'none':

            __name, __nameKey = secure.encrypt(__name)
            __address, __addressKey = secure.encrypt(__address)
            __contact_number, __contact_numberKey = secure.encrypt(
                __contact_number)
            gender, genderKey = secure.encrypt(self.gender)
            __rollNumber = self.rollNumberForInter()

            data_obj = {}

            if __supject != None and __level != None and __email != None:
                __supject, __supjectKey = secure.encrypt(__supject)
                __level, __levelKey = secure.encrypt(__level)
                __email, __emailKey = secure.encrypt(__email)

                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Contact-Number": [__contact_number, __contact_numberKey],
                    "Subject": [__supject, __supjectKey],
                    "Gender": [gender, genderKey],
                    "Level": [__level, __levelKey],
                    "E-Mail": [__email, __emailKey]
                }

            elif __supject != None and __level == None and __email == None:
                __supject, __supjectKey = secure.encrypt(__supject)
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Contact-Number": [__contact_number, __contact_numberKey],
                    "Subject": [__supject, __supjectKey],
                    "Gender": [gender, genderKey],
                    "Level": None,
                    "E-Mail": None
                }

            elif __supject == None and __level != None and __email == None:
                __level, __levelKey = secure.encrypt(__level)
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Contact-Number": [__contact_number, __contact_numberKey],
                    "Subject": None,
                    "Gender": [gender, genderKey],
                    "Level": [__level, __levelKey],
                    "E-Mail": None
                }

            elif __supject == None and __level == None and __email != None:
                __email, __emailKey = secure.encrypt(__email)
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Contact-Number": [__contact_number, __contact_numberKey],
                    "Subject": None,
                    "Gender": [gender, genderKey],
                    "Level": None,
                    "E-Mail": [__email, __emailKey]
                }

            elif __supject != None and __level != None and __email == None:
                __supject, __supjectKey = secure.encrypt(__supject)
                __level, __levelKey = secure.encrypt(__level)
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Contact-Number": [__contact_number, __contact_numberKey],
                    "Subject": [__supject, __supjectKey],
                    "Gender": [gender, genderKey],
                    "Level": [__level, __levelKey],
                    "E-Mail": None
                }

            elif __supject == None and __level != None and __email != None:
                __level, __levelKey = secure.encrypt(__level)
                __email, __emailKey = secure.encrypt(__email)

                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Contact-Number": [__contact_number, __contact_numberKey],
                    "Subject": None,
                    "Gender": [gender, genderKey],
                    "Level": [__level, __levelKey],
                    "E-Mail": [__email, __emailKey]
                }

            elif __supject != None and __level == None and __email != None:
                __supject, __supjectKey = secure.encrypt(__supject)
                __email, __emailKey = secure.encrypt(__email)

                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Contact-Number": [__contact_number, __contact_numberKey],
                    "Subject": [__supject, __supjectKey],
                    "Gender": [gender, genderKey],
                    "Level": None,
                    "E-Mail": [__email, __emailKey]
                }

            else:
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Contact-Number": [__contact_number, __contact_numberKey],
                    "Subject": None,
                    "Gender": [gender, genderKey],
                    "Level": None,
                    "E-Mail": None
                }

            self.ui.label_show_roll_number.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p><span style=" font-size:12pt;">Roll Number: {__rollNumber}</span></p>
                    </body>
                </html>
            """)
            store_thread = Thread(target=Store.update_json,
                                  args=[data_obj, INTERUSER])
            store_thread.start()
            store_thread.join()

            self.ui.lineEdit_name.clear()
            self.ui.lineEdit_address.clear()
            self.ui.lineEdit_contect.clear()
            self.ui.lineEdit_email.clear()
            self.ui.lineEdit_subject.clear()
            self.ui.lineEdit_level.clear()

        else:
            self.ui.label_show_roll_number.setText("""
                <html>
                    <head/>
                    <body>
                        <p>(<span style=\"color: red;font-size:12pt;\">Something Missing</span>)</p>
                    </body>
                </html>
            """)

    # Get Roll Number For Inter
    def rollNumberForInter(self):
        data = Store.read_json()
        interUserList = data[INTERUSER]

        if interUserList == []:
            rollNumberForInterUser = f"INTER{self.interUserCount:04}I"
            self.interUserCount += 1
        else:
            lastRollNumberForInterUser = interUserList[-1]["Roll"]
            lastRollNumberForInterUser = lastRollNumberForInterUser.split(
                "INTER")[-1].split("I")[0]
            lastRollNumberForInterUser = int(lastRollNumberForInterUser)
            lastRollNumberForInterUser += 1
            rollNumberForInterUser = f"INTER{lastRollNumberForInterUser:04}I"

        return rollNumberForInterUser

    # ADD GANDER STRING
    def female_set(self):
        self.gender = "Female"

    def male_set(self):
        self.gender = "Male"

    def other_set(self):
        self.gender = "Other"

    # Call Lower Window
    def callLowerWindow(self):
        UIFunctions.addLower_page(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_students)

    # Roll Search Thread
    def search_thread(self):
        storeThread = Thread(target=self.store_lower_data)
        storeThread.start()
        storeThread.join()
        self.connect_lower_odrinary()
        self.data_frame()

    def storeThread(self):
        storeThread = Thread(target=self.store_lower_adv_data)
        storeThread.start()
        storeThread.join()
        self.data_frame()
        self.connect_lower_advanced()

    def storeThread_primary(self):
        store_thread = Thread(target=self.store_primary_lower_data)
        store_thread.start()
        store_thread.join()
        self.connect_lower_primary()
        self.data_frame()

    # Store Lower Primary Data

    def store_primary_lower_data(self):
        __name = self.ui.lineEdit_name_primary.text()
        __address = self.ui.lineEdit_address_primary.text()
        __fatherName = self.ui.lineEdit_father_primary.text()
        __matherName = self.ui.lineEdit_mather_primary.text()
        __contactNumber = self.ui.lineEdit_contect_primary.text()
        __ragistartionNumber = self.ui.lineEdit_registration_primary.text()
        __level = self.ui.comboBox_stream_primary.currentText()
        __email = self.ui.lineEdit_email_primary.text()
        __religion = self.ui.lineEdit_religion_primary.text()

        # Get Data Of Birth
        __dateOfBirth = self.ui.dateEdit_date_of_birth_primary.date().toString()

        data = Store.read_json()
        lavelClassNumberList = [
            className for className in data[LOWERUSERPRIMARY]]

        __contactNumber = phone_number_checker(__contactNumber)

        if __name != '' and __address != '' and __fatherName != '' and __matherName != '' and __contactNumber != False and __ragistartionNumber != '' and __religion != '' and self.gender != 'none':
            __email = email_check(__email)
            level = self.checkLevelsForPrimary(__level)

            __rollNumber = self.rollNumberForLowerPrimary(__level)

            # Encrypt data
            __name, __nameKey = secure.encrypt(__name)
            __address, __addressKey = secure.encrypt(__address)
            __fatherName, __fatherNameKey = secure.encrypt(__fatherName)
            __matherName, __matherNameKey = secure.encrypt(__matherName)
            __contactNumber, __contactNumberKey = secure.encrypt(
                __contactNumber)
            __ragistartionNumber, __ragistartionNumberKey = secure.encrypt(
                __ragistartionNumber)
            __level, __levelKey = secure.encrypt(__level)
            __religion, __religionKey = secure.encrypt(__religion)
            __dateOfBirth, __dateOfBirthKey = secure.encrypt(__dateOfBirth)
            __gender, __genderKey = secure.encrypt(self.gender)

            if __email != None:
                __email, __emailKey = secure.encrypt(__email)
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Father-Name": [__fatherName, __fatherNameKey],
                    "Mather-Name": [__matherName, __matherNameKey],
                    "Contact-Number": [__contactNumber, __contactNumberKey],
                    "Registration-Number": [__ragistartionNumber, __ragistartionNumberKey],
                    "Date-of-Birth": [__dateOfBirth, __dateOfBirthKey],
                    "Religion": [__religion, __religionKey],
                    "E-Mail": [__email, __emailKey],
                    "Level": [__level, __levelKey],
                    "Gender": [__gender, __genderKey],
                }

            else:
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Father-Name": [__fatherName, __fatherNameKey],
                    "Mather-Name": [__matherName, __matherNameKey],
                    "Contact-Number": [__contactNumber, __contactNumberKey],
                    "Registration-Number": [__ragistartionNumber, __ragistartionNumberKey],
                    "Date-of-Birth": [__dateOfBirth, __dateOfBirthKey],
                    "Religion": [__religion, __religionKey],
                    "E-Mail": None,
                    "Level": [__level, __levelKey],
                    "Gender": [__gender, __genderKey],
                }

            self.ui.label_show_roll_primary.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p><span style=" font-size:12pt;">Roll Number: {__rollNumber}</span></p>
                    </body>
                </html>
            """)

            temp = data[LOWERUSERPRIMARY][level]
            temp.append(data_obj)
            store = Thread(target=Store.write_json, args=[data, ])
            store.start()
            store.join()

            self.ui.lineEdit_name_primary.clear()
            self.ui.lineEdit_address_primary.clear()
            self.ui.lineEdit_father_primary.clear()
            self.ui.lineEdit_mather_primary.clear()
            self.ui.lineEdit_contect_primary.clear()
            self.ui.lineEdit_registration_primary.clear()
            self.ui.lineEdit_email_primary.clear()
            self.ui.lineEdit_religion_primary.clear()

        else:
            self.ui.label_show_roll_primary.setText("""
                <html>
                    <head/>
                    <body>
                        <p>(<span style=\"color: red;font-size:12pt;\"> Something Missed </span>)</p>
                    </body>
                </html>
            """)

    # Store Lower Advance Data
    def store_lower_adv_data(self):
        __name = self.ui.lineEdit_name_ad.text()
        __address = self.ui.lineEdit_address_ad.text()
        __fatherName = self.ui.lineEdit_father_ad.text()
        __matherName = self.ui.lineEdit_mather_ad.text()
        __contactNumber = self.ui.lineEdit_contect_ad.text()
        __ragistartionNumber = self.ui.lineEdit_registration_ad.text()
        __level = self.ui.lineEdit_level_ad.currentText()
        __email = self.ui.lineEdit_email_ad.text()
        __religion = self.ui.lineEdit_religion_ad.text()

        # Get Data Of Birth
        __dateOfBirth = self.ui.dateEdit_date_of_birth_ad.date().toString()

        data = Store.read_json()
        lavelClassNumberList = [
            className for className in data[LOWERUSERADVANCED]]
        lavelClassStreamList = [
            className for className in data[LOWERUSERADVANCED][lavelClassNumberList[0]]]

        __contactNumber = phone_number_checker(__contactNumber)

        if __name != '' and __address != '' and __fatherName != '' and __matherName != '' and __contactNumber != False and __ragistartionNumber != '' and __religion != '' and self.gender != 'none':
            __email = email_check(__email)
            level = self.checkLevelAd(__level)

            __rollNumber = self.rollNumberForLowerAdvance(
                __level, self.ui.comboBox_stream.currentIndex())

            # Encrypt data
            __name, __nameKey = secure.encrypt(__name)
            __address, __addressKey = secure.encrypt(__address)
            __fatherName, __fatherNameKey = secure.encrypt(__fatherName)
            __matherName, __matherNameKey = secure.encrypt(__matherName)
            __contactNumber, __contactNumberKey = secure.encrypt(
                __contactNumber)
            __ragistartionNumber, __ragistartionNumberKey = secure.encrypt(
                __ragistartionNumber)
            __level, __levelKey = secure.encrypt(__level)
            __religion, __religionKey = secure.encrypt(__religion)
            __dateOfBirth, __dateOfBirthKey = secure.encrypt(__dateOfBirth)
            __gender, __genderKey = secure.encrypt(self.gender)
            __stream, __streamKey = secure.encrypt(
                lavelClassStreamList[self.ui.comboBox_stream.currentIndex()])

            if __email != None:
                __email, __emailKey = secure.encrypt(__email)
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Father-Name": [__fatherName, __fatherNameKey],
                    "Mather-Name": [__matherName, __matherNameKey],
                    "Contact-Number": [__contactNumber, __contactNumberKey],
                    "Registration-Number": [__ragistartionNumber, __ragistartionNumberKey],
                    "Date-of-Birth": [__dateOfBirth, __dateOfBirthKey],
                    "Religion": [__religion, __religionKey],
                    "E-Mail": [__email, __emailKey],
                    "Level": [__level, __levelKey],
                    "Gender": [__gender, __genderKey],
                    "Stream": [__stream, __streamKey]
                }

            else:
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Father-Name": [__fatherName, __fatherNameKey],
                    "Mather-Name": [__matherName, __matherNameKey],
                    "Contact-Number": [__contactNumber, __contactNumberKey],
                    "Registration-Number": [__ragistartionNumber, __ragistartionNumberKey],
                    "Date-of-Birth": [__dateOfBirth, __dateOfBirthKey],
                    "Religion": [__religion, __religionKey],
                    "E-Mail": None,
                    "Level": [__level, __levelKey],
                    "Gender": [__gender, __genderKey],
                    "Stream": [__stream, __streamKey]
                }

            self.ui.label_show_roll_ad.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p><span style=" font-size:12pt;">Roll Number: {__rollNumber}</span></p>
                    </body>
                </html>
            """)

            temp = data[LOWERUSERADVANCED][level][lavelClassStreamList[self.ui.comboBox_stream.currentIndex()]]
            temp.append(data_obj)
            store = Thread(target=Store.write_json, args=[data, ])
            store.start()
            store.join()

            self.ui.lineEdit_name_ad.clear()
            self.ui.lineEdit_address_ad.clear()
            self.ui.lineEdit_father_ad.clear()
            self.ui.lineEdit_mather_ad.clear()
            self.ui.lineEdit_contect_ad.clear()
            self.ui.lineEdit_registration_ad.clear()
            self.ui.lineEdit_email_ad.clear()
            self.ui.lineEdit_religion_ad.clear()

        else:
            self.ui.label_show_roll_ad.setText("""
                <html>
                    <head/>
                    <body>
                        <p>(<span style=\"color: red;font-size:12pt;\"> Something Missed </span>)</p>
                    </body>
                </html>
            """)

    # Store Lower Ordnary Data

    def store_lower_data(self):
        __name = self.ui.lineEdit_name_lower.text()
        __address = self.ui.lineEdit_address_lower.text()
        __fatherName = self.ui.lineEdit_father.text()
        __matherName = self.ui.lineEdit_mather.text()
        __contactNumber = self.ui.lineEdit_contect_lower.text()
        __ragistartionNumber = self.ui.lineEdit_ragis_number.text()
        __level = self.ui.lineEdit_level_lower.currentText()
        __email = self.ui.lineEdit_email_lower.text()
        __religion = self.ui.lineEdit_religion.text()

        # Get Date Of Birth
        __dateOfBirth = self.ui.dateEdit_data_of_birth.date().toString()

        __contactNumber = phone_number_checker(__contactNumber)

        if __name != '' and __address != '' and __fatherName != '' and __matherName != '' and __contactNumber != False and __ragistartionNumber != '' and __religion != '' and self.gender != 'none':
            __email = email_check(__email)
            __rollNumber = self.rollNumberForLower(__level)
            level = self.checkLevel(__level)

            # Encrypt data
            __name, __nameKey = secure.encrypt(__name)
            __address, __addressKey = secure.encrypt(__address)
            __fatherName, __fatherNameKey = secure.encrypt(__fatherName)
            __matherName, __matherNameKey = secure.encrypt(__matherName)
            __contactNumber, __contactNumberKey = secure.encrypt(
                __contactNumber)
            __ragistartionNumber, __ragistartionNumberKey = secure.encrypt(
                __ragistartionNumber)
            __level, __levelKey = secure.encrypt(__level)
            __religion, __religionKey = secure.encrypt(__religion)
            __dateOfBirth, __dateOfBirthKey = secure.encrypt(__dateOfBirth)
            __gender, __genderKey = secure.encrypt(self.gender)

            if __email != None:
                __email, __emailKey = secure.encrypt(__email)
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Father-Name": [__fatherName, __fatherNameKey],
                    "Mather-Name": [__matherName, __matherNameKey],
                    "Contact-Number": [__contactNumber, __contactNumberKey],
                    "Registration-Number": [__ragistartionNumber, __ragistartionNumberKey],
                    "Date-of-Birth": [__dateOfBirth, __dateOfBirthKey],
                    "Religion": [__religion, __religionKey],
                    "E-Mail": [__email, __emailKey],
                    "Level": [__level, __levelKey],
                    "Gender": [__gender, __genderKey]
                }

            else:
                data_obj = {
                    "Roll": __rollNumber,
                    "Name": [__name, __nameKey],
                    "Address": [__address, __addressKey],
                    "Father-Name": [__fatherName, __fatherNameKey],
                    "Mather-Name": [__matherName, __matherNameKey],
                    "Contact-Number": [__contactNumber, __contactNumberKey],
                    "Registration-Number": [__ragistartionNumber, __ragistartionNumberKey],
                    "Date-of-Birth": [__dateOfBirth, __dateOfBirthKey],
                    "Religion": [__religion, __religionKey],
                    "E-Mail": None,
                    "Level": [__level, __levelKey],
                    "Gender": [__gender, __genderKey]
                }

            self.ui.label_show_roll_number_lower.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p><span style=" font-size:12pt;">Roll Number: {__rollNumber}</span></p>
                    </body>
                </html>
            """)
            data = Store.read_json()
            data[LOWERUSERORDINARY][self.ui.lineEdit_level_lower.currentText()
                                    ].append(data_obj)
            store_thread = Thread(target=Store.write_json, args=[
                data, ])
            store_thread.start()
            store_thread.join()

            self.ui.lineEdit_name_lower.clear()
            self.ui.lineEdit_address_lower.clear()
            self.ui.lineEdit_father.clear()
            self.ui.lineEdit_mather.clear()
            self.ui.lineEdit_contect_lower.clear()
            self.ui.lineEdit_ragis_number.clear()
            self.ui.lineEdit_email_lower.clear()
            self.ui.lineEdit_religion.clear()

        else:
            self.ui.label_show_roll_number_lower.setText("""
                <html>
                    <head/>
                    <body>
                        <p>(<span style=\"color: red;font-size:12pt;\"> Something Missed </span>)</p>
                    </body>
                </html>
            """)

    def checkLevel(self, value):
        getLevel = "none"
        data = Store.read_json()
        listLevel = [levels for levels in data[LOWERUSERORDINARY]]
        for level in listLevel:
            if level == value:
                getLevel = level
        return getLevel

    def checkLevelAd(self, value):
        getLevel = "none"
        data = Store.read_json()
        listLevel = [level for level in data[LOWERUSERADVANCED]]
        for level in listLevel:
            if level == value:
                getLevel = level
        return getLevel

    def checkLevelsForPrimary(self, value):
        getLevel = "none"
        data = Store.read_json()
        listLevel = [level for level in data[LOWERUSERPRIMARY]]
        for level in listLevel:
            if level == value:
                getLevel = value
        return getLevel

    def rollNumberForLowerPrimary(self, levelClass):
        data = Store.read_json()
        levelClassNumberList = [
            className for className in data[LOWERUSERPRIMARY]]
        returnValue = int(levelClass.split("-")[-1])

        rollNumberForLowerUser = None
        if levelClass != "none":
            if data[LOWERUSERPRIMARY][levelClass] == []:
                if int(returnValue) == 1:
                    lowerUserCount = 0
                    rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L1"
                    lowerUserCount += 1
                elif int(returnValue) == 2:
                    lowerUserCount = 0
                    rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L2"
                    lowerUserCount += 1
                elif int(returnValue) == 3:
                    lowerUserCount = 0
                    rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L3"
                    lowerUserCount += 1
                elif int(returnValue) == 4:
                    lowerUserCount = 0
                    rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L4"
                    lowerUserCount += 1
                else:
                    lowerUserCount = 0
                    rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L5"
                    lowerUserCount += 1
            else:
                lastRollNumberForPrimaryLower = data[LOWERUSERPRIMARY][levelClass][-1]["Roll"]
                lastRollNumberForPrimaryLower = lastRollNumberForPrimaryLower.split(
                    "LOWER")[-1].split("L")[0]
                lastRollNumberForPrimaryLower = int(
                    lastRollNumberForPrimaryLower)
                if int(returnValue) == 1:
                    lastRollNumberForPrimaryLower += 1
                    rollNumberForLowerUser = f"LOWER{lastRollNumberForPrimaryLower:04}L1"

                elif int(returnValue) == 2:
                    lastRollNumberForPrimaryLower += 1
                    rollNumberForLowerUser = f"LOWER{lastRollNumberForPrimaryLower:04}L2"

                elif int(returnValue) == 3:
                    lastRollNumberForPrimaryLower += 1
                    rollNumberForLowerUser = f"LOWER{lastRollNumberForPrimaryLower:04}L3"

                elif int(returnValue) == 4:
                    lastRollNumberForPrimaryLower += 1
                    rollNumberForLowerUser = f"LOWER{lastRollNumberForPrimaryLower:04}L4"

                else:
                    lastRollNumberForPrimaryLower += 1
                    rollNumberForLowerUser = f"LOWER{lastRollNumberForPrimaryLower:04}L5"
        return rollNumberForLowerUser

    def rollNumberForLowerAdvance(self, levelClass, index):
        data = Store.read_json()
        lavelClassNumberList = [
            className for className in data[LOWERUSERADVANCED]]
        lavelClassStreamList = [
            className for className in data[LOWERUSERADVANCED][lavelClassNumberList[0]]]

        rollNumberForLowerUser = None

        returnValue = levelClass
        if returnValue != "none":
            if data[LOWERUSERADVANCED][returnValue][lavelClassStreamList[index]] == []:
                if int(returnValue.split("-")[-1]) == 12:
                    if "Mathematics" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L12|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    elif "Science" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L12|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    elif "Engineering-Technology" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L12|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    elif "Bio-Technology" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L12|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    elif "Commerce" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L12|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    else:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L12|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                else:
                    if "Mathematics" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L13|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    elif "Science" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L13|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    elif "Engineering-Technology" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L13|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    elif "Bio-Technology" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L13|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    elif "Commerce" == lavelClassStreamList[index]:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L13|{lavelClassStreamList[index]}"
                        lowerUserCount += 1
                    else:
                        lowerUserCount = 0
                        rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L13|{lavelClassStreamList[index]}"
                        lowerUserCount += 1

            else:
                lastRollNumberForAdvanceLower = data[LOWERUSERADVANCED][
                    returnValue][lavelClassStreamList[index]][-1]["Roll"]
                stream_value = lastRollNumberForAdvanceLower.split("|")[-1]
                lastRollNumberForAdvanceLower = lastRollNumberForAdvanceLower.split(
                    "LOWER")[-1].split("L")[0]
                lastRollNumberForAdvanceLower = int(
                    lastRollNumberForAdvanceLower)

                if int(returnValue.split("-")[-1]) == 12:
                    if "Mathematics" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L12|{lavelClassStreamList[index]}"
                    elif "Science" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L12|{lavelClassStreamList[index]}"

                    elif "Engineering-Technology" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L12|{lavelClassStreamList[index]}"

                    elif "Bio-Technology" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L12|{lavelClassStreamList[index]}"

                    elif "Commerce" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L12|{lavelClassStreamList[index]}"

                    else:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L12|{lavelClassStreamList[index]}"

                else:
                    if "Mathematics" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L13|{lavelClassStreamList[index]}"

                    elif "Science" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L13|{lavelClassStreamList[index]}"

                    elif "Engineering-Technology" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L13|{lavelClassStreamList[index]}"

                    elif "Bio-Technology" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L13|{lavelClassStreamList[index]}"

                    elif "Commerce" == lavelClassStreamList[index]:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L13|{lavelClassStreamList[index]}"

                    else:
                        lastRollNumberForAdvanceLower += 1
                        rollNumberForLowerUser = f"LOWER{lastRollNumberForAdvanceLower:04}L13|{lavelClassStreamList[index]}"
        return rollNumberForLowerUser

    def rollNumberForLower(self, levelClass):
        data = Store.read_json()

        leveNum = int(levelClass.split("-")[-1])

        # Get Class Name Key
        levelClassList = data[LOWERUSERORDINARY][levelClass]
        if levelClassList == []:
            levelClass = levelClass

            if leveNum == 6:
                lowerUserCount = 0
                rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L6"
                lowerUserCount += 1

            elif leveNum == 7:
                lowerUserCount = 0
                rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L7"
                lowerUserCount += 1

            elif leveNum == 8:
                lowerUserCount = 0
                rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L8"
                lowerUserCount += 1

            elif leveNum == 9:
                lowerUserCount = 0
                rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L9"
                lowerUserCount += 1

            elif leveNum == 10:
                lowerUserCount = 0
                rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L10"
                lowerUserCount += 1

            else:
                lowerUserCount = 0
                rollNumberForLowerUser = f"LOWER{lowerUserCount:04}L11"
                lowerUserCount += 1
        else:
            # Get last Roll Number
            lastRollNumberForLowerUser = levelClassList[-1]["Roll"]
            lastRollNumberForLowerUser = lastRollNumberForLowerUser.split(
                "LOWER")[-1].split("L")[0]

            if leveNum == 6:
                lastRollNumberForLowerUser = int(
                    lastRollNumberForLowerUser)
                lastRollNumberForLowerUser += 1
                rollNumberForLowerUser = f"LOWER{lastRollNumberForLowerUser:04}L6"

            elif leveNum == 7:
                lastRollNumberForLowerUser = int(
                    lastRollNumberForLowerUser)
                lastRollNumberForLowerUser += 1
                rollNumberForLowerUser = f"LOWER{lastRollNumberForLowerUser:04}L7"

            elif leveNum == 8:
                lastRollNumberForLowerUser = int(
                    lastRollNumberForLowerUser)
                lastRollNumberForLowerUser += 1
                rollNumberForLowerUser = f"LOWER{lastRollNumberForLowerUser:04}L8"

            elif leveNum == 9:
                lastRollNumberForLowerUser = int(
                    lastRollNumberForLowerUser)
                lastRollNumberForLowerUser += 1
                rollNumberForLowerUser = f"LOWER{lastRollNumberForLowerUser:04}L9"

            elif leveNum == 10:
                lastRollNumberForLowerUser = int(
                    lastRollNumberForLowerUser)
                lastRollNumberForLowerUser += 1
                rollNumberForLowerUser = f"LOWER{lastRollNumberForLowerUser:04}L10"
            else:
                lastRollNumberForLowerUser = int(
                    lastRollNumberForLowerUser)
                lastRollNumberForLowerUser += 1
                rollNumberForLowerUser = f"LOWER{lastRollNumberForLowerUser:04}L11"

        return rollNumberForLowerUser

    # Call Backup Window
    def callBackupWindow(self):
        backup = Backup()
        Thread(target=backup.show).start()

    # Able Lower List

    def able_lower_lst(self, lst, userType, stream=False):

        data = Store.read_json()
        if stream != True:
            for name in data[userType]:
                if data[userType][name] != []:
                    lst.append(name)
        else:
            print("abel")
            for name in data[userType]:
                for stre in data[userType][name]:
                    if data[userType][name][stre] != []:
                        lst.append((name, stre))

    # Show Primary Lower And Random Getter
    def random_getter_primary(self):
        ABLE_PRIMARY_LOWER.clear()
        data = Store.read_json()

        able_thread = Thread(target=self.able_lower_lst, args=[
                             ABLE_PRIMARY_LOWER, LOWERUSERPRIMARY])
        able_thread.start()
        able_thread.join()

        if ABLE_PRIMARY_LOWER != []:
            random_level = random.choice(ABLE_PRIMARY_LOWER)
            random_index = random.randrange(
                len(data[LOWERUSERPRIMARY][random_level]))

            if RANDOM_LOWER_PRIMARY == []:
                RANDOM_LOWER_PRIMARY.append((random_level, random_index))
            else:
                if (random_level, random_index) not in RANDOM_LOWER_PRIMARY:
                    RANDOM_LOWER_PRIMARY.append((random_level, random_index))
                else:
                    thread_random = Thread(target=self.random_getter_primary)
                    thread_random.start()
                    thread_random.join()

    def random_getter_odrinary(self):
        ABLE_ODRINARY_LOWER.clear()
        data = Store.read_json()

        able_thread = Thread(target=self.able_lower_lst, args=[
                             ABLE_ODRINARY_LOWER, LOWERUSERORDINARY])
        able_thread.start()
        able_thread.join()

        if ABLE_ODRINARY_LOWER != []:
            random_level = random.choice(ABLE_ODRINARY_LOWER)
            random_index = random.randrange(
                len(data[LOWERUSERORDINARY][random_level]))

            if RANDOM_LOWER_ODRINAEY == []:
                RANDOM_LOWER_ODRINAEY.append((random_level, random_index))
            else:
                if (random_level, random_index) not in RANDOM_LOWER_ODRINAEY:
                    RANDOM_LOWER_ODRINAEY.append((random_level, random_index))
                else:
                    RANDOM_LOWER_ODRINAEY.clear()
                    thread_random = Thread(target=self.random_getter_odrinary)
                    thread_random.start()
                    thread_random.join()

    def random_getter_advanced(self):
        ABLE_ADVANCED_LOWER.clear()
        data = Store.read_json()

        accessable = False

        able_thread = Thread(target=self.able_lower_lst, args=[
                             ABLE_ADVANCED_LOWER, LOWERUSERADVANCED, True])
        able_thread.start()
        able_thread.join()

        if ABLE_ADVANCED_LOWER != []:
            random_level = random.choice(
                [lst[0] for lst in ABLE_ADVANCED_LOWER])
            random_stream = random.choice(
                [lst[-1] for lst in ABLE_ADVANCED_LOWER])

            if (random_level, random_stream) in ABLE_ADVANCED_LOWER and accessable == False:
                accessable = True

            if accessable == True:
                random_index = random.randrange(
                    len(data[LOWERUSERADVANCED][random_level][random_stream]))
                if RANDOM_LOWER_ADVANCED == []:
                    RANDOM_LOWER_ADVANCED.append(
                        (random_level, random_stream, random_index))
                else:
                    if (random_level, random_stream, random_index) not in RANDOM_LOWER_ADVANCED:
                        RANDOM_LOWER_ADVANCED.append(
                            (random_level, random_stream, random_index))
                    else:
                        RANDOM_LOWER_ADVANCED.clear()
                        thread_random = Thread(
                            target=self.random_getter_advanced)
                        thread_random.start()
                        thread_random.join()

    def random_getter_inter(self):
        data = Store.read_json()
        if data[INTERUSER] != []:
            random_index = random.randrange(len(data[INTERUSER]))

            if RANDOM_INTER == []:
                RANDOM_INTER.append(random_index)
            else:
                if random_index not in RANDOM_INTER:
                    RANDOM_INTER.append(random_index)
                else:
                    RANDOM_INTER.clear()
                    thread_random = Thread(target=self.random_getter_inter)
                    thread_random.start()
                    thread_random.join()

    def random_getter_primary_left(self):
        data = Store.read_json_for_left()
        if data[LOWERUSERPRIMARY] != []:
            random_index = random.randrange(len(data[LOWERUSERPRIMARY]))

            if RANDOM_LOWER_PRIMARY_LEFT == []:
                RANDOM_LOWER_PRIMARY_LEFT.append(random_index)
            else:
                if random_index not in RANDOM_LOWER_PRIMARY_LEFT:
                    RANDOM_LOWER_PRIMARY_LEFT.append(random_index)
                else:
                    thread_random = Thread(
                        target=self.random_getter_primary_left)
                    thread_random.start()
                    thread_random.join()

    def random_getter_odrinary_left(self):
        data = Store.read_json_for_left()
        if data[LOWERUSERORDINARY] != []:
            random_index = random.randrange(len(data[LOWERUSERORDINARY]))

            if RANDOM_LOWER_ODRINAEY_LEFT == []:
                RANDOM_LOWER_ODRINAEY_LEFT.append(random_index)
            else:
                if random_index not in RANDOM_LOWER_ODRINAEY_LEFT:
                    RANDOM_LOWER_ODRINAEY_LEFT.append(random_index)
                else:
                    thread_random = Thread(
                        target=self.random_getter_odrinary_left)
                    thread_random.start()
                    thread_random.join()

    def random_getter_inter_left(self):
        data = Store.read_json_for_left()
        if data[INTERUSER] != []:
            random_index = random.randrange(len(data[INTERUSER]))

            if RANDOM_INTER_LEFT == []:
                RANDOM_INTER_LEFT.append(random_index)
            else:
                if random_index not in RANDOM_INTER_LEFT:
                    RANDOM_INTER_LEFT.append(random_index)
                else:
                    thread_random = Thread(
                        target=self.random_getter_inter_left)
                    thread_random.start()
                    thread_random.join()

    def random_getter_advanced_left(self):
        data = Store.read_json_for_left()
        if data[LOWERUSERADVANCED] != []:
            random_index = random.randrange(len(data[LOWERUSERADVANCED]))

            if RANDOM_LOWER_ADVANCED_LEFT != []:
                RANDOM_LOWER_ADVANCED_LEFT.append(random_index)
            else:
                if random_index not in RANDOM_LOWER_ADVANCED_LEFT:
                    RANDOM_LOWER_ADVANCED_LEFT.append(random_index)
                else:
                    thread_random = Thread(
                        target=self.random_getter_advanced_left)
                    thread_random.start()
                    thread_random.join()

    def show_random_lower(self, label_object, type, frame_object,  user_index, user_level=None, stream=None):
        if type == "pri":
            label_object.setFont(self.font_info)
            __target = self.decryptForLowerPrimary(user_level, user_index)
            frame_object.setMinimumSize(QSize(0, 500))
            label_object.setText(f"""
				<html>
					<head/>
					<body>
					<p align=\"center\"> <b>STUDENTS TYPE - PRIMARY</b> </p>
					<br>
					<p>
						<pre><spen>Roll-Number          :   {__target[0]}</pre></spen>
						<pre><spen>Name                 :   {__target[1].title()}</pre></spen>
						<pre><spen>Address              :   <address>{__target[2].title()}</address></pre></spen>
						<pre><spen>Father-Name          :   {__target[3].title()}</pre></spen>
						<pre><spen>Mather-Name          :   {__target[4].title()}</pre></spen>
						<pre><spen>Contact-Number       :   {__target[5]}</pre></spen>
						<pre><spen>Registration-Number  :   {__target[6]}</pre></spen>
						<pre><spen>Level                :   {__target[7]}</pre></spen>
						<pre><spen>E-Mail               :   {__target[8]}</pre></spen>
						<pre><spen>Religion             :   {__target[9].title()}</pre></spen>
						<pre><spen>Date-Of-Birth        :   {__target[10]}</pre></spen>
						<pre><spen>Gender               :   {__target[11]}</pre></spen>
					</p>
					<br>
				    </body>
			    </html>
		    """)
        elif type == "od":
            label_object.setFont(self.font_info)
            __target = self.decryptForLower(user_level,  user_index)
            frame_object.setMinimumSize(QSize(0, 500))
            label_object.setText(f"""
				<html>
					<head/>
					<body>
					<p align=\"center\"> <b>STUDENTS TYPE - ODRINARY</b> </p>
					<br>
					<p>
						<pre><spen>Roll-Number          :   {__target[0]}</pre></spen>
						<pre><spen>Name                 :   {__target[1].title()}</pre></spen>
						<pre><spen>Address              :   <address>{__target[2].title()}</address></pre></spen>
						<pre><spen>Father-Name          :   {__target[3].title()}</pre></spen>
						<pre><spen>Mather-Name          :   {__target[4].title()}</pre></spen>
						<pre><spen>Contact-Number       :   {__target[5]}</pre></spen>
						<pre><spen>Registration-Number  :   {__target[6]}</pre></spen>
						<pre><spen>Level                :   {__target[7]}</pre></spen>
						<pre><spen>E-Mail               :   {__target[8]}</pre></spen>
						<pre><spen>Religion             :   {__target[9].title()}</pre></spen>
						<pre><spen>Date-Of-Birth        :   {__target[10]}</pre></spen>
						<pre><spen>Gender               :   {__target[11]}</pre></spen>
					</p>
					<br>
				    </body>
			    </html>
		    """)
        elif type == "in":
            label_object.setFont(self.font_info)
            __target = self.decryptForInter(user_index)
            frame_object.setMinimumSize(QSize(0, 400))
            label_object.setText(f"""
				<html>
					<head/>
					<body>
					<p align=\"center\"> <b>TEACHER TYPE</b> </p>
					<br>
					<p>
						<pre><spen>Roll-Number      :   {__target[0]}</spen></pre>
						<pre><spen>Name             :   {__target[1]}</spen></pre>
						<pre><spen>Address          :   <address>{__target[2]}</address></spen></pre>
						<pre><spen>Subject          :   {__target[3]}</spen></pre>
						<pre><spen>E-Mail           :   {__target[4]}</spen></pre>
						<pre><spen>Contact-Number   :   {__target[5]}</spen></pre>
						<pre><spen>Level            :   {__target[6]}</spen></pre>
						<pre><spen>Gender           :   {__target[7]}</spen></pre>
					</p>
					<br>
				    </body>
			    </html>
		    """)
        else:
            label_object.setFont(self.font_info)
            __target = self.decryptForAdvanceLowerLeft(
                user_index,  user_level, stream)
            frame_object.setMinimumSize(QSize(0, 500))
            label_object.setText(f"""
				<html>
					<head/>
					<body>
					<p align=\"center\"> <b>STUDENTS TYPE - ADVANCED</b> </p>
					<br>
					<p>
						<pre><spen>Roll-Number          :   {__target[0]}</pre></spen>
						<pre><spen>Name                 :   {__target[1].title()}</pre></spen>
						<pre><spen>Address              :   <address>{__target[2].title()}</address></pre></spen>
						<pre><spen>Father-Name          :   {__target[3].title()}</pre></spen>
						<pre><spen>Mather-Name          :   {__target[4].title()}</pre></spen>
						<pre><spen>Contact-Number       :   {__target[5]}</pre></spen>
						<pre><spen>Registration-Number  :   {__target[6]}</pre></spen>
						<pre><spen>Level                :   {__target[7]}</pre></spen>
						<pre><spen>E-Mail               :   {__target[8]}</pre></spen>
						<pre><spen>Religion             :   {__target[9].title()}</pre></spen>
						<pre><spen>Date-Of-Birth        :   {__target[10]}</pre></spen>
						<pre><spen>Gender               :   {__target[11]}</pre></spen>
                        <pre><spen>Stream               :   {__target[12]}</pre></spen>
					</p>
					<br>
				    </body>
			    </html>
		    """)

    def show_random_lower_left(self, label_object, type, frame_object,  user_index):
        if type == "pri":
            label_object.setFont(self.font_info)
            __target = self.decryptForLowerPrimaryLeft(user_index)
            frame_object.setMinimumSize(QSize(0, 500))
            label_object.setText(f"""
				<html>
					<head/>
					<body>
					<p align=\"center\"> <b>STUDENTS TYPE - PRIMARY | Recycle Bin</b> </p>
					<br>
					<p>
						<pre><spen>Roll-Number          :   {__target[0]}</pre></spen>
						<pre><spen>Name                 :   {__target[1].title()}</pre></spen>
						<pre><spen>Address              :   <address>{__target[2].title()}</address></pre></spen>
						<pre><spen>Father-Name          :   {__target[3].title()}</pre></spen>
						<pre><spen>Mather-Name          :   {__target[4].title()}</pre></spen>
						<pre><spen>Contact-Number       :   {__target[5]}</pre></spen>
						<pre><spen>Registration-Number  :   {__target[6]}</pre></spen>
						<pre><spen>Level                :   {__target[7]}</pre></spen>
						<pre><spen>E-Mail               :   {__target[8]}</pre></spen>
						<pre><spen>Religion             :   {__target[9].title()}</pre></spen>
						<pre><spen>Date-Of-Birth        :   {__target[10]}</pre></spen>
						<pre><spen>Gender               :   {__target[11]}</pre></spen>
					</p>
					<br>
				    </body>
			    </html>
		    """)
        elif type == "od":
            label_object.setFont(self.font_info)
            __target = self.decryptForLowerLeft(user_index)
            frame_object.setMinimumSize(QSize(0, 500))
            label_object.setText(f"""
				<html>
					<head/>
					<body>
					<p align=\"center\"> <b>STUDENTS TYPE - ODRINARY | Recycle Bin</b> </p>
					<br>
					<p>
						<pre><spen>Roll-Number          :   {__target[0]}</pre></spen>
						<pre><spen>Name                 :   {__target[1].title()}</pre></spen>
						<pre><spen>Address              :   <address>{__target[2].title()}</address></pre></spen>
						<pre><spen>Father-Name          :   {__target[3].title()}</pre></spen>
						<pre><spen>Mather-Name          :   {__target[4].title()}</pre></spen>
						<pre><spen>Contact-Number       :   {__target[5]}</pre></spen>
						<pre><spen>Registration-Number  :   {__target[6]}</pre></spen>
						<pre><spen>Level                :   {__target[7]}</pre></spen>
						<pre><spen>E-Mail               :   {__target[8]}</pre></spen>
						<pre><spen>Religion             :   {__target[9].title()}</pre></spen>
						<pre><spen>Date-Of-Birth        :   {__target[10]}</pre></spen>
						<pre><spen>Gender               :   {__target[11]}</pre></spen>
					</p>
					<br>
				    </body>
			    </html>
		    """)
        elif type == "in":
            label_object.setFont(self.font_info)
            __target = self.decryptForInterLeft(user_index)
            frame_object.setMinimumSize(QSize(0, 400))
            label_object.setText(f"""
				<html>
					<head/>
					<body>
					<p align=\"center\"> <b>TEACHER TYPE | Recycle Bin</b> </p>
					<br>
					<p>
						<pre><spen>Roll-Number      :   {__target[0]}</spen></pre>
						<pre><spen>Name             :   {__target[1]}</spen></pre>
						<pre><spen>Address          :   <address>{__target[2]}</address></spen></pre>
						<pre><spen>Subject          :   {__target[3]}</spen></pre>
						<pre><spen>E-Mail           :   {__target[4]}</spen></pre>
						<pre><spen>Contact-Number   :   {__target[5]}</spen></pre>
						<pre><spen>Level            :   {__target[6]}</spen></pre>
						<pre><spen>Gender           :   {__target[7]}</spen></pre>
					</p>
					<br>
				    </body>
			    </html>
		    """)
        else:
            label_object.setFont(self.font_info)
            __target = self.decryptForAdvanceLowerLeft(user_index)
            frame_object.setMinimumSize(QSize(0, 500))
            label_object.setText(f"""
				<html>
					<head/>
					<body>
					<p align=\"center\"> <b>STUDENTS TYPE - ADVANCED | Recycle Bin</b> </p>
					<br>
					<p>
						<pre><spen>Roll-Number          :   {__target[0]}</pre></spen>
						<pre><spen>Name                 :   {__target[1].title()}</pre></spen>
						<pre><spen>Address              :   <address>{__target[2].title()}</address></pre></spen>
						<pre><spen>Father-Name          :   {__target[3].title()}</pre></spen>
						<pre><spen>Mather-Name          :   {__target[4].title()}</pre></spen>
						<pre><spen>Contact-Number       :   {__target[5]}</pre></spen>
						<pre><spen>Registration-Number  :   {__target[6]}</pre></spen>
						<pre><spen>Level                :   {__target[7]}</pre></spen>
						<pre><spen>E-Mail               :   {__target[8]}</pre></spen>
						<pre><spen>Religion             :   {__target[9].title()}</pre></spen>
						<pre><spen>Date-Of-Birth        :   {__target[10]}</pre></spen>
						<pre><spen>Gender               :   {__target[11]}</pre></spen>
                        <pre><spen>Stream               :   {__target[12]}</pre></spen>
					</p>
					<br>
				    </body>
			    </html>
		    """)

    # Random Lower Shower
    def connect_lower_primary(self):
        try:
            thread_random = Thread(target=self.random_getter_primary)
            thread_random.start()
            thread_random.join()

            self.show_random_lower(self.ui.label_info_lower_pri, "pri", self.ui.widget_lower_pri,
                                   RANDOM_LOWER_PRIMARY[-1][-1], RANDOM_LOWER_PRIMARY[-1][0])
        except:
            self.ui.label_info_lower_pri.setText("""
                <h2 align=\"center\"> <b>Primary Students Are Not Available</b> </h2>
            """)

    def connect_lower_odrinary(self):
        try:
            thread_random = Thread(target=self.random_getter_odrinary)
            thread_random.start()
            thread_random.join()
            self.show_random_lower(self.ui.label_info_lower_1, "od", self.ui.widget_lower_1,
                                   RANDOM_LOWER_ODRINAEY[-1][-1], RANDOM_LOWER_ODRINAEY[-1][0])

        except:
            self.ui.label_info_lower_1.setText("""
                <h2 align=\"center\"> <b>Odrinaey Students Are Not Available</b> </h2>
            """)

    def connect_inter(self):
        try:
            thread_random = Thread(target=self.random_getter_inter)
            thread_random.start()
            thread_random.join()
            self.show_random_lower(
                self.ui.label_info_Inter_1, "in",  self.ui.widget_inter_1, RANDOM_INTER[-1])

        except:
            self.ui.label_info_Inter_1.setText("""
                <h2 align=\"center\"> <b>Teachers Are Not Available</b> </h2>
            """)

    def connect_lower_advanced(self):
        try:
            thread_random = Thread(target=self.random_getter_advanced)
            thread_random.start()
            thread_random.join()

            print(RANDOM_LOWER_ADVANCED)
            self.show_random_lower(self.ui.label_info_lower_advan, "ad", self.ui.widget_lower_advan,
                                   RANDOM_LOWER_ADVANCED[-1][-1], RANDOM_LOWER_ADVANCED[-1][0], RANDOM_LOWER_ADVANCED[-1][-2])

        except:
            self.ui.label_info_lower_advan.setText("""
                <h2 align=\"center\"> <b>Advanced Students Are Not Available</b> </h2>
            """)

    def connect_lower_primary_Left(self):
        try:
            thread_random = Thread(target=self.random_getter_primary_left)
            thread_random.start()
            thread_random.join()
            self.show_random_lower_left(self.ui.info_lower_left_pri, "pri",
                                        self.ui.widget_lower_left_pri, RANDOM_LOWER_PRIMARY_LEFT[-1])
        except:
            self.ui.info_lower_left_pri.setText(
                """<h2 align=\"center\"> <b>Primary Students Are Not Available</b> </h2>"""
            )

    def connect_lower_odrinary_left(self):
        try:
            thread_random = Thread(target=self.random_getter_odrinary_left)
            thread_random.start()
            thread_random.join()
            self.show_random_lower_left(
                self.ui.info_lower_1, "od", self.ui.widget_lower_left_1, RANDOM_LOWER_ODRINAEY_LEFT[-1])
        except:
            self.ui.info_lower_1.setText(
                """<h2 align=\"center\"> <b>Odrinaey Students Are Not Available</b> </h2>"""
            )

    def connect_inter_left(self):
        try:
            thread_random = Thread(target=self.random_getter_inter_left)
            thread_random.start()
            thread_random.join()
            self.show_random_lower_left(
                self.ui.info_inter_left_1, "in", self.ui.widget_inter_left_1, RANDOM_INTER_LEFT[-1])
        except:
            self.ui.info_inter_left_1.setText(
                """<h2 align=\"center\"> <b>Teachers Are Not Available</b> </h2>"""
            )

    def connect_lower_advanced_left(self):
        try:
            thread_random = Thread(target=self.random_getter_advanced_left)
            thread_random.start()
            thread_random.join()
            print(RANDOM_LOWER_ADVANCED_LEFT)
            self.show_random_lower_left(self.ui.info_lower_left_advan, "ad",
                                        self.ui.widget_lower_left_advan, RANDOM_LOWER_ADVANCED_LEFT[-1])
        except:
            self.ui.info_lower_left_advan.setText("""
                <h2 align=\"center\"> <b>Advanced Students Are Not Available</b> </h2>
            """)
    # Decrypt For Inter User

    def decryptForInter(self, userNumber):
        data = Store.read_json()

        if data[INTERUSER][userNumber]["Level"] != None:
            __level = secure.decrypt(
                data[INTERUSER][userNumber]["Level"][-2], data[INTERUSER][userNumber]["Level"][-1])
        else:
            __level = data[INTERUSER][userNumber]["Level"]

        if data[INTERUSER][userNumber]["Subject"] != None:
            __subject = secure.decrypt(
                data[INTERUSER][userNumber]["Subject"][-2], data[INTERUSER][userNumber]["Subject"][-1])
        else:
            __subject = data[INTERUSER][userNumber]["Subject"]

        if data[INTERUSER][userNumber]["E-Mail"] != None:
            __email = secure.decrypt(
                data[INTERUSER][userNumber]["E-Mail"][-2], data[INTERUSER][userNumber]["E-Mail"][-1])
        else:
            __email = data[INTERUSER][userNumber]["E-Mail"]

        __roll = data[INTERUSER][userNumber]["Roll"]
        __name = secure.decrypt(
            data[INTERUSER][userNumber]["Name"][-2], data[INTERUSER][userNumber]["Name"][-1])
        __address = secure.decrypt(
            data[INTERUSER][userNumber]["Address"][-2], data[INTERUSER][userNumber]["Address"][-1])

        __contact_number = secure.decrypt(
            data[INTERUSER][userNumber]["Contact-Number"][-2], data[INTERUSER][userNumber]["Contact-Number"][-1])

        __gender = secure.decrypt(
            data[INTERUSER][userNumber]["Gender"][-2], data[INTERUSER][userNumber]["Gender"][-1])

        __target = [__roll, __name, __address, __subject,
                    __email, __contact_number, __level, __gender]

        return __target
        # Decrypt For primary user

    def decryptForLowerPrimaryLeft(self,  userNumber):
        data = Store.read_json_for_left()

        __roll = data[LOWERUSERPRIMARY][userNumber]['Roll']
        __name = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]
                                ['Name'][-2], data[LOWERUSERPRIMARY][userNumber]['Name'][-1])
        __address = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]['Address']
                                   [-2], data[LOWERUSERPRIMARY][userNumber]['Address'][-1])
        __fatherName = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]['Father-Name']
                                      [-2], data[LOWERUSERPRIMARY][userNumber]['Father-Name'][-1])
        __matherName = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]['Mather-Name']
                                      [-2], data[LOWERUSERPRIMARY][userNumber]['Mather-Name'][-1])
        __contact_number = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]['Contact-Number']
                                          [-2], data[LOWERUSERPRIMARY][userNumber]['Contact-Number'][-1])
        __ragistartion_number = secure.decrypt(
            data[LOWERUSERPRIMARY][userNumber]['Registration-Number'][-2], data[LOWERUSERPRIMARY][userNumber]['Registration-Number'][-1])
        __level = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]
                                 ['Level'][-2], data[LOWERUSERPRIMARY][userNumber]['Level'][-1])
        __religion = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]['Religion']
                                    [-2], data[LOWERUSERPRIMARY][userNumber]['Religion'][-1])
        __dateOfBirth = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]['Date-of-Birth']
                                       [-2], data[LOWERUSERPRIMARY][userNumber]['Date-of-Birth'][-1])
        __gender = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]
                                  ['Gender'][-2], data[LOWERUSERPRIMARY][userNumber]['Gender'][-1])

        if data[LOWERUSERPRIMARY][userNumber]['E-Mail'] != None:
            __email = secure.decrypt(data[LOWERUSERPRIMARY][userNumber]['E-Mail']
                                     [-2], data[LOWERUSERPRIMARY][userNumber]['E-Mail'][-1])
        else:
            __email = data[LOWERUSERPRIMARY][userNumber]['E-Mail']

        __target = [__roll, __name, __address, __fatherName, __matherName, __contact_number,
                    __ragistartion_number, __level, __email, __religion, __dateOfBirth, __gender]
        return __target

    # Decrypt For primary user

    def decryptForLowerPrimary(self, userLevel, userNumber):
        data = Store.read_json()

        __roll = data[LOWERUSERPRIMARY][userLevel][userNumber]['Roll']
        __name = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]
                                ['Name'][-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Name'][-1])
        __address = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]['Address']
                                   [-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Address'][-1])
        __fatherName = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]['Father-Name']
                                      [-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Father-Name'][-1])
        __matherName = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]['Mather-Name']
                                      [-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Mather-Name'][-1])
        __contact_number = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]['Contact-Number']
                                          [-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Contact-Number'][-1])
        __ragistartion_number = secure.decrypt(
            data[LOWERUSERPRIMARY][userLevel][userNumber]['Registration-Number'][-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Registration-Number'][-1])
        __level = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]
                                 ['Level'][-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Level'][-1])
        __religion = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]['Religion']
                                    [-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Religion'][-1])
        __dateOfBirth = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]['Date-of-Birth']
                                       [-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Date-of-Birth'][-1])
        __gender = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]
                                  ['Gender'][-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['Gender'][-1])

        if data[LOWERUSERPRIMARY][userLevel][userNumber]['E-Mail'] != None:
            __email = secure.decrypt(data[LOWERUSERPRIMARY][userLevel][userNumber]['E-Mail']
                                     [-2], data[LOWERUSERPRIMARY][userLevel][userNumber]['E-Mail'][-1])
        else:
            __email = data[LOWERUSERPRIMARY][userLevel][userNumber]['E-Mail']

        __target = [__roll, __name, __address, __fatherName, __matherName, __contact_number,
                    __ragistartion_number, __level, __email, __religion, __dateOfBirth, __gender]
        return __target

    # Decrypt For Lower User
    def decryptForLower(self, userLevel, userNumber):
        data = Store.read_json()

        __roll = data[LOWERUSERORDINARY][userLevel][userNumber]['Roll']
        __name = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]
                                ['Name'][-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Name'][-1])
        __address = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]['Address']
                                   [-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Address'][-1])
        __fatherName = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]['Father-Name']
                                      [-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Father-Name'][-1])
        __matherName = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]['Mather-Name']
                                      [-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Mather-Name'][-1])
        __contact_number = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]['Contact-Number']
                                          [-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Contact-Number'][-1])
        __ragistartion_number = secure.decrypt(
            data[LOWERUSERORDINARY][userLevel][userNumber]['Registration-Number'][-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Registration-Number'][-1])
        __level = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]
                                 ['Level'][-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Level'][-1])
        __religion = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]['Religion']
                                    [-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Religion'][-1])
        __dateOfBirth = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]['Date-of-Birth']
                                       [-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Date-of-Birth'][-1])
        __gender = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]
                                  ['Gender'][-2], data[LOWERUSERORDINARY][userLevel][userNumber]['Gender'][-1])

        if data[LOWERUSERORDINARY][userLevel][userNumber]['E-Mail'] != None:
            __email = secure.decrypt(data[LOWERUSERORDINARY][userLevel][userNumber]['E-Mail']
                                     [-2], data[LOWERUSERORDINARY][userLevel][userNumber]['E-Mail'][-1])
        else:
            __email = data[LOWERUSERORDINARY][userLevel][userNumber]['E-Mail']

        __target = [__roll, __name, __address, __fatherName, __matherName, __contact_number,
                    __ragistartion_number, __level, __email, __religion, __dateOfBirth, __gender]
        return __target

    # Roll Number for left status Inter
    def leftStatusRollNumberForInter(self):
        data = Store.read_json_for_left()
        interUserList = data[INTERUSER]

        interUserCount = 0
        if interUserList == []:
            rollnumberForLeftStatusInter = f"INTER{interUserCount:04}I|LEFT"
            interUserCount += 1
        else:
            getLastRollNumberForInter = interUserList[-1]['Roll']
            getLastRollNumberForInter = int(
                getLastRollNumberForInter.split("INTER")[-1].split("I")[0])
            getLastRollNumberForInter += 1
            rollnumberForLeftStatusInter = f"INTER{getLastRollNumberForInter:04}I|LEFT"

        return rollnumberForLeftStatusInter

    # Roll Number for left status Lower
    def leftStatusRollNumberForLower(self):
        data = Store.read_json_for_left()
        lowerUserList = data[LOWERUSERORDINARY]

        lowerUserCount = 0
        if lowerUserList == []:
            rollnumberForLeftStatusLower = f"LOWER{lowerUserCount:04}L|ORDINARY-LEFT"
            lowerUserCount += 1
        else:
            getLastRollNumberForLower = lowerUserList[-1]['Roll']
            getLastRollNumberForLower = int(
                getLastRollNumberForLower.split("LOWER")[-1].split("|")[0].split("L")[0])
            getLastRollNumberForLower += 1
            rollnumberForLeftStatusLower = f"LOWER{getLastRollNumberForLower:04}L|ORDINARY-LEFT"

        return rollnumberForLeftStatusLower

    # Roll Number For Left Status Primary Lower
    def leftStatusRollNumberForPrimaryLower(self):
        data = Store.read_json_for_left()
        lowerUserList = data[LOWERUSERPRIMARY]

        lowerUserCount = 0
        if lowerUserList == []:
            rollNumberForLeftStatusPrimaryLower = f"LOWER{lowerUserCount:04}L|PRIMARY-LEFT"
            lowerUserCount += 1
        else:
            getLastRollNumberForPrimaryLower = lowerUserList[-1]["Roll"]
            getLastRollNumberForPrimaryLower = int(
                getLastRollNumberForPrimaryLower.split(
                    "LOWER")[-1].split("|")[0].split("L")[0]
            )
            getLastRollNumberForPrimaryLower += 1
            rollNumberForLeftStatusPrimaryLower = f"LOWER{getLastRollNumberForPrimaryLower:04}L|PRIMARY-LEFT"

        return rollNumberForLeftStatusPrimaryLower

    # Roll Number For Left Status Advance
    def leftStatusRollNumberForAdvanceLower(self):
        data = Store.read_json_for_left()
        lowerUserLeft = data[LOWERUSERADVANCED]

        lowerUserCount = 0
        if lowerUserLeft == []:
            rollNumberForLeftStatusAdvanceLower = f"LOWER{lowerUserCount:04}L|ADVANCE-LEFT"
            lowerUserCount += 1
        else:
            getLastRollNumberForAdvanceLower = lowerUserLeft[-1]['Roll']
            getLastRollNumberForAdvanceLower = int(
                getLastRollNumberForAdvanceLower.split("LOWER")[-1].split("L")[0])
            getLastRollNumberForAdvanceLower += 1
            rollNumberForLeftStatusAdvanceLower = f"LOWER{getLastRollNumberForAdvanceLower:04}L|ADVANCE-LEFT"

        return rollNumberForLeftStatusAdvanceLower

    # Connect Name Search
    def connectIntoNameSearch(self):

        # CLEAR THE NAME LIST
        def clear():
            NAME_SEARCH_INTER_ACTIVE.clear()
            NAME_SEARCH_LOWER_ACTIVE.clear()
            NAME_SEARCH_INTER_LEFT.clear()
            NAME_SEARCH_LOWER_LEFT.clear()
            NAME_SEARCH_ADVANCE_LOWER.clear()
            NAME_SEARCH_ADVANCE_LOWER_LEFT.clear()
            NAME_SEARCH_PRIMARY_LOWER.clear()
            NAME_SEARCH_PRIMARY_LOWER_LEFT.clear()

        # CLEAR THE ROLL LEFT
        def rollClear():
            ROLL_SEARCH_INTER_ACTIVE.clear()
            ROLL_SEARCH_LOWER_ACTIVE.clear()
            ROLL_SEARCH_INTER_LEFT.clear()
            ROLL_SEARCH_LOWER_LEFT.clear()
            ROLL_SEARCH_ADVANCED_LOWER.clear()
            ROLL_SEARCH_ADVANCED_LOWER_LEFT.clear()
            ROLL_SEARCH_PRIMARY_LOWER.clear()
            ROLL_SEARCH_PRIMARY_LOWER_LEFT.clear()

        # THREAD FOR CLEAR
        clearThread = Thread(target=clear)
        clearThread.start()
        clearThread.join()

        # THREAD FOR CLEAR
        rollClear = Thread(target=rollClear)
        rollClear.start()
        rollClear.join()

        # THREAD FOR NAME SEARCH
        searchThread = Thread(target=self.searchName)
        searchThread.start()
        searchThread.join()

        # Run the Base Search Frame
        self.main_frame_for_base_search()
        self.vars_names.clear()
        self.counter_inter = 0
        self.counter_lower = 0
        self.counter_inter_l = 0
        self.counter_lower_l = 0
        self.counter_ad_lower = 0
        self.counter_ad_lower_l = 0
        self.counter_pri_lower = 0
        self.counter_pri_lower_left = 0

        if NAME_SEARCH_INTER_ACTIVE == [] and NAME_SEARCH_LOWER_ACTIVE == [] and NAME_SEARCH_INTER_LEFT == [] and NAME_SEARCH_LOWER_LEFT == [] and NAME_SEARCH_ADVANCE_LOWER == [] and NAME_SEARCH_ADVANCE_LOWER_LEFT == [] and NAME_SEARCH_PRIMARY_LOWER == [] and NAME_SEARCH_PRIMARY_LOWER_LEFT == []:
            self.not_found_frame()

        if NAME_SEARCH_INTER_ACTIVE != []:
            for index in NAME_SEARCH_INTER_ACTIVE:
                __target = self.decryptForInter(index)
                self.inti_frame_for_search_resalt(f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>TEACHERS TYPE</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number      :   {__target[0]}</spen></pre>
                                <pre><spen>Name             :   {__target[1]}</spen></pre>
                                <pre><spen>Address          :   <address>{__target[2]}</address></spen></pre>
                                <pre><spen>Subject          :   {__target[3]}</spen></pre>
                                <pre><spen>E-Mail           :   {__target[4]}</spen></pre>
                                <pre><spen>Contact-Number   :   {__target[5]}</spen></pre>
                                <pre><spen>Level            :   {__target[6]}</spen></pre>
                                <pre><spen>Gender           :   {__target[7]}</spen></pre>
                            </p>
                        </body>
                    </html>
                """, "inter")

        if NAME_SEARCH_PRIMARY_LOWER != []:
            for index in NAME_SEARCH_PRIMARY_LOWER:
                print(index)
                __target = self.decryptForLowerPrimary(index[-1], index[0])
                self.inti_frame_for_search_resalt(f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>STUDENTS TYPE</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                                <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                                <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                                <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                                <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                                <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                                <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                                <pre><spen>Level                :   {__target[7]}</spen></pre>
                                <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                                <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                                <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                                <pre><spen>Gender               :   {__target[11]}</spen></pre>
                            </p>
                            <br>
                        </body>
                    </html>
                """, "pri_lower")

        if NAME_SEARCH_PRIMARY_LOWER_LEFT != []:
            for index in NAME_SEARCH_PRIMARY_LOWER_LEFT:
                __target = self.decryptForLowerPrimaryLeft(index)
                self.inti_frame_for_search_resalt(f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>STUDENTS TYPE | Recycle Bin</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                                <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                                <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                                <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                                <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                                <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                                <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                                <pre><spen>Level                :   {__target[7]}</spen></pre>
                                <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                                <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                                <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                                <pre><spen>Gender               :   {__target[11]}</spen></pre>
                            </p>
                            <br>
                        </body>
                    </html>
                """, "pri_lower_l")

        if NAME_SEARCH_LOWER_ACTIVE != []:
            for index in NAME_SEARCH_LOWER_ACTIVE:
                __target = self.decryptForLower(index[-1], index[0])
                self.inti_frame_for_search_resalt(f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>STUDENTS TYPE</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                                <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                                <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                                <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                                <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                                <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                                <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                                <pre><spen>Level                :   {__target[7]}</spen></pre>
                                <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                                <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                                <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                                <pre><spen>Gender               :   {__target[11]}</spen></pre>
                            </p>
                            <br>
                        </body>
                    </html>
                """, "lower")

        if NAME_SEARCH_INTER_LEFT != []:
            for index in NAME_SEARCH_INTER_LEFT:
                __target = self.decryptForInterLeft(index)
                self.inti_frame_for_search_resalt(f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>TEACHERS TYPE | Recycle Bin</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number      :   {__target[0]}<spen></pre>
                                <pre><spen>Name             :   {__target[1]}<spen></pre>
                                <pre><spen>Address          :   <address>{__target[2]}</address><spen></pre>
                                <pre><spen>Subject          :   {__target[3]}<spen></pre>
                                <pre><spen>E-Mail           :   {__target[4]}<spen></pre>
                                <pre><spen>Contact-Number   :   {__target[5]}<spen></pre>
                                <pre><spen>Level            :   {__target[6]}<spen></pre>
                                <pre><spen>Gender           :   {__target[7]}<spen></pre>
                            </p>
                        </body>
                    </html>
                """, "inter_l")

        if NAME_SEARCH_LOWER_LEFT != []:
            for index in NAME_SEARCH_LOWER_LEFT:
                __target = self.decryptForLowerLeft(index)
                self.inti_frame_for_search_resalt(f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>STUDENTS TYPE | Recycle Bin</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                                <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                                <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                                <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                                <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                                <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                                <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                                <pre><spen>Level                :   {__target[7]}</spen></pre>
                                <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                                <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                                <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                                <pre><spen>Gender               :   {__target[11]}</spen></pre>
                            </p>
                            <br>
                        </body>
                    </html>
                """, "lower_l")

        if NAME_SEARCH_ADVANCE_LOWER != []:
            for index, stream, level in NAME_SEARCH_ADVANCE_LOWER:
                __target = self.decryptForAdvanceLowerLeft(
                    index, level, stream)
                self.inti_frame_for_search_resalt(
                    f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>ADVANCED STUDENTS TYPE</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                                <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                                <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                                <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                                <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                                <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                                <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                                <pre><spen>Level                :   {__target[7]}</spen></pre>
                                <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                                <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                                <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                                <pre><spen>Gender               :   {__target[11]}</spen></pre>
                                <pre><spen>Stream               :   {__target[12].title()}</spen></pre>
                            </p>
                            <br>
                        </body>
                    </html>

                    """, "adv_lower")

        if NAME_SEARCH_ADVANCE_LOWER_LEFT != []:
            for index in NAME_SEARCH_ADVANCE_LOWER_LEFT:
                __target = self.decryptForAdvanceLowerLeft(index, None, None)
                self.inti_frame_for_search_resalt(
                    f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>ADVANCED STUDENTS TYPE | Recycle Bin</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                                <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                                <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                                <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                                <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                                <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                                <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                                <pre><spen>Level                :   {__target[7]}</spen></pre>
                                <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                                <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                                <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                                <pre><spen>Gender               :   {__target[11]}</spen></pre>
                                <pre><spen>Stream               :   {__target[12].title()}</spen></pre>
                            </p>
                            <br>
                        </body>
                    </html>

                    """, "adv_lower_l")

        # Call the delete button function
        if NAME_SEARCH_ADVANCE_LOWER != []:
            for index in range(len(NAME_SEARCH_ADVANCE_LOWER)):
                self.vars_names["btn_adv_lower_"+str(index)].clicked.connect(
                    lambda _, value=index: self.deleteAdvanceLowerUserForSearch(NAME_SEARCH_ADVANCE_LOWER[value]))

        if NAME_SEARCH_ADVANCE_LOWER_LEFT != []:
            for index in range(len(NAME_SEARCH_ADVANCE_LOWER_LEFT)):
                self.vars_names["btn_adv_lower_l_"+str(index)].clicked.connect(
                    lambda _, value=index: self.deleteAdvanceLowerLeftForSearch(NAME_SEARCH_ADVANCE_LOWER_LEFT[value]))

        if NAME_SEARCH_INTER_ACTIVE != []:
            for index in range(len(NAME_SEARCH_INTER_ACTIVE)):
                self.vars_names["btn_inter_"+str(index)].clicked.connect(
                    lambda _, value=index: self.deleteInterUserForSearch(NAME_SEARCH_INTER_ACTIVE[value]))

        if NAME_SEARCH_LOWER_ACTIVE != []:
            for index in range(len(NAME_SEARCH_LOWER_ACTIVE)):
                self.vars_names["btn_lower_"+str(index)].clicked.connect(
                    lambda _, value=index: self.deleteLowerUserForSearch(NAME_SEARCH_LOWER_ACTIVE[value]))

        if NAME_SEARCH_INTER_LEFT != []:
            for index in range(len(NAME_SEARCH_INTER_LEFT)):
                self.vars_names["btn_inter_l_"+str(index)].clicked.connect(
                    lambda _, value=index: self.deleteInterUserLeftForSearch(NAME_SEARCH_INTER_LEFT[value]))

        if NAME_SEARCH_LOWER_LEFT != []:
            for index in range(len(NAME_SEARCH_LOWER_LEFT)):
                self.vars_names["btn_lower_l_"+str(index)].clicked.connect(
                    lambda _, value=index: self.deleteLowerUserLeftForSearch(NAME_SEARCH_LOWER_LEFT[value]))

        if NAME_SEARCH_PRIMARY_LOWER != []:
            for index in range(len(NAME_SEARCH_PRIMARY_LOWER)):
                self.vars_names["btn_pri_lower_"+str(index)].clicked.connect(
                    lambda _, value=index: self.deletePrimaryLowerUserForSearch(
                        NAME_SEARCH_PRIMARY_LOWER[value])
                )

        if NAME_SEARCH_PRIMARY_LOWER_LEFT != []:
            for index in range(len(NAME_SEARCH_PRIMARY_LOWER_LEFT)):
                print(self.vars_names)
                self.vars_names["btn_pri_lower_l_"+str(index)].clicked.connect(
                    lambda _, value=index: self.deletePrimaryLowerUserForSearchLeft(
                        NAME_SEARCH_PRIMARY_LOWER_LEFT[value])
                )

    def deleteInterUserForSearch(self, index):
        a_data = Store.read_json()
        activeInterUserList = a_data[INTERUSER][index]
        activeInterUserList["Roll"] = self.leftStatusRollNumberForInter()
        Store.update_json_for_left(activeInterUserList, INTERUSER)
        del a_data[INTERUSER][index]
        Store.write_json(a_data)
        self.connect_inter()
        self.connect_inter_left()
        self.connectIntoNameSearch()
        self.data_frame()

    def deleteLowerUserForSearch(self, index):
        a_data = Store.read_json()
        activeLowerUserList = a_data[LOWERUSERORDINARY][index[-1]][index[-2]]
        activeLowerUserList["Roll"] = self.leftStatusRollNumberForLower()
        Store.update_json_for_left(activeLowerUserList, LOWERUSERORDINARY)
        del a_data[LOWERUSERORDINARY][index[-1]][index[-2]]
        Store.write_json(a_data)
        self.connect_lower_odrinary()
        self.connect_lower_odrinary_left()
        self.connectIntoNameSearch()
        self.data_frame()

    def deletePrimaryLowerUserForSearch(self, index):
        a_data = Store.read_json()
        activePrimaryLowerUserList = a_data[LOWERUSERPRIMARY][index[-1]][index[-2]]
        activePrimaryLowerUserList["Roll"] = self.leftStatusRollNumberForPrimaryLower(
        )
        Store.update_json_for_left(
            activePrimaryLowerUserList, LOWERUSERPRIMARY)
        del a_data[LOWERUSERPRIMARY][index[-1]][index[-2]]
        Store.write_json(a_data)
        self.connectIntoNameSearch()
        self.data_frame()
        self.connect_lower_primary()
        self.connect_lower_primary_Left()

    def deletePrimaryLowerUserForSearchLeft(self, index):
        l_data = Store.read_json_for_left()
        del l_data[LOWERUSERPRIMARY][index]
        Store.write_json_for_left(l_data)
        self.connectIntoNameSearch()
        self.connect_lower_primary_Left()

    def deleteAdvanceLowerUserForSearch(self, indexs):
        a_data = Store.read_json()
        activeAdvanceLowerUserList = a_data[LOWERUSERADVANCED][indexs[-1]
                                                               ][indexs[-2]][indexs[-3]]
        activeAdvanceLowerUserList["Roll"] = self.leftStatusRollNumberForAdvanceLower(
        )
        Store.update_json_for_left(
            activeAdvanceLowerUserList, LOWERUSERADVANCED)
        del a_data[LOWERUSERADVANCED][indexs[-1]][indexs[-2]][indexs[-3]]
        Store.write_json(a_data)
        self.connectIntoNameSearch()
        self.connect_lower_advanced()
        self.connect_lower_advanced_left()
        self.data_frame()

    def deleteInterUserLeftForSearch(self, index):
        l_data = Store.read_json_for_left()
        del l_data[INTERUSER][index]
        Store.write_json_for_left(l_data)
        self.connectIntoNameSearch()
        self.connect_inter_left()

    def deleteLowerUserLeftForSearch(self, index):
        l_data = Store.read_json_for_left()
        del l_data[LOWERUSERORDINARY][index]
        Store.write_json_for_left(l_data)
        self.connectIntoNameSearch()
        self.connect_lower_odrinary_left()

    def deleteAdvanceLowerLeftForSearch(self, index):
        l_data = Store.read_json_for_left()
        del l_data[LOWERUSERADVANCED][index]
        Store.write_json_for_left(l_data)
        self.connectIntoNameSearch()
        self.connect_lower_advanced_left()

    # Connect Roll Search
    def connectIntoRollSearch(self):

        # CLEAR THE ROLL LEST
        def rolClear():
            ROLL_SEARCH_INTER_ACTIVE.clear()
            ROLL_SEARCH_INTER_LEFT.clear()
            ROLL_SEARCH_LOWER_ACTIVE.clear()
            ROLL_SEARCH_LOWER_LEFT.clear()
            ROLL_SEARCH_ADVANCED_LOWER.clear()
            ROLL_SEARCH_ADVANCED_LOWER_LEFT.clear()
            ROLL_SEARCH_PRIMARY_LOWER.clear()
            ROLL_SEARCH_PRIMARY_LOWER_LEFT.clear()

        # CLEAR THE NAME LIST
        def clear():
            NAME_SEARCH_INTER_ACTIVE.clear()
            NAME_SEARCH_LOWER_ACTIVE.clear()
            NAME_SEARCH_INTER_LEFT.clear()
            NAME_SEARCH_LOWER_LEFT.clear()
            ROLL_SEARCH_ADVANCED_LOWER.clear()
            ROLL_SEARCH_ADVANCED_LOWER_LEFT.clear()
            ROLL_SEARCH_PRIMARY_LOWER.clear()
            ROLL_SEARCH_PRIMARY_LOWER_LEFT.clear()

        clearThread = Thread(target=clear)
        clearThread.start()
        clearThread.join()

        rollClear = Thread(target=rolClear)
        rollClear.start()
        rollClear.join()

        searchThread = Thread(target=self.rollSearch)
        searchThread.start()
        searchThread.join()

        # Run the Base Search Frame
        self.main_frame_for_base_search()

        if ROLL_SEARCH_INTER_ACTIVE == [] and ROLL_SEARCH_INTER_LEFT == [] and ROLL_SEARCH_LOWER_ACTIVE == [] and ROLL_SEARCH_LOWER_LEFT == [] and ROLL_SEARCH_ADVANCED_LOWER == [] and ROLL_SEARCH_ADVANCED_LOWER == [] and ROLL_SEARCH_ADVANCED_LOWER_LEFT == [] and ROLL_SEARCH_PRIMARY_LOWER == [] and ROLL_SEARCH_PRIMARY_LOWER_LEFT == []:
            self.not_found_frame()

        if ROLL_SEARCH_INTER_ACTIVE != []:
            __target = self.decryptForInter(ROLL_SEARCH_INTER_ACTIVE[-1])
            self.inti_frame_for_search_resalt(f"""
				<html>
					<head/>
					<body>
						<p align=\"center\"> <b>TEACHERS TYPE</b> </p>
						<br>
						<p>
							<pre><spen>Roll-Number      :   {__target[0]}</spen></pre>
							<pre><spen>Name             :   {__target[1]}</spen></pre>
							<pre><spen>Address          :   <address>{__target[2]}</address></spen></pre>
							<pre><spen>Subject          :   {__target[3]}</spen></pre>
							<pre><spen>E-Mail           :   {__target[4]}</spen></pre>
							<pre><spen>Contact-Number   :   {__target[5]}</spen></pre>
							<pre><spen>Level            :   {__target[6]}</spen></pre>
							<pre><spen>Gender           :   {__target[7]}</spen></pre>
						</p>
					</body>
				</html>
			""")
            self.btn_roll_deleter.clicked.connect(
                lambda: self.deleteInterRollSearch(ROLL_SEARCH_INTER_ACTIVE[-1]))

        if ROLL_SEARCH_LOWER_ACTIVE != []:
            __target = self.decryptForLower(
                ROLL_SEARCH_LOWER_ACTIVE[-1][0], ROLL_SEARCH_LOWER_ACTIVE[-1][-1])
            self.inti_frame_for_search_resalt(f"""
                <html>
                    <head/>
                    <body>
                        <p align=\"center\"> <b>STUDENTS TYPE</b> </p>
                        <br>
                        <p>
                            <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                            <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                            <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                            <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                            <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                            <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                            <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                            <pre><spen>Level                :   {__target[7]}</spen></pre>
                            <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                            <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                            <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                            <pre><spen>Gender               :   {__target[11]}</spen></pre>
                        </p>
                        <br>
                    </body>
                </html>
			""")
            self.btn_roll_deleter.clicked.connect(
                lambda: self.deleteLowerRollSearch(ROLL_SEARCH_LOWER_ACTIVE[-1]))

        if ROLL_SEARCH_ADVANCED_LOWER != []:
            __target = self.decryptForAdvanceLowerLeft(
                ROLL_SEARCH_ADVANCED_LOWER[-1][0], ROLL_SEARCH_ADVANCED_LOWER[-1][-1], ROLL_SEARCH_ADVANCED_LOWER[-1][-2])
            self.inti_frame_for_search_resalt(f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>ADVANCED STUDENTS TYPE</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                                <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                                <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                                <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                                <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                                <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                                <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                                <pre><spen>Level                :   {__target[7]}</spen></pre>
                                <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                                <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                                <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                                <pre><spen>Gender               :   {__target[11]}</spen></pre>
                                <pre><spen>Stream               :   {__target[12].title()}</spen></pre>
                            </p>
                            <br>
                        </body>
                    </html>
            """)
            self.btn_roll_deleter.clicked.connect(
                lambda: self.deleteAdvancedLowerRollSearch(ROLL_SEARCH_ADVANCED_LOWER[-1]))

        if ROLL_SEARCH_ADVANCED_LOWER_LEFT != []:
            __target = self.decryptForAdvanceLowerLeft(
                ROLL_SEARCH_ADVANCED_LOWER_LEFT[-1], None, None)
            self.inti_frame_for_search_resalt(f"""
                    <html>
                        <head/>
                        <body>
                            <p align=\"center\"> <b>ADVANCED STUDENTS TYPE | Recycle Bin</b> </p>
                            <br>
                            <p>
                                <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                                <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                                <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                                <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                                <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                                <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                                <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                                <pre><spen>Level                :   {__target[7]}</spen></pre>
                                <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                                <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                                <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                                <pre><spen>Gender               :   {__target[11]}</spen></pre>
                                <pre><spen>Stream               :   {__target[12].title()}</spen></pre>
                            </p>
                            <br>
                        </body>
                    </html>
            """)
            self.btn_roll_deleter.clicked.connect(
                lambda: self.deleteAdvancedLowerRollSearchLeft(ROLL_SEARCH_ADVANCED_LOWER_LEFT[-1]))

        if ROLL_SEARCH_INTER_LEFT != []:
            __target = self.decryptForInterLeft(ROLL_SEARCH_INTER_LEFT[-1])
            self.inti_frame_for_search_resalt(f"""
				<html>
					<head/>
					<body>
						<p align=\"center\"> <b>TEACHERS TYPE | Recycle Bin</b> </p>
						<br>
						<p>
							<pre><spen>Roll-Number      :   {__target[0]}</spen></pre>
							<pre><spen>Name             :   {__target[1]}</spen></pre>
							<pre><spen>Address          :   <address>{__target[2]}</address></spen></pre>
							<pre><spen>Subject          :   {__target[3]}</spen></pre>
							<pre><spen>E-Mail           :   {__target[4]}</spen></pre>
							<pre><spen>Contact-Number   :   {__target[5]}</spen></pre>
							<pre><spen>Level            :   {__target[6]}</spen></pre>
							<pre><spen>Gender           :   {__target[7]}</spen></pre>
						</p>
					</body>
				</html>
			""")
            self.btn_roll_deleter.clicked.connect(
                lambda: self.deleteInterLeftRollSearch(ROLL_SEARCH_INTER_LEFT[-1]))
            self.label_info_user_search.setText("""
                <html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>
            """)

        if ROLL_SEARCH_LOWER_LEFT != []:
            __target = self.decryptForLowerLeft(ROLL_SEARCH_LOWER_LEFT[-1])
            self.inti_frame_for_search_resalt(f"""
                <html>
                    <head/>
                    <body>
                        <p align=\"center\"> <b>STUDENTS TYPE | Recycle Bin</b> </p>
                        <br>
                        <p>
                            <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                            <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                            <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                            <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                            <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                            <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                            <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                            <pre><spen>Level                :   {__target[7]}</spen></pre>
                            <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                            <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                            <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                            <pre><spen>Gender               :   {__target[11]}</spen></pre>
                        </p>
                        <br>
                    </body>
                </html>
			""")
            self.btn_roll_deleter.clicked.connect(
                lambda: self.deleteLowerLeftRollSearch(ROLL_SEARCH_LOWER_LEFT[-1]))
            self.label_info_user_search.setText("""
                <html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>
            """)

        if ROLL_SEARCH_PRIMARY_LOWER != []:
            __target = self.decryptForLowerPrimary(
                ROLL_SEARCH_PRIMARY_LOWER[-1][0], ROLL_SEARCH_PRIMARY_LOWER[-1][-1])
            self.inti_frame_for_search_resalt(f"""
                <html>
                    <head/>
                    <body>
                        <p align=\"center\"> <b>STUDENTS TYPE</b> </p>
                        <br>
                        <p>
                            <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                            <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                            <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                            <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                            <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                            <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                            <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                            <pre><spen>Level                :   {__target[7]}</spen></pre>
                            <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                            <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                            <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                            <pre><spen>Gender               :   {__target[11]}</spen></pre>
                        </p>
                        <br>
                    </body>
                </html>
			""")
            self.btn_roll_deleter.clicked.connect(
                lambda: self.deleteLowerRollSearchPrimary(ROLL_SEARCH_PRIMARY_LOWER[-1][0], ROLL_SEARCH_PRIMARY_LOWER[-1][-1]))
            self.label_info_user_search.setText("""
                <html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>
            """)

        if ROLL_SEARCH_PRIMARY_LOWER_LEFT != []:
            __target = self.decryptForLowerPrimaryLeft(
                ROLL_SEARCH_PRIMARY_LOWER_LEFT[-1])
            self.inti_frame_for_search_resalt(f"""
                <html>
                    <head/>
                    <body>
                        <p align=\"center\"> <b>STUDENTS TYPE | Recycle Bin</b> </p>
                        <br>
                        <p>
                            <pre><spen>Roll-Number          :   {__target[0]}</spen></pre>
                            <pre><spen>Name                 :   {__target[1].title()}</spen></pre>
                            <pre><spen>Address              :   <address>{__target[2].title()}</address></spen></pre>
                            <pre><spen>Father-Name          :   {__target[3].title()}</spen></pre>
                            <pre><spen>Mather-Name          :   {__target[4].title()}</spen></pre>
                            <pre><spen>Contact-Number       :   {__target[5]}</spen></pre>
                            <pre><spen>Registration-Number  :   {__target[6]}</spen></pre>
                            <pre><spen>Level                :   {__target[7]}</spen></pre>
                            <pre><spen>E-Mail               :   {__target[8]}</spen></pre>
                            <pre><spen>Religion             :   {__target[9].title()}</spen></pre>
                            <pre><spen>Date-Of-Birth        :   {__target[10]}</spen></pre>
                            <pre><spen>Gender               :   {__target[11]}</spen></pre>
                        </p>
                        <br>
                    </body>
                </html>
			""")
            self.btn_roll_deleter.clicked.connect(
                lambda: self.deleteLowerLeftRollSearchPrimary(ROLL_SEARCH_PRIMARY_LOWER_LEFT[-1]))
            self.label_info_user_search.setText("""
                <html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>
            """)

    def deleteLowerLeftRollSearchPrimary(self, index):
        l_data = Store.read_json_for_left()
        del l_data[LOWERUSERPRIMARY][index]
        Store.write_json_for_left(l_data)
        self.frame_resalt.deleteLater()
        self.actionsOfFrame = False
        self.connect_lower_primary_Left()

    def deleteLowerRollSearchPrimary(self, level, index):
        a_data = Store.read_json()
        activeLowerRollList = a_data[LOWERUSERPRIMARY][level][index]
        activeLowerRollList["Roll"] = self.leftStatusRollNumberForPrimaryLower()
        Store.update_json_for_left(activeLowerRollList, LOWERUSERPRIMARY)
        del a_data[LOWERUSERPRIMARY][level][index]
        Store.write_json(a_data)
        self.frame_resalt.deleteLater()
        self.actionsOfFrame = False
        self.data_frame()
        self.connect_lower_primary()
        self.connect_lower_primary_Left()

    def deleteLowerLeftRollSearch(self, index):
        l_data = Store.read_json_for_left()
        del l_data[LOWERUSERORDINARY][index]
        Store.write_json_for_left(l_data)
        self.frame_resalt.deleteLater()
        self.actionsOfFrame = False
        self.connect_lower_odrinary_left()

    def deleteAdvancedLowerRollSearch(self, index):
        a_data = Store.read_json()
        activeLowerRollList = a_data[LOWERUSERADVANCED][index[-1]
                                                        ][index[-2]][index[-3]]
        activeLowerRollList["Roll"] = self.leftStatusRollNumberForAdvanceLower()
        Store.update_json_for_left(activeLowerRollList, LOWERUSERADVANCED)
        del a_data[LOWERUSERADVANCED][index[-1]][index[-2]][index[-3]]
        Store.write_json(a_data)
        self.frame_resalt.deleteLater()
        self.actionsOfFrame = False
        self.data_frame()
        self.connect_lower_advanced()
        self.connect_lower_advanced_left()

    def deleteAdvancedLowerRollSearchLeft(self, index):
        l_data = Store.read_json_for_left()
        del l_data[LOWERUSERADVANCED][index]
        Store.write_json_for_left(l_data)
        self.frame_resalt.deleteLater()
        self.actionsOfFrame = False
        self.connect_lower_advanced_left()

    def deleteInterLeftRollSearch(self, index):
        l_data = Store.read_json_for_left()
        del l_data[INTERUSER][index]
        Store.write_json_for_left(l_data)
        self.frame_resalt.deleteLater()
        self.actionsOfFrame = False
        self.connect_inter_left()

    def deleteLowerRollSearch(self, index):
        a_data = Store.read_json()
        activeLowerRollList = a_data[LOWERUSERORDINARY][index[-2]][index[-1]]
        activeLowerRollList["Roll"] = self.leftStatusRollNumberForLower()
        Store.update_json_for_left(activeLowerRollList, LOWERUSERORDINARY)
        del a_data[LOWERUSERORDINARY][index[-2]][index[-1]]
        Store.write_json(a_data)
        self.frame_resalt.deleteLater()
        self.actionsOfFrame = False
        self.connect_lower_odrinary()
        self.connect_lower_odrinary_left()
        self.data_frame()

    def deleteInterRollSearch(self, index):
        a_data = Store.read_json()
        activeInterRollList = a_data[INTERUSER][index]
        activeInterRollList["Roll"] = self.leftStatusRollNumberForInter()
        Store.update_json_for_left(activeInterRollList, INTERUSER)
        del a_data[INTERUSER][index]
        Store.write_json(a_data)
        self.frame_resalt.deleteLater()
        self.actionsOfFrame = False
        self.connect_inter()
        self.connect_inter_left()
        self.data_frame()

    # Search Name
    def searchName(self):
        __nameOfUserEnterIt = self.ui.lineEdit_nameSearch.text()
        self.ui.lineEdit_rollSearch.clear()
        if __nameOfUserEnterIt != "":
            active_data = Store.read_json()
            left_data = Store.read_json_for_left()

            listOfInter_A = active_data[INTERUSER]
            listOfLower_A = [name for name in active_data[LOWERUSERORDINARY]]

            listOfLower_Advance_levels = [
                name_level for name_level in active_data[LOWERUSERADVANCED]]
            listOfLower_Advance_streams = [
                name for name in active_data[LOWERUSERADVANCED][listOfLower_Advance_levels[0]]]

            listOfInter_L = left_data[INTERUSER]
            listOfLower_L = left_data[LOWERUSERORDINARY]
            listOfAdvanceLower_L = left_data[LOWERUSERADVANCED]

            listOfLowerPrimary_a = active_data[LOWERUSERPRIMARY]
            listOfLowerPrimary_l = left_data[LOWERUSERPRIMARY]
            listOfLowerPrimaryLevels = [
                name for name in active_data[LOWERUSERPRIMARY]]

            # NAME SEARCH FOR ACTIVE INTER
            for index in range(len(listOfInter_A)):
                __name = secure.decrypt(
                    listOfInter_A[index]["Name"][-2], listOfInter_A[index]["Name"][-1])
                if self.nameSearchAlgorithm(__name, __nameOfUserEnterIt) >= 60:
                    NAME_SEARCH_INTER_ACTIVE.append(index)

            # NAME SEARCH FOR ADVANCE LOWER
            for level in listOfLower_Advance_levels:
                for stream in listOfLower_Advance_streams:
                    for index in range(len(active_data[LOWERUSERADVANCED][level][stream])):
                        __name = secure.decrypt(
                            active_data[LOWERUSERADVANCED][level][stream][index]["Name"][-2], active_data[LOWERUSERADVANCED][level][stream][index]["Name"][-1])
                        if self.nameSearchAlgorithm(__name, __nameOfUserEnterIt) >= 60:
                            NAME_SEARCH_ADVANCE_LOWER.append(
                                (index, stream, level))

            # NAME SEARCH FOR ADVANCESD LOWER LEFT
            for index in range(len(listOfAdvanceLower_L)):
                __name = secure.decrypt(
                    listOfAdvanceLower_L[index]["Name"][-2], listOfAdvanceLower_L[index]["Name"][-1])
                if self.nameSearchAlgorithm(__name, __nameOfUserEnterIt) >= 60:
                    NAME_SEARCH_ADVANCE_LOWER_LEFT.append(index)

            # NAME SEARCH FOR ACTIVE LOWER
            for level in listOfLower_A:
                for index in range(len(active_data[LOWERUSERORDINARY][level])):
                    __name = secure.decrypt(
                        active_data[LOWERUSERORDINARY][level][index]["Name"][-2], active_data[LOWERUSERORDINARY][level][index]["Name"][-1])
                    if self.nameSearchAlgorithm(__name, __nameOfUserEnterIt) >= 60:
                        NAME_SEARCH_LOWER_ACTIVE.append((index, level))

            # NAME SEARCH FOR ACTIVE LOWER PRIMARY
            for level in listOfLowerPrimaryLevels:
                for index in range(len(listOfLowerPrimary_a[level])):
                    __name = secure.decrypt(
                        listOfLowerPrimary_a[level][index]["Name"][-2], listOfLowerPrimary_a[level][index]["Name"][-1])
                    if self.nameSearchAlgorithm(__name, __nameOfUserEnterIt) >= 60:
                        NAME_SEARCH_PRIMARY_LOWER.append((index, level))

            # NAME SEARCH FOR LEFT LOWER PRIMARY
            for index in range(len(listOfLowerPrimary_l)):
                __name = secure.decrypt(
                    listOfLowerPrimary_l[index]["Name"][-2], listOfLowerPrimary_l[index]["Name"][-1])
                if self.nameSearchAlgorithm(__name, __nameOfUserEnterIt) >= 60:
                    NAME_SEARCH_PRIMARY_LOWER_LEFT.append(index)

            # NAME SEARCH FOR LEFT INTER
            for index in range(len(listOfInter_L)):
                __name = secure.decrypt(
                    listOfInter_L[index]["Name"][-2], listOfInter_L[index]["Name"][-1])
                if self.nameSearchAlgorithm(__name, __nameOfUserEnterIt) >= 60:
                    NAME_SEARCH_INTER_LEFT.append(index)

            # NAME SEARCH FOR LEFT LOWER
            for index in range(len(listOfLower_L)):
                __name = secure.decrypt(
                    listOfLower_L[index]["Name"][-2], listOfLower_L[index]["Name"][-1])
                if self.nameSearchAlgorithm(__name, __nameOfUserEnterIt) >= 60:
                    NAME_SEARCH_LOWER_LEFT.append(index)

    # Roll Search
    def rollSearch(self):
        self.ui.lineEdit_nameSearch.clear()
        __rollOfUserEnterIt = self.ui.lineEdit_rollSearch.text()

        if __rollOfUserEnterIt != "":

            active_data = Store.read_json()
            left_data = Store.read_json_for_left()

            listOfInterUser_A = active_data[INTERUSER]
            listOfLowerUser_A = active_data[LOWERUSERORDINARY]

            listOfInterUser_L = left_data[INTERUSER]
            listOfLowerUser_L = left_data[LOWERUSERORDINARY]

            listOfAdvancedLower_active = active_data[LOWERUSERADVANCED]
            listOfAdvancedLower_left = left_data[LOWERUSERADVANCED]

            ListOfAdvancedLowerLevels = [
                level for level in active_data[LOWERUSERADVANCED]]
            ListOfAdvancedLowerStreams = [
                stream for stream in active_data[LOWERUSERADVANCED][ListOfAdvancedLowerLevels[-1]]]

            listOfPrimaryLower_active = active_data[LOWERUSERPRIMARY]
            listOfPrimaryLower_left = left_data[LOWERUSERPRIMARY]

            if __rollOfUserEnterIt[0] == "I":
                if __rollOfUserEnterIt.split("|")[-1] == "LEFT":
                    Thread(target=self.rollSearchAlgorithmConnecter, args=[
                        listOfInterUser_L, __rollOfUserEnterIt, 'inter_l']).start()
                else:
                    Thread(target=self.rollSearchAlgorithmConnecter, args=[
                        listOfInterUser_A, __rollOfUserEnterIt, "inter_a"]).start()
            else:
                if __rollOfUserEnterIt.split("|")[-1] == "ORDINARY-LEFT":
                    Thread(target=self.rollSearchAlgorithmConnecter, args=[
                        listOfLowerUser_L, __rollOfUserEnterIt, "lower_l"]).start()
                elif __rollOfUserEnterIt.split("|")[-1] in ListOfAdvancedLowerStreams:
                    Thread(target=self.rollSearchAlgorithmConnecter, args=[
                        listOfAdvancedLower_active, __rollOfUserEnterIt, "adv_lower"]).start()
                elif __rollOfUserEnterIt.split("|")[-1] == "ADVANCE-LEFT":
                    Thread(target=self.rollSearchAlgorithmConnecter, args=[
                        listOfAdvancedLower_left, __rollOfUserEnterIt, "adv_lower_l"]).start()
                elif __rollOfUserEnterIt.split("|")[-1] == "PRIMARY-LEFT":
                    Thread(target=self.rollSearchAlgorithmConnecter, args=[
                        listOfPrimaryLower_left, __rollOfUserEnterIt, "pri_lower_l"
                    ]).start()
                elif int(__rollOfUserEnterIt.split("|")[0].split("L")[-1]) in list(range(1, 5)):
                    Thread(target=self.rollSearchAlgorithmConnecter, args=[
                        listOfPrimaryLower_active, __rollOfUserEnterIt, "pri_lower_a"
                    ]).start()
                else:
                    Thread(target=self.rollSearchAlgorithmConnecter, args=[
                        listOfLowerUser_A, __rollOfUserEnterIt, "lower_a"]).start()

    # Name Search Algorithm

    def nameSearchAlgorithm(self, matching_name, target_name):
        rows = len(matching_name) + 1
        cols = len(target_name) + 1
        distance = np.zeros((rows, cols), dtype=int)

        for i in range(1, rows):
            for k in range(1, cols):
                distance[i][0] = i
                distance[0][k] = k

        for col in range(1, cols):
            for row in range(1, rows):
                if matching_name[row-1] == target_name[col-1]:
                    cost = 0
                else:
                    cost = 2

                distance[row][col] = min(distance[row-1][col]+1,
                                         distance[row][col-1] + 1,
                                         distance[row-1][col-1] + cost)

        Ratio = ((len(matching_name)+len(target_name)) -
                 distance[row][col]) / (len(matching_name)+len(target_name)) * 100
        return Ratio

    # Roll Search Algorithm Connecter
    def rollSearchAlgorithmConnecter(self, array, target_roll, userType):

        try:

            # ROLL SEARCH FOR INTER
            if userType == "inter_a":
                index = self.rollSearchAlgorithm(array, target_roll)
                if index != None:
                    ROLL_SEARCH_INTER_ACTIVE.append(index)

            # ROLL SEARCH FOR LOWER
            elif userType == "lower_a":
                level = [levelName for levelName in array]
                for levelN in level:
                    lnum = levelN.split("Level -")[-1]
                    if int(lnum) == int(target_roll.split("LOWER")[-1].split("L")[-1]):
                        index = self.rollSearchAlgorithm(
                            array[levelN], target_roll)
                        if index != None:
                            ROLL_SEARCH_LOWER_ACTIVE.append((levelN, index))

            # Roll SEARCH FOR ADVANCED LOWER
            elif userType == "adv_lower":
                ListOfAdvancedLowerLevels = [level for level in array]
                ListOfAdvancedLowerStreams = [
                    stream for stream in array[ListOfAdvancedLowerLevels[-1]]]
                for level in ListOfAdvancedLowerLevels:
                    for stream in ListOfAdvancedLowerStreams:
                        if stream == target_roll.split("|")[-1]:
                            index = self.rollSearchAlgorithm(
                                array[level][stream], target_roll)
                            if index != None:
                                ROLL_SEARCH_ADVANCED_LOWER.append(
                                    (index, stream, level))

            # Roll SEARCH FOR ADVANCED LOWER -- LEFT
            elif userType == "adv_lower_l":
                index = self.rollSearchAlgorithm(array, target_roll)
                if index != None:
                    ROLL_SEARCH_ADVANCED_LOWER_LEFT.append(index)

            # ROLL SEARCH FOR INTER -- LEFT
            elif userType == "inter_l":
                index = self.rollSearchAlgorithm(array, target_roll)
                if index != None:
                    ROLL_SEARCH_INTER_LEFT.append(index)

            elif userType == "pri_lower_a":
                level = [levelName for levelName in array]
                for levelN in level:
                    lnum = levelN.split("Level -")[-1]
                    if int(lnum) == int(target_roll.split("LOWER")[-1].split("L")[-1]):
                        index = self.rollSearchAlgorithm(
                            array[levelN], target_roll)
                        if index != None:
                            ROLL_SEARCH_PRIMARY_LOWER.append((levelN, index))

            elif userType == "pri_lower_l":
                index = self.rollSearchAlgorithm(array, target_roll)
                if index != None:
                    ROLL_SEARCH_PRIMARY_LOWER_LEFT.append(index)

            # ROLL SEARCH FOR LOWER -- LEFT
            else:
                index = self.rollSearchAlgorithm(array, target_roll)
                if index != None:
                    ROLL_SEARCH_LOWER_LEFT.append(index)

        except ValueError as er:
            pass

    # Roll Search Algorithm
    def rollSearchAlgorithm(self, array, target):
        low = 0
        high = len(array) - 1

        while low <= high:
            mid = low + (high - low) // 2
            res = array[mid]["Roll"] == target
            if res == 1:
                return mid
            elif res < 1:
                low = mid + 1
            else:
                high = mid - 1

        return None

    # ANALYICS FOR DATA
    def data_frame(self):

        data = Store.read_json()

        # Inter Data Sets

        inter_data_info_list = []

        def inter_getter():
            if data[INTERUSER] != []:
                df_inter = pd.DataFrame(data[INTERUSER])
                x = np.array(["", 'A', 'B', "C", "D", "E", "F"])
                values_y = np.array([0, df_inter.shape[0] - df_inter["Subject"].isnull().sum(), df_inter["Subject"].isnull().sum(), df_inter.shape[0] -
                                     df_inter["E-Mail"].isnull().sum(), df_inter["E-Mail"].isnull().sum(), df_inter.shape[0] - df_inter["Level"].isnull().sum(), df_inter["Level"].isnull().sum()])
                inter_data_info_list.append((x, values_y, df_inter))

        getter = Thread(target=inter_getter)
        getter.start()
        getter.join()

        if inter_data_info_list != []:
            max_n = 0
            for n in inter_data_info_list[-1][-2]:
                if max_n <= n:
                    max_n = n
            self.analytics_inter([0, max_n + 1], [0, 7],
                                 inter_data_info_list[-1][-3], inter_data_info_list[-1][-2], .3, '#00ff7f', inter_data_info_list[-1][-1].shape[0])
            inter_data_info_list.clear()

        else:
            self.analytics_inter([0, 4], [0, 7], ["", "A", "B", "C", "D", "E", "F"], [
                                 0, 0, 0, 0, 0, 0, 0], .3, '#00ff7f', 0)

        # Primary Lower Data Set
        lower_primary_data_info_list = []

        def primary_getter():
            df = data[LOWERUSERPRIMARY]
            level_1 = pd.DataFrame(df["Level - 01"])
            level_2 = pd.DataFrame(df["Level - 02"])
            level_3 = pd.DataFrame(df["Level - 03"])
            level_4 = pd.DataFrame(df["Level - 04"])
            level_5 = pd.DataFrame(df["Level - 05"])

            tot_lower = level_1.shape[0] + level_2.shape[0] + \
                level_3.shape[0] + level_4.shape[0] + level_5.shape[0]

            x = np.array(["", "A", "B", "C", "D", "E"])
            y = np.array([0, level_1.shape[0], level_2.shape[0],
                         level_3.shape[0], level_4.shape[0], level_5.shape[0]])

            lower_primary_data_info_list.append((tot_lower, x, y))

        getter_p = Thread(target=primary_getter)
        getter_p.start()
        getter_p.join()

        print(lower_primary_data_info_list)

        if lower_primary_data_info_list != []:
            max_n = 0
            for n in lower_primary_data_info_list[-1][-1]:
                if max_n <= n:
                    max_n = n
            self.analytics_lower_primary([0, max_n + 1],
                                         [0, 6], lower_primary_data_info_list[-1][-2], lower_primary_data_info_list[-1][-1], .3, '#00ff7f', lower_primary_data_info_list[-1][-3])
            lower_primary_data_info_list.clear()

        # Advanced Lower More Data Sets
        advanced_lower_data_info_list_more = []

        def advanced_getter_12():
            df = data[LOWERUSERADVANCED]
            level = "Level - 12"

            mathematics = pd.DataFrame(df[level]["Mathematics"])
            science = pd.DataFrame(df[level]["Science"])
            engin_tech = pd.DataFrame(df[level]["Engineering-Technology"])
            bio_tech = pd.DataFrame(df[level]["Bio-Technology"])
            commerce = pd.DataFrame(df[level]["Commerce"])
            art = pd.DataFrame(df[level]["Art"])

            tot_lower = mathematics.shape[0] + science.shape[0] + \
                engin_tech.shape[0] + bio_tech.shape[0] + \
                commerce.shape[0] + art.shape[0]

            x = np.array(["", "A", "B", "C", "D", "E", "F"])
            y = np.array([0, mathematics.shape[0], science.shape[0], engin_tech.shape[0],
                         bio_tech.shape[0], commerce.shape[0], art.shape[0]])
            advanced_lower_data_info_list_more.append((tot_lower, x, y))

        getter_am_12 = Thread(target=advanced_getter_12)
        getter_am_12.start()
        getter_am_12.join()

        print(advanced_lower_data_info_list_more)

        if advanced_lower_data_info_list_more != []:
            max_n = 0
            for n in advanced_lower_data_info_list_more[-1][-1]:
                if max_n <= n:
                    max_n = n
            self.analytics_lower_Advanced_level_12([0, max_n + 1],
                                                   [0, 7], advanced_lower_data_info_list_more[-1][-2], advanced_lower_data_info_list_more[-1][-1], .3, '#00ff7f', advanced_lower_data_info_list_more[-1][-3])
            advanced_lower_data_info_list_more.clear()

        # Advanced Lower More Data Sets
        advanced_lower_data_info_list_more_13 = []

        def advanced_getter_13():
            df = data[LOWERUSERADVANCED]
            level = "Level - 13"

            mathematics = pd.DataFrame(df[level]["Mathematics"])
            science = pd.DataFrame(df[level]["Science"])
            engin_tech = pd.DataFrame(df[level]["Engineering-Technology"])
            bio_tech = pd.DataFrame(df[level]["Bio-Technology"])
            commerce = pd.DataFrame(df[level]["Commerce"])
            art = pd.DataFrame(df[level]["Art"])

            tot_lower = mathematics.shape[0] + science.shape[0] + \
                engin_tech.shape[0] + bio_tech.shape[0] + \
                commerce.shape[0] + art.shape[0]

            x = np.array(["", "A", "B", "C", "D", "E", "F"])
            y = np.array([0, mathematics.shape[0], science.shape[0], engin_tech.shape[0],
                         bio_tech.shape[0], commerce.shape[0], art.shape[0]])
            advanced_lower_data_info_list_more_13.append((tot_lower, x, y))

        getter_am_13 = Thread(target=advanced_getter_13)
        getter_am_13.start()
        getter_am_13.join()

        print(advanced_lower_data_info_list_more_13)

        if advanced_lower_data_info_list_more_13 != []:
            max_n = 0
            for n in advanced_lower_data_info_list_more_13[-1][-1]:
                if max_n <= n:
                    max_n = n
            self.analytics_lower_Advanced_level_13([0, max_n + 1],
                                                   [0, 7], advanced_lower_data_info_list_more_13[-1][-2], advanced_lower_data_info_list_more_13[-1][-1], .3, '#00ff7f', advanced_lower_data_info_list_more_13[-1][-3])
            advanced_lower_data_info_list_more_13.clear()

        # Advanced Lower Data Sets
        advanced_lower_data_info_list = []

        def advanced_getter():
            df = data[LOWERUSERADVANCED]

            strems_list = [name for name in df["Level - 12"]]

            level_12_count_list = 0
            for stream in strems_list:
                level_12_count_list += len(df["Level - 12"][stream])

            level_13_count_list = 0
            for stream in strems_list:
                level_13_count_list += len(df["Level - 13"][stream])

            tot_advanced = level_12_count_list + level_13_count_list

            x = np.array(["", "Level - 12", "Level - 13"])
            y = np.array([0, level_12_count_list, level_13_count_list])

            advanced_lower_data_info_list.append((tot_advanced, x, y))

        getter_a = Thread(target=advanced_getter)
        getter_a.start()
        getter_a.join()
        if advanced_lower_data_info_list != []:
            max_number = 0
            for n in advanced_lower_data_info_list[-1][-1]:
                if max_number <= n:
                    max_number = n
            self.analytics_lower_Advanced([0, max_number + 1],
                                          [0, 3], advanced_lower_data_info_list[-1][-2], advanced_lower_data_info_list[-1][-1], .4, '#00ff7f', advanced_lower_data_info_list[-1][-3])
            advanced_lower_data_info_list.clear()

        # Lower Data Sets
        lower_data_info_list = []

        def lower_getter():
            df_lower = data[LOWERUSERORDINARY]
            level_6 = pd.DataFrame(df_lower["Level - 06"])
            level_7 = pd.DataFrame(df_lower["Level - 07"])
            level_8 = pd.DataFrame(df_lower["Level - 08"])
            level_9 = pd.DataFrame(df_lower["Level - 09"])
            level_10 = pd.DataFrame(df_lower["Level - 10"])
            level_11 = pd.DataFrame(df_lower["Level - 11"])

            tot_lower = level_6.shape[0] + level_7.shape[0] + level_8.shape[0] + \
                level_9.shape[0] + level_10.shape[0] + level_11.shape[0]

            x = np.array(["", "A", "B", "C", "D", "E",
                          "F"])
            values_y = np.array([0, level_6.shape[0], level_7.shape[0], level_8.shape[0],
                                 level_9.shape[0], level_10.shape[0], level_11.shape[0]])
            lower_data_info_list.append((tot_lower, x, values_y))

        getter_l = Thread(target=lower_getter)
        getter_l.start()
        getter_l.join()
        if lower_data_info_list != []:
            max_n = 0
            for n in lower_data_info_list[-1][-1]:
                if max_n <= n:
                    max_n = n
            self.analytics_lower([0, max_n + 1],
                                 [0, 7], lower_data_info_list[-1][-2], lower_data_info_list[-1][-1], .3, '#00ff7f', lower_data_info_list[-1][-3])
            lower_data_info_list.clear()

    # ANALYTICS LOWER ADVANCED MORE LEVEL 12
    def analytics_lower_Advanced_level_12(self, xlabel_content: list, ylabel_content: list, content_pos: list, content_value: list, width, color: str, tot_lower: int):

        if self.barChart_active_lower_ad_12 != True:

            # Bar Chart Frame
            self.frame_barChart_advan_12 = QFrame(
                self.ui.frame_advanced_level_12)
            self.frame_barChart_advan_12.setObjectName(
                "frame_barChart_advan_12")
            self.frame_barChart_advan_12.setStyleSheet("QFrame{\n"
                                                       "background-color: none;\n"
                                                       "color: #fff;\n"
                                                       "border: 0px solid;\n"
                                                       "border-radius: 10px;\n"
                                                       "};\n"
                                                       )
            self.frame_barChart_advan_12.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_advan_12.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_advan_12)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas_advan_12 = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas_advan_12)
            self.ui.frame_advanced_level_12_layout.addWidget(
                self.frame_barChart_advan_12)

            # Inforemation Frame
            self.frame_inforemation_advan_12 = QFrame(
                self.ui.frame_advanced_level_12)
            self.frame_inforemation_advan_12.setObjectName(
                "frame_inforemation_advan_12")
            self.frame_inforemation_advan_12.setMaximumSize(QSize(200, 300))
            self.frame_inforemation_advan_12.setMinimumSize(QSize(200, 300))
            self.frame_inforemation_advan_12.setStyleSheet("QFrame{\n"
                                                           "background-color: #282934;\n"
                                                           "color: #fff;\n"
                                                           "border: 0px solid;\n"
                                                           "border-radius: 10px;\n"
                                                           "};\n"
                                                           )
            self.frame_inforemation_advan_12.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_advan_12.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_advan_12)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_advan_12)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - (Mathematics)</pre>
                            <pre>B - (Science)</pre>
                            <pre>C - (Engineering-Technology)</pre>
                            <pre>D - (Bio-Technology)</pre>
                            <pre>E - (Commerce)</pre>
                            <pre>F - (Art)</pre>
                            <br>
                            <hr/>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.ui.frame_advanced_level_12_layout.addWidget(
                self.frame_inforemation_advan_12, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax_advan_12 = self.canvas_advan_12.figure.subplots()
            self.ax_advan_12.set_facecolor('#1a1b22')
            self.ax_advan_12.set_alpha(.5)
            self.ax_advan_12.plot(markeredgecolor='#fff')

            self.ax_advan_12.set_xlabel('Type of Students')
            self.ax_advan_12.set_ylabel('Number of Students')

            self.ax_advan_12.spines['left'].set_color('white')
            self.ax_advan_12.spines['top'].set_color('white')
            self.ax_advan_12.spines['bottom'].set_color('white')
            self.ax_advan_12.spines['right'].set_color('white')

            self.ax_advan_12.yaxis.label.set_color('white')
            self.ax_advan_12.xaxis.label.set_color('white')

            self.ax_advan_12.tick_params(colors='white', which='both')
            self.ax_advan_12.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax_advan_12.set_ylim(xlabel_content)

            # X label
            self.ax_advan_12.set_xlim(ylabel_content)

            self.ax_advan_12.bar(content_pos, content_value,
                                 width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax_advan_12.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas_advan_12.draw()

            self.barChart_active_lower_ad_12 = True

        else:
            self.frame_barChart_advan_12.deleteLater()
            self.frame_inforemation_advan_12.deleteLater()

            # Bar Chart Frame
            self.frame_barChart_advan_12 = QFrame(
                self.ui.frame_advanced_level_12)
            self.frame_barChart_advan_12.setObjectName(
                "frame_barChart_advan_12")
            self.frame_barChart_advan_12.setStyleSheet("QFrame{\n"
                                                       "background-color: none;\n"
                                                       "color: #fff;\n"
                                                       "border: 0px solid;\n"
                                                       "border-radius: 10px;\n"
                                                       "};\n"
                                                       )
            self.frame_barChart_advan_12.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_advan_12.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_advan_12)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas_advan_12 = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas_advan_12)
            self.ui.frame_advanced_level_12_layout.addWidget(
                self.frame_barChart_advan_12)

            # Inforemation Frame
            self.frame_inforemation_advan_12 = QFrame(
                self.ui.frame_advanced_level_12)
            self.frame_inforemation_advan_12.setObjectName(
                "frame_inforemation_advan_12")
            self.frame_inforemation_advan_12.setMaximumSize(QSize(200, 300))
            self.frame_inforemation_advan_12.setMinimumSize(QSize(200, 300))
            self.frame_inforemation_advan_12.setStyleSheet("QFrame{\n"
                                                           "background-color: #282934;\n"
                                                           "color: #fff;\n"
                                                           "border: 0px solid;\n"
                                                           "border-radius: 10px;\n"
                                                           "};\n"
                                                           )
            self.frame_inforemation_advan_12.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_advan_12.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_advan_12)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_advan_12)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - (Mathematics)</pre>
                            <pre>B - (Science)</pre>
                            <pre>C - (Engineering-Technology)</pre>
                            <pre>D - (Bio-Technology)</pre>
                            <pre>E - (Commerce)</pre>
                            <pre>F - (Art)</pre>
                            <br>
                            <hr/>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.ui.frame_advanced_level_12_layout.addWidget(
                self.frame_inforemation_advan_12, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax_advan_12 = self.canvas_advan_12.figure.subplots()
            self.ax_advan_12.set_facecolor('#1a1b22')
            self.ax_advan_12.set_alpha(.5)
            self.ax_advan_12.plot(markeredgecolor='#fff')

            self.ax_advan_12.set_xlabel('Type of Students')
            self.ax_advan_12.set_ylabel('Number of Students')

            self.ax_advan_12.spines['left'].set_color('white')
            self.ax_advan_12.spines['top'].set_color('white')
            self.ax_advan_12.spines['bottom'].set_color('white')
            self.ax_advan_12.spines['right'].set_color('white')

            self.ax_advan_12.yaxis.label.set_color('white')
            self.ax_advan_12.xaxis.label.set_color('white')

            self.ax_advan_12.tick_params(colors='white', which='both')
            self.ax_advan_12.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax_advan_12.set_ylim(xlabel_content)

            # X label
            self.ax_advan_12.set_xlim(ylabel_content)

            self.ax_advan_12.bar(content_pos, content_value,
                                 width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax_advan_12.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas_advan_12.draw()

    # ANALYTICS LOWER ADVANCED MORE LEVEL 13
    def analytics_lower_Advanced_level_13(self, xlabel_content: list, ylabel_content: list, content_pos: list, content_value: list, width, color: str, tot_lower: int):

        if self.barChart_active_lower_ad_13 != True:

            # Bar Chart Frame
            self.frame_barChart_advan_13 = QFrame(
                self.ui.frame_advanced_level_13)
            self.frame_barChart_advan_13.setObjectName(
                "frame_barChart_advan_13")
            self.frame_barChart_advan_13.setStyleSheet("QFrame{\n"
                                                       "background-color: none;\n"
                                                       "color: #fff;\n"
                                                       "border: 0px solid;\n"
                                                       "border-radius: 10px;\n"
                                                       "};\n"
                                                       )
            self.frame_barChart_advan_13.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_advan_13.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_advan_13)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas_advan_13 = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas_advan_13)
            self.ui.frame_advanced_level_13_layout.addWidget(
                self.frame_barChart_advan_13)

            # Inforemation Frame
            self.frame_inforemation_advan_13 = QFrame(
                self.ui.frame_advanced_level_13)
            self.frame_inforemation_advan_13.setObjectName(
                "frame_inforemation_advan_13")
            self.frame_inforemation_advan_13.setMaximumSize(QSize(200, 300))
            self.frame_inforemation_advan_13.setMinimumSize(QSize(200, 300))
            self.frame_inforemation_advan_13.setStyleSheet("QFrame{\n"
                                                           "background-color: #282934;\n"
                                                           "color: #fff;\n"
                                                           "border: 0px solid;\n"
                                                           "border-radius: 10px;\n"
                                                           "};\n"
                                                           )
            self.frame_inforemation_advan_13.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_advan_13.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_advan_13)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_advan_13)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - (Mathematics)</pre>
                            <pre>B - (Science)</pre>
                            <pre>C - (Engineering-Technology)</pre>
                            <pre>D - (Bio-Technology)</pre>
                            <pre>E - (Commerce)</pre>
                            <pre>F - (Art)</pre>
                            <br>
                            <hr/>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.ui.frame_advanced_level_13_layout.addWidget(
                self.frame_inforemation_advan_13, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax_advan_13 = self.canvas_advan_13.figure.subplots()
            self.ax_advan_13.set_facecolor('#1a1b22')
            self.ax_advan_13.set_alpha(.5)
            self.ax_advan_13.plot(markeredgecolor='#fff')

            self.ax_advan_13.set_xlabel('Type of Students')
            self.ax_advan_13.set_ylabel('Number of Students')

            self.ax_advan_13.spines['left'].set_color('white')
            self.ax_advan_13.spines['top'].set_color('white')
            self.ax_advan_13.spines['bottom'].set_color('white')
            self.ax_advan_13.spines['right'].set_color('white')

            self.ax_advan_13.yaxis.label.set_color('white')
            self.ax_advan_13.xaxis.label.set_color('white')

            self.ax_advan_13.tick_params(colors='white', which='both')
            self.ax_advan_13.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax_advan_13.set_ylim(xlabel_content)

            # X label
            self.ax_advan_13.set_xlim(ylabel_content)

            self.ax_advan_13.bar(content_pos, content_value,
                                 width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax_advan_13.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas_advan_13.draw()

            self.barChart_active_lower_ad_13 = True

        else:
            self.frame_barChart_advan_13.deleteLater()
            self.frame_inforemation_advan_13.deleteLater()

            # Bar Chart Frame
            self.frame_barChart_advan_13 = QFrame(
                self.ui.frame_advanced_level_13)
            self.frame_barChart_advan_13.setObjectName(
                "frame_barChart_advan_13")
            self.frame_barChart_advan_13.setStyleSheet("QFrame{\n"
                                                       "background-color: none;\n"
                                                       "color: #fff;\n"
                                                       "border: 0px solid;\n"
                                                       "border-radius: 10px;\n"
                                                       "};\n"
                                                       )
            self.frame_barChart_advan_13.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_advan_13.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_advan_13)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas_advan_13 = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas_advan_13)
            self.ui.frame_advanced_level_13_layout.addWidget(
                self.frame_barChart_advan_13)

            # Inforemation Frame
            self.frame_inforemation_advan_13 = QFrame(
                self.ui.frame_advanced_level_13)
            self.frame_inforemation_advan_13.setObjectName(
                "frame_inforemation_advan_13")
            self.frame_inforemation_advan_13.setMaximumSize(QSize(200, 300))
            self.frame_inforemation_advan_13.setMinimumSize(QSize(200, 300))
            self.frame_inforemation_advan_13.setStyleSheet("QFrame{\n"
                                                           "background-color: #282934;\n"
                                                           "color: #fff;\n"
                                                           "border: 0px solid;\n"
                                                           "border-radius: 10px;\n"
                                                           "};\n"
                                                           )
            self.frame_inforemation_advan_13.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_advan_13.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_advan_13)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_advan_13)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - (Mathematics)</pre>
                            <pre>B - (Science)</pre>
                            <pre>C - (Engineering-Technology)</pre>
                            <pre>D - (Bio-Technology)</pre>
                            <pre>E - (Commerce)</pre>
                            <pre>F - (Art)</pre>
                            <br>
                            <hr/>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.ui.frame_advanced_level_13_layout.addWidget(
                self.frame_inforemation_advan_13, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax_advan_13 = self.canvas_advan_13.figure.subplots()
            self.ax_advan_13.set_facecolor('#1a1b22')
            self.ax_advan_13.set_alpha(.5)
            self.ax_advan_13.plot(markeredgecolor='#fff')

            self.ax_advan_13.set_xlabel('Type of Students')
            self.ax_advan_13.set_ylabel('Number of Students')

            self.ax_advan_13.spines['left'].set_color('white')
            self.ax_advan_13.spines['top'].set_color('white')
            self.ax_advan_13.spines['bottom'].set_color('white')
            self.ax_advan_13.spines['right'].set_color('white')

            self.ax_advan_13.yaxis.label.set_color('white')
            self.ax_advan_13.xaxis.label.set_color('white')

            self.ax_advan_13.tick_params(colors='white', which='both')
            self.ax_advan_13.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax_advan_13.set_ylim(xlabel_content)

            # X label
            self.ax_advan_13.set_xlim(ylabel_content)

            self.ax_advan_13.bar(content_pos, content_value,
                                 width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax_advan_13.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas_advan_13.draw()

    # ANALYTICS LOWER ADVANCED

    def analytics_lower_Advanced(self, xlabel_content: list, ylabel_content: list, content_pos: list, content_value: list, width, color: str, tot_lower: int):

        if self.barChart_active_lower_ad != True:

            # Bar Chart Frame
            self.frame_barChart_advan = QFrame(self.ui.frame_lower_advan)
            self.frame_barChart_advan.setObjectName("frame_barChart_advam")
            self.frame_barChart_advan.setStyleSheet("QFrame{\n"
                                                    "background-color: none;\n"
                                                    "color: #fff;\n"
                                                    "border: 0px solid;\n"
                                                    "border-radius: 10px;\n"
                                                    "};\n"
                                                    )
            self.frame_barChart_advan.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_advan.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_advan)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas_advan = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas_advan)
            self.ui.frame_lower_advan_layout.addWidget(
                self.frame_barChart_advan)

            # Inforemation Frame
            self.frame_inforemation_advan = QFrame(self.ui.frame_lower_advan)
            self.frame_inforemation_advan.setObjectName(
                "frame_inforemation_advan")
            self.frame_inforemation_advan.setMaximumSize(QSize(200, 100))
            self.frame_inforemation_advan.setMinimumSize(QSize(200, 100))
            self.frame_inforemation_advan.setStyleSheet("QFrame{\n"
                                                        "background-color: #282934;\n"
                                                        "color: #fff;\n"
                                                        "border: 0px solid;\n"
                                                        "border-radius: 10px;\n"
                                                        "};\n"
                                                        )
            self.frame_inforemation_advan.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_advan.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_advan)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_advan)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.btn_more_advanced = QPushButton(self.frame_inforemation_advan)
            self.btn_more_advanced.setFont(font)
            self.btn_more_advanced.setObjectName("btn_more_advanced")
            self.btn_more_advanced.setMaximumSize(QSize(16777215, 30))
            self.btn_more_advanced.setMinimumSize(QSize(0, 30))
            self.btn_more_advanced.setStyleSheet(u"QPushButton{\n"
                                                 "  color: rgb(255, 255, 255);\n"
                                                 "  background-color: rgb(30, 36, 48);\n"
                                                 "  border: 0px solid;\n"
                                                 "  border-radius: 5px;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "  background-color: rgb(21, 134, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed{\n"
                                                 "   background-color: rgba(26, 114, 255, 100);\n"
                                                 "}"
                                                 )
            self.btn_more_advanced.setText("Show More... ")
            icon = QIcon()
            icon.addFile(
                "./packges/app/items/icons/main-icons/icon_arrow_left.svg")
            self.btn_more_advanced.setIcon(icon)
            self.btn_more_advanced.clicked.connect(
                lambda: self.call_input_menu(self.ui.page_more_advanced))
            layout_for_infor.addWidget(self.btn_more_advanced)

            self.ui.frame_lower_advan_layout.addWidget(
                self.frame_inforemation_advan, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax_advan = self.canvas_advan.figure.subplots()
            self.ax_advan.set_facecolor('#1a1b22')
            self.ax_advan.set_alpha(.5)
            self.ax_advan.plot(markeredgecolor='#fff')

            self.ax_advan.set_xlabel('Type of Students')
            self.ax_advan.set_ylabel('Number of Students')

            self.ax_advan.spines['left'].set_color('white')
            self.ax_advan.spines['top'].set_color('white')
            self.ax_advan.spines['bottom'].set_color('white')
            self.ax_advan.spines['right'].set_color('white')

            self.ax_advan.yaxis.label.set_color('white')
            self.ax_advan.xaxis.label.set_color('white')

            self.ax_advan.tick_params(colors='white', which='both')
            self.ax_advan.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax_advan.set_ylim(xlabel_content)

            # X label
            self.ax_advan.set_xlim(ylabel_content)

            self.ax_advan.bar(content_pos, content_value,
                              width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax_advan.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas_advan.draw()

            self.barChart_active_lower_ad = True

        else:
            self.frame_barChart_advan.deleteLater()
            self.frame_inforemation_advan.deleteLater()

            # Bar Chart Frame
            self.frame_barChart_advan = QFrame(self.ui.frame_lower_advan)
            self.frame_barChart_advan.setObjectName("frame_barChart_advan")
            self.frame_barChart_advan.setStyleSheet("QFrame{\n"
                                                    "background-color: none;\n"
                                                    "color: #fff;\n"
                                                    "border: 0px solid;\n"
                                                    "border-radius: 10px;\n"
                                                    "};\n"
                                                    )
            self.frame_barChart_advan.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_advan.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_advan)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas_advan = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas_advan)
            self.ui.frame_lower_advan_layout.addWidget(
                self.frame_barChart_advan)

            # Inforemation Frame
            self.frame_inforemation_advan = QFrame(self.ui.frame_lower_advan)
            self.frame_inforemation_advan.setObjectName(
                "frame_inforemation_advan")
            self.frame_inforemation_advan.setMaximumSize(QSize(200, 100))
            self.frame_inforemation_advan.setMinimumSize(QSize(200, 100))
            self.frame_inforemation_advan.setStyleSheet("QFrame{\n"
                                                        "background-color: #282934;\n"
                                                        "color: #fff;\n"
                                                        "border: 0px solid;\n"
                                                        "border-radius: 10px;\n"
                                                        "};\n"
                                                        )
            self.frame_inforemation_advan.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_advan.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_advan)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_advan)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.btn_more_advanced = QPushButton(self.frame_inforemation_advan)
            self.btn_more_advanced.setFont(font)
            self.btn_more_advanced.setObjectName("btn_more_advanced")
            self.btn_more_advanced.setMaximumSize(QSize(16777215, 30))
            self.btn_more_advanced.setMinimumSize(QSize(0, 30))
            self.btn_more_advanced.setStyleSheet(u"QPushButton{\n"
                                                 "  color: rgb(255, 255, 255);\n"
                                                 "  background-color: rgb(30, 36, 48);\n"
                                                 "  border: 0px solid;\n"
                                                 "  border-radius: 5px;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "  background-color: rgb(21, 134, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed{\n"
                                                 "   background-color: rgba(26, 114, 255, 100);\n"
                                                 "}"
                                                 )
            self.btn_more_advanced.setText("Show More... ")
            icon = QIcon()
            icon.addFile(
                "./packges/app/items/icons/main-icons/icon_arrow_left.svg")
            self.btn_more_advanced.setIcon(icon)
            self.btn_more_advanced.clicked.connect(
                lambda: self.call_input_menu(self.ui.page_more_advanced))
            layout_for_infor.addWidget(self.btn_more_advanced)
            self.ui.frame_lower_advan_layout.addWidget(
                self.frame_inforemation_advan, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax_advan = self.canvas_advan.figure.subplots()
            self.ax_advan.set_facecolor('#1a1b22')
            self.ax_advan.set_alpha(.5)
            self.ax_advan.plot(markeredgecolor='#fff')

            self.ax_advan.set_xlabel('Type of Students')
            self.ax_advan.set_ylabel('Number of Students')

            self.ax_advan.spines['left'].set_color('white')
            self.ax_advan.spines['top'].set_color('white')
            self.ax_advan.spines['bottom'].set_color('white')
            self.ax_advan.spines['right'].set_color('white')

            self.ax_advan.yaxis.label.set_color('white')
            self.ax_advan.xaxis.label.set_color('white')

            self.ax_advan.tick_params(colors='white', which='both')
            self.ax_advan.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax_advan.set_ylim(xlabel_content)

            # X label
            self.ax_advan.set_xlim(ylabel_content)

            self.ax_advan.bar(content_pos, content_value,
                              width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax_advan.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas_advan.draw()

    # ANALYTICS LOWER PRIMARY
    def analytics_lower_primary(self, xlabel_content: list, ylabel_content: list, content_pos: list, content_value: list, width, color: str, tot_lower: int):

        if self.barChart_active_lower_pr != True:

            # Bar Chart Frame
            self.frame_barChart_pri = QFrame(self.ui.frame_lower_prim)
            self.frame_barChart_pri.setObjectName("frame_barChart_pri")
            self.frame_barChart_pri.setStyleSheet("QFrame{\n"
                                                  "background-color: none;\n"
                                                  "color: #fff;\n"
                                                  "border: 0px solid;\n"
                                                  "border-radius: 10px;\n"
                                                  "};\n"
                                                  )
            self.frame_barChart_pri.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_pri.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_pri)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas_pri = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas_pri)
            self.ui.frame_lower_prim_layout.addWidget(self.frame_barChart_pri)

            # Inforemation Frame
            self.frame_inforemation_pri = QFrame(self.ui.frame_lower_prim)
            self.frame_inforemation_pri.setObjectName("frame_inforemation_pri")
            self.frame_inforemation_pri.setMaximumSize(QSize(200, 250))
            self.frame_inforemation_pri.setMinimumSize(QSize(200, 250))
            self.frame_inforemation_pri.setStyleSheet("QFrame{\n"
                                                      "background-color: #282934;\n"
                                                      "color: #fff;\n"
                                                      "border: 0px solid;\n"
                                                      "border-radius: 10px;\n"
                                                      "};\n"
                                                      )
            self.frame_inforemation_pri.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_pri.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_pri)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_pri)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - (Level - 01)</pre>
                            <pre>B - (Level - 02)</pre>
                            <pre>C - (Level - 03)</pre>
                            <pre>D - (Level - 04)</pre>
                            <pre>E - (Level - 05)</pre>
                            <br>
                            <hr/>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.ui.frame_lower_prim_layout.addWidget(
                self.frame_inforemation_pri, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax_pri = self.canvas_pri.figure.subplots()
            self.ax_pri.set_facecolor('#1a1b22')
            self.ax_pri.set_alpha(.5)
            self.ax_pri.plot(markeredgecolor='#fff')

            self.ax_pri.set_xlabel('Type of Students')
            self.ax_pri.set_ylabel('Number of Students')

            self.ax_pri.spines['left'].set_color('white')
            self.ax_pri.spines['top'].set_color('white')
            self.ax_pri.spines['bottom'].set_color('white')
            self.ax_pri.spines['right'].set_color('white')

            self.ax_pri.yaxis.label.set_color('white')
            self.ax_pri.xaxis.label.set_color('white')

            self.ax_pri.tick_params(colors='white', which='both')
            self.ax_pri.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax_pri.set_ylim(xlabel_content)

            # X label
            self.ax_pri.set_xlim(ylabel_content)

            self.ax_pri.bar(content_pos, content_value,
                            width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax_pri.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas_pri.draw()

            self.barChart_active_lower_pr = True

        else:
            self.frame_barChart_pri.deleteLater()
            self.frame_inforemation_pri.deleteLater()

            # Bar Chart Frame
            self.frame_barChart_pri = QFrame(self.ui.frame_lower_prim)
            self.frame_barChart_pri.setObjectName("frame_barChart_pri")
            self.frame_barChart_pri.setStyleSheet("QFrame{\n"
                                                  "background-color: none;\n"
                                                  "color: #fff;\n"
                                                  "border: 0px solid;\n"
                                                  "border-radius: 10px;\n"
                                                  "};\n"
                                                  )
            self.frame_barChart_pri.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_pri.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_pri)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas_pri = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas_pri)
            self.ui.frame_lower_prim_layout.addWidget(self.frame_barChart_pri)

            # Inforemation Frame
            self.frame_inforemation_pri = QFrame(self.ui.frame_lower_prim)
            self.frame_inforemation_pri.setObjectName("frame_inforemation_pri")
            self.frame_inforemation_pri.setMaximumSize(QSize(200, 250))
            self.frame_inforemation_pri.setMinimumSize(QSize(200, 250))
            self.frame_inforemation_pri.setStyleSheet("QFrame{\n"
                                                      "background-color: #282934;\n"
                                                      "color: #fff;\n"
                                                      "border: 0px solid;\n"
                                                      "border-radius: 10px;\n"
                                                      "};\n"
                                                      )
            self.frame_inforemation_pri.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_pri.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_pri)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_pri)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - (Level - 01)</pre>
                            <pre>B - (Level - 02)</pre>
                            <pre>C - (Level - 03)</pre>
                            <pre>D - (Level - 04)</pre>
                            <pre>E - (Level - 05)</pre>
                            <br>
                            <hr/>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.ui.frame_lower_prim_layout.addWidget(
                self.frame_inforemation_pri, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax_pri = self.canvas_pri.figure.subplots()
            self.ax_pri.set_facecolor('#1a1b22')
            self.ax_pri.set_alpha(.5)
            self.ax_pri.plot(markeredgecolor='#fff')

            self.ax_pri.set_xlabel('Type of Students')
            self.ax_pri.set_ylabel('Number of Students')

            self.ax_pri.spines['left'].set_color('white')
            self.ax_pri.spines['top'].set_color('white')
            self.ax_pri.spines['bottom'].set_color('white')
            self.ax_pri.spines['right'].set_color('white')

            self.ax_pri.yaxis.label.set_color('white')
            self.ax_pri.xaxis.label.set_color('white')

            self.ax_pri.tick_params(colors='white', which='both')
            self.ax_pri.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax_pri.set_ylim(xlabel_content)

            # X label
            self.ax_pri.set_xlim(ylabel_content)

            self.ax_pri.bar(content_pos, content_value,
                            width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax_pri.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas_pri.draw()

    # ANALYTICS LOWER

    def analytics_lower(self, xlabel_content: list, ylabel_content: list, content_pos: list, content_value: list, width, color: str, tot_lower: int):

        if self.barChart_active_lower != True:

            # Bar Chart Frame
            self.frame_barChart = QFrame(self.ui.frame_lower)
            self.frame_barChart.setObjectName("frame_barChart")
            self.frame_barChart.setStyleSheet("QFrame{\n"
                                              "background-color: none;\n"
                                              "color: #fff;\n"
                                              "border: 0px solid;\n"
                                              "border-radius: 10px;\n"
                                              "};\n"
                                              )
            self.frame_barChart.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas)
            self.ui.lower_frame_layout.addWidget(self.frame_barChart)

            # Inforemation Frame
            self.frame_inforemation = QFrame(self.ui.frame_lower)
            self.frame_inforemation.setObjectName("frame_inforemation")
            self.frame_inforemation.setMaximumSize(QSize(200, 250))
            self.frame_inforemation.setMinimumSize(QSize(200, 250))
            self.frame_inforemation.setStyleSheet("QFrame{\n"
                                                  "background-color: #282934;\n"
                                                  "color: #fff;\n"
                                                  "border: 0px solid;\n"
                                                  "border-radius: 10px;\n"
                                                  "};\n"
                                                  )
            self.frame_inforemation.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - (Level - 06)</pre>
                            <pre>B - (Level - 07)</pre>
                            <pre>C - (Level - 08)</pre>
                            <pre>D - (Level - 09)</pre>
                            <pre>E - (Level - 10)</pre>
                            <pre>F - (Level - 11)</pre>
                            <br>
                            <hr/>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.ui.lower_frame_layout.addWidget(
                self.frame_inforemation, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax = self.canvas.figure.subplots()
            self.ax.set_facecolor('#1a1b22')
            self.ax.set_alpha(.5)
            self.ax.plot(markeredgecolor='#fff')

            self.ax.set_xlabel('Type of Students')
            self.ax.set_ylabel('Number of Students')

            self.ax.spines['left'].set_color('white')
            self.ax.spines['top'].set_color('white')
            self.ax.spines['bottom'].set_color('white')
            self.ax.spines['right'].set_color('white')

            self.ax.yaxis.label.set_color('white')
            self.ax.xaxis.label.set_color('white')

            self.ax.tick_params(colors='white', which='both')
            self.ax.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax.set_ylim(xlabel_content)

            # X label
            self.ax.set_xlim(ylabel_content)

            self.ax.bar(content_pos, content_value,
                        width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas.draw()

            self.barChart_active_lower = True

        else:
            self.frame_barChart.deleteLater()
            self.frame_inforemation.deleteLater()

            # Bar Chart Frame
            self.frame_barChart = QFrame(self.ui.frame_lower)
            self.frame_barChart.setObjectName("frame_barChart")
            self.frame_barChart.setStyleSheet("QFrame{\n"
                                              "background-color: none;\n"
                                              "color: #fff;\n"
                                              "border: 0px solid;\n"
                                              "border-radius: 10px;\n"
                                              "};\n"
                                              )
            self.frame_barChart.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(6, 3))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas)
            self.ui.lower_frame_layout.addWidget(self.frame_barChart)

            # Inforemation Frame
            self.frame_inforemation = QFrame(self.ui.frame_lower)
            self.frame_inforemation.setObjectName("frame_inforemation")
            self.frame_inforemation.setMaximumSize(QSize(200, 250))
            self.frame_inforemation.setMinimumSize(QSize(200, 250))
            self.frame_inforemation.setStyleSheet("QFrame{\n"
                                                  "background-color: #282934;\n"
                                                  "color: #fff;\n"
                                                  "border: 0px solid;\n"
                                                  "border-radius: 10px;\n"
                                                  "};\n"
                                                  )
            self.frame_inforemation.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - (Level - 06)</pre>
                            <pre>B - (Level - 07)</pre>
                            <pre>C - (Level - 08)</pre>
                            <pre>D - (Level - 09)</pre>
                            <pre>E - (Level - 10)</pre>
                            <pre>F - (Level - 11)</pre>
                            <br>
                            <hr/>
                            <pre>Total Students: {tot_lower}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)
            self.ui.lower_frame_layout.addWidget(
                self.frame_inforemation, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax = self.canvas.figure.subplots()
            self.ax.set_facecolor('#1a1b22')
            self.ax.set_alpha(.5)
            self.ax.plot(markeredgecolor='#fff')

            self.ax.set_xlabel('Type of Students')
            self.ax.set_ylabel('Number of Students')

            self.ax.spines['left'].set_color('white')
            self.ax.spines['top'].set_color('white')
            self.ax.spines['bottom'].set_color('white')
            self.ax.spines['right'].set_color('white')

            self.ax.yaxis.label.set_color('white')
            self.ax.xaxis.label.set_color('white')

            self.ax.tick_params(colors='white', which='both')
            self.ax.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax.set_ylim(xlabel_content)

            # X label
            self.ax.set_xlim(ylabel_content)

            self.ax.bar(content_pos, content_value,
                        width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas.draw()

    # ANALYTICS INTER

    def analytics_inter(self, xlabel_content: list, ylabel_content: list, content_pos: list, content_value: list, width, color: str, tot_inter: int) -> None:

        if self.barChart_active_inter != True:

            # Bar Chart Frame
            self.frame_barChart_in = QFrame(self.ui.frame_inter)
            self.frame_barChart_in.setObjectName("frame_barChart")
            self.frame_barChart_in.setStyleSheet("QFrame{\n"
                                                 "background-color: none;\n"
                                                 "color: #fff;\n"
                                                 "border: 0px solid;\n"
                                                 "border-radius: 10px;\n"
                                                 "};\n"
                                                 )
            self.frame_barChart_in.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_in.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_in)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(12, 6))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas)
            self.ui.inter_frame_layout.addWidget(self.frame_barChart_in)

            # Inforemation Frame
            self.frame_inforemation_in = QFrame(self.ui.frame_inter)
            self.frame_inforemation_in.setObjectName("frame_inforemation")
            self.frame_inforemation_in.setMaximumSize(QSize(200, 250))
            self.frame_inforemation_in.setMinimumSize(QSize(200, 250))
            self.frame_inforemation_in.setStyleSheet("QFrame{\n"
                                                     "background-color: #282934;\n"
                                                     "color: #fff;\n"
                                                     "border: 0px solid;\n"
                                                     "border-radius: 10px;\n"
                                                     "};\n"
                                                     )
            self.frame_inforemation_in.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_in.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_in)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_in)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - Subject </pre>
                            <pre>B - None-Subject </pre>
                            <pre>C - E-Mail </pre>
                            <pre>D - None-(E-Mail) </pre>
                            <pre>E - Level </pre>
                            <pre>F - None-Level </pre>
                            <br>
                            <hr/>
                            <pre>Total Teachers: {tot_inter}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)

            self.ui.inter_frame_layout.addWidget(
                self.frame_inforemation_in, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Draw Bar Chart
            matplotlib.rc("font", **font)
            self.ax = self.canvas.figure.subplots()
            self.ax.set_facecolor('#1a1b22')
            self.ax.set_alpha(.5)
            self.ax.plot(markeredgecolor='#fff')

            self.ax.set_xlabel('Type of Teachers')
            self.ax.set_ylabel('Number of Teachers')

            self.ax.spines['left'].set_color('white')
            self.ax.spines['top'].set_color('white')
            self.ax.spines['bottom'].set_color('white')
            self.ax.spines['right'].set_color('white')

            self.ax.yaxis.label.set_color('white')
            self.ax.xaxis.label.set_color('white')

            self.ax.tick_params(colors='white', which='both')
            self.ax.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax.set_ylim(xlabel_content)

            # X label
            self.ax.set_xlim(ylabel_content)

            self.ax.bar(content_pos, content_value,
                        width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas.draw()

            self.barChart_active_inter = True

        else:

            self.frame_barChart_in.deleteLater()
            self.frame_inforemation_in.deleteLater()

            # Bar Chart Frame
            self.frame_barChart_in = QFrame(self.ui.frame_inter)
            self.frame_barChart_in.setObjectName("frame_barChart")
            self.frame_barChart_in.setStyleSheet("QFrame{\n"
                                                 "background-color: none;\n"
                                                 "color: #fff;\n"
                                                 "border: 0px solid;\n"
                                                 "border-radius: 10px;\n"
                                                 "};\n"
                                                 )
            self.frame_barChart_in.setFrameShape(QFrame.StyledPanel)
            self.frame_barChart_in.setFrameShadow(QFrame.Raised)

            # Bar Chart Frame Layout
            layout_barChart = QHBoxLayout(self.frame_barChart_in)
            layout_barChart.setContentsMargins(2, 2, 2, 2)
            layout_barChart.setSpacing(0)

            # Figure Compnent
            fig = plt.Figure(figsize=(12, 6))
            fig.patch.set_facecolor('#1a1b22')
            self.canvas = FigureCanvas(fig)

            layout_barChart.addWidget(self.canvas)
            self.ui.inter_frame_layout.addWidget(self.frame_barChart_in)

            # Inforemation Frame
            self.frame_inforemation_in = QFrame(self.ui.frame_inter)
            self.frame_inforemation_in.setObjectName("frame_inforemation")
            self.frame_inforemation_in.setMaximumSize(QSize(200, 250))
            self.frame_inforemation_in.setMinimumSize(QSize(200, 250))
            self.frame_inforemation_in.setStyleSheet("QFrame{\n"
                                                     "background-color: #282934;\n"
                                                     "color: #fff;\n"
                                                     "border: 0px solid;\n"
                                                     "border-radius: 10px;\n"
                                                     "};\n"
                                                     )
            self.frame_inforemation_in.setFrameShape(QFrame.StyledPanel)
            self.frame_inforemation_in.setFrameShadow(QFrame.Raised)

            layout_for_infor = QVBoxLayout(self.frame_inforemation_in)
            layout_for_infor.setContentsMargins(0, 0, 0, 0)
            layout_for_infor.setSpacing(0)

            font = QFont()
            font.setFamily("monospace, sans-serif")
            font.setPointSize(10)
            font.setBold(True)

            label_info = QLabel(self.frame_inforemation_in)
            label_info.setFont(font)
            label_info.setObjectName("label_info")
            label_info.setStyleSheet("QLabel{\n"
                                     "   background-color: none;\n"
                                     "   color: #8f93ba;\n"
                                     "   padding: 7px;\n"
                                     "}\n")
            label_info.setText(f"""
                <html>
                    <head/>
                    <body>
                        <p>
                            <pre>A - Subject </pre>
                            <pre>B - None-Subject </pre>
                            <pre>C - E-Mail </pre>
                            <pre>D - None-(E-Mail) </pre>
                            <pre>E - Level </pre>
                            <pre>F - None-Level </pre>
                            <br>
                            <hr/>
                            <pre>Total Teachers: {tot_inter}</pre>
                        </p>
                    </body>
                </html>
            """)
            layout_for_infor.addWidget(label_info)

            self.ui.inter_frame_layout.addWidget(
                self.frame_inforemation_in, 0, Qt.AlignTop)

            # Font
            font = {
                "family": "monospace"
            }

            # Bar Chart Draw
            matplotlib.rc("font", **font)
            self.ax = self.canvas.figure.subplots()
            self.ax.set_facecolor('#1a1b22')
            self.ax.set_alpha(.5)
            self.ax.plot(markeredgecolor='#fff')

            self.ax.set_xlabel('Type of Teachers')
            self.ax.set_ylabel('Number of Teachers')

            self.ax.spines['left'].set_color('white')
            self.ax.spines['top'].set_color('white')
            self.ax.spines['bottom'].set_color('white')
            self.ax.spines['right'].set_color('white')

            self.ax.yaxis.label.set_color('white')
            self.ax.xaxis.label.set_color('white')

            self.ax.tick_params(colors='white', which='both')
            self.ax.tick_params(axis='x', which='major', labelsize=8)

            # Y label
            self.ax.set_ylim(xlabel_content)

            # X label
            self.ax.set_xlim(ylabel_content)

            self.ax.bar(content_pos, content_value,
                        width=width, color=color, edgecolor='#fff', linewidth=2)
            self.ax.grid(color="#007acc", linewidth=0.5,  alpha=0.1)
            self.canvas.draw()

    # Right Click Menu bar

    def eventFilter(self, source: QtCore.QObject, event: QtCore.QEvent) -> bool:

        # COPY EVENT
        if event.type() == QEvent.KeyPress and event == QKeySequence.Copy:

            text = None

            # Active Status
            if self.ui.label_info_lower_1.selectedText():
                text = self.ui.label_info_lower_1.selectedText()
            if self.ui.label_info_Inter_1.selectedText():
                text = self.ui.label_info_Inter_1.selectedText()

            if self.ui.label_show_roll_primary.selectedText():
                text = self.ui.label_show_roll_primary.selectedText()
            if self.ui.label_show_roll_ad.selectedText():
                text = self.ui.label_show_roll_ad.selectedText()

            if self.ui.label_show_roll_number.selectedText():
                text = self.ui.label_show_roll_number.selectedText()
            if self.ui.label_show_roll_number_lower.selectedText():
                text = self.ui.label_show_roll_primary.selectedText()
            if self.ui.label_info_lower_advan.selectedText():
                text = self.ui.label_info_lower_advan.selectedText()
            if self.ui.label_info_lower_pri.selectedText():
                text = self.ui.label_info_lower_pri.selectedText()

            # Left Status
            if self.ui.info_inter_left_1.selectedText():
                text = self.ui.info_inter_left_1.selectedText()
            if self.ui.info_lower_1.selectedText():
                text = self.ui.info_lower_1.selectedText()
            if self.ui.info_lower_left_pri.selectedText():
                text = self.ui.info_lower_left_pri.selectedText()
            if self.ui.info_lower_left_advan.selectedText():
                text = self.ui.info_lower_left_advan.selectedText()

            if text and text != None:
                QApplication.clipboard().setText(text)

        elif event.type() == QEvent.ContextMenu and (source is self.ui.label_info_lower_1 or source is self.ui.label_info_Inter_1 or source is self.ui.info_inter_left_1 or source is self.ui.info_lower_1 or source is self.ui.label_show_roll_ad or source is self.ui.label_show_roll_primary or source is self.ui.label_show_roll_number_lower or source is self.ui.label_show_roll_number or source is self.ui.info_lower_left_pri or source is self.ui.label_info_lower_pri or source is self.ui.label_info_lower_advan or source is self.ui.info_lower_left_advan):

            text = None
            # Active Status
            if self.ui.label_info_lower_1.selectedText():
                text = self.ui.label_info_lower_1.selectedText()
            if self.ui.label_info_Inter_1.selectedText():
                text = self.ui.label_info_Inter_1.selectedText()
            if self.ui.label_info_lower_advan.selectedText():
                text = self.ui.label_info_lower_advan.selectedText()
            if self.ui.label_info_lower_pri.selectedText():
                text = self.ui.label_info_lower_pri.selectedText()

            # Left Status
            if self.ui.info_inter_left_1.selectedText():
                text = self.ui.info_inter_left_1.selectedText()
            if self.ui.info_lower_1.selectedText():
                text = self.ui.info_lower_1.selectedText()

            if self.ui.label_show_roll_ad.selectedText():
                text = self.ui.label_show_roll_ad.selectedText()
            if self.ui.label_show_roll_primary.selectedText():
                text = self.ui.label_show_roll_primary.selectedText()

            if self.ui.label_show_roll_number.selectedText():
                text = self.ui.label_show_roll_number.selectedText()
            if self.ui.label_show_roll_number_lower.selectedText():
                text = self.ui.label_show_roll_primary.selectedText()

            if self.ui.info_lower_left_pri.selectedText():
                text = self.ui.info_lower_left_pri.selectedText()
            if self.ui.info_lower_left_advan.selectedText():
                text = self.ui.info_lower_left_advan.selectedText()

            menu = QMenu(self)
            copyAction = menu.addAction("Copy")
            copyAction.setShortcut("Ctrl+C")

            paste = menu.addAction("Paste")
            paste.setShortcut("Ctrl+V")
            paste.setEnabled(False)

            menu.setStyleSheet("""
                QMenu {
                    color: #fff;
                    border: 0px solid;
                    border-radius: 5px;
                    padding-left: 10px;
                    padding-right: 10px;
                }
                QMenu::item {
                    background-color: transparent;
                }
                QMenu::item:selected {
                    background-color: rgba(85, 170, 255, 100);
                    border-radius: 5px;
                }
                QMenu::item:disabled {
                    background-color: transparent;
                    color: rgb(100, 100, 100);
                }
            """)

            if not text and text is None:
                copyAction.setEnabled(False)
            res = menu.exec_(QCursor.pos())
            if res == copyAction:
                QApplication.clipboard().setText(text)

        return super().eventFilter(source, event)

    # Reset Data
    def reset(self):
        if "config.bin" in os.listdir(PATH_CONFIG_DIR):
            if "data.json" in os.listdir(PATH_STORE_DATA_DIR):
                os.remove(PATH_STORE_DATA_FILE)
            if "recycleBin.json" in os.listdir(PATH_STORE_DATA_DIR):
                os.remove(PATH_STORE_DATA_BIN_FILE)
            if "setting.json" in os.listdir(PATH_STORE_DATA_DIR):
                os.remove(PATH_STORE_DATA_SETTING)

            ReadBinary.write_binary_file("False")
        self.close()
        runBash()

    # Logout
    def logout(self):
        self.close()
        runBash()

    # Reload
    def reload(self):
        self.close()
        runBash()


# Add Icon For Line Edit
def setIcon_line(lineEditName, icon_path):
    icon = QIcon()
    icon.addFile(icon_path, QSize(), QIcon.Normal, QIcon.Off)
    lineEditName.addAction(icon, QLineEdit.LeadingPosition)

# Rerunner


def runBash():
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)


# First Runner code
class AppRnuner(object):

    def __init__(self):

        # This Find .findup folder
        if ".findup" not in os.listdir(PATH_SAVE_FILE):
            os.makedirs(PATH_CONFIG_DIR)
            os.makedirs(PATH_STORE_DATA_DIR)

    def startWindow(self):

        # Get Create Window
        if "config.bin" not in os.listdir(PATH_CONFIG_DIR):
            app = QApplication(sys.argv)
            create = Create()
            create.show()
            sys.exit(app.exec_())

        else:
            # Get Login Window
            data = ReadBinary.read_binary_file()
            if data == 'True':
                app = QApplication(sys.argv)
                login = Login()
                login.show()
                sys.exit(app.exec_())

            else:
                # Get Create Window
                app = QApplication(sys.argv)
                create = Create()
                target = create.show()
                sys.exit(app.exec_())


if __name__ == "__main__":
    main = AppRnuner()
    main.startWindow()
