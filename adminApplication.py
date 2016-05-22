# A00202022

# This application was to be used as part of the final build, however the
# functionality was no developed in time. (Other users story)

# Import PyQT Stuff
from PyQt4 import QtCore, QtGui

#Import Gui Class
from adminGUI import Ui_MainWindow

# NukeBox 2000 Main Class
class NukeBox2000Server(QtGui.QMainWindow, Ui_MainWindow):

    '''
    This class is used to build the NukeBox Server Client
    '''

    # Initialize
    def __init__(self):

        QtGui.QMainWindow.__init__(self)

        # Call the UI Main window class
        self.setupUi(self)

        # Transport Control
        self.playBtn.clicked.connect(lambda: self.transportControl("Play"))
        self.stopBtn.clicked.connect(lambda: self.transportControl("Stop"))
        self.skipButton.clicked.connect(lambda: self.transportControl("Skip"))
        self.volumeSlider.sliderReleased.connect(self.volumeAdjust)
        self.trackSlide.sliderReleased.connect(self.trackAdjust)

        # User Administration
        self.removeUser.clicked.connect(lambda: self.userAdmin("Remove"))
        self.banUser.clicked.connect(lambda: self.userAdmin("Ban"))
        self.userMusic.clicked.connect(lambda: self.userAdmin("Music"))
        self.restartServer.clicked.connect(self.restartFunc)
        self.viewLogs.clicked.connect(self.viewLogInfo)
        self.userGo.clicked.connect(self.searchUsers)


    #####################
    #   Begin Methods   #
    #####################

    # Transport Controls 
    def transportControl(self, action):

        '''
        This method allows users to interact with the transport controls of the
        player. It taakes on additional attribute which defines the control type.
        -   action: Button pressed/Control Type
        '''
        # Play
        if action == "Play":
            pass
        # Stop
        elif action == "Stop":
            pass
        # Skip
        elif action == "Skip":
            pass

    # Volume Slider
    def volumeAdjust(self):
        '''
        Used to adjust the volume of the third party audio player
        '''

        # User specified value between 0% and 100%
        volume = self.volumeSlider.value()
        pass

    # Track Slider
    def trackAdjust(self):
        '''
        Used to adjust the track position, information is to be fed a
        third party audio player.

        The current Track time should also be calculated here

        '''

        # User specified value between 0% and 100%
        trackposition = self.trackSlide.value()

        #Update the track timer (Placeholder data)
        self.trackTime.setText("2:28/3:36")

        pass

    # User Administration
    def userAdmin(self, action):

        '''
        This method allows users toaccess adinisstrative functonality on the
        admin application. It taakes on additional attribute which defines 
        the user interaction.

        On click the selected user in the list would be administrated.

        -   action: User interaction
        '''
        # Get the User info
        try:
            self.user = self.userList.currentItem().text()

            # Remove the User
            if action == "Remove":
                pass
            # Ban their MAC addresss
            elif action == "Ban":
                pass
            # Remove/Flush users music
            elif action == "Music":
                pass

        # No user selected
        except:
            pass

    # Restart Server
    def restartFunc(self):
        '''
        This method is a place holder for the server restart functionality.
        '''
        pass

    # Log Information
    def viewLogInfo(self):
        '''
        A method which calls the log information.
        '''
        pass

    # Search Users
    def searchUsers(self):
        '''
        This method is triggerd when the user tries to search for users, the
        objective of this is to provide a way to search large databases of
        users within the database.
        '''
        pass


# Main Program
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = NukeBox2000Server()
    MainWindow.show()
    sys.exit(app.exec_())
