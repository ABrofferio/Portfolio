import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.basicGUI()
    def basicGUI(self):
        panel=wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        editButton = wx.Menu()
        exitItem = fileButton.Append(wx.NewId(), 'Exit', 'status')
        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        animalBox = wx.TextEntryDialog(None, "What's your favorite animal?", 'Welcome', 'animal')
        if animalBox.ShowModal() == wx.ID_OK:
            userAnimal = animalBox.GetValue()

        yesNoBox = wx.MessageDialog(None, 'Do you enjoy wx.Python?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        if yesNoAnswer == wx.ID_NO:
            userAnimal = 'wx.Python hater'

        chooseOneBox = wx.SingleChoiceDialog(None, "What's your favorite color?",
                                             'Color Question',
                                             ['Green', 'Red', 'Blue', 'Yellow'])
        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        wx.TextCtrl(panel, pos=(3,100), size=(150,50))
        aweText = wx.StaticText(panel, -1,"This is your favorite color", (3,3))
        aweText.SetForegroundColour(favColor)
        aweText.SetBackgroundColour('blue')

        self.SetTitle('Welcome, ' +userAnimal+ ' lover')
        self.Show()

    def Quit(self, e):
        leave = raw_input("Are you sure you want to exit? Y/N")
        if leave == "Y" or "y":
            self.Close()
        else:
            return
            #typing anyting other than Y or y still closes the window
def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()
main()
  
