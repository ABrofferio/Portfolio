import wx, db_program


class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800, 600))
        panel = wx.Panel(self)
        
        #create menu bar
        menuBar = wx.MenuBar()
        #create File menu
        fileMenu = wx.Menu()
        #append exit item to File menu
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        #append File menu to menu bar
        menuBar.Append(fileMenu,"File")
        #Set up menubar and status bar and give exit item functionality
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exit, exitItem)
        self.CreateStatusBar()

        wx.StaticBox(panel, label='Add a New Character', pos=(20,40), size=(280,190))        
        wx.StaticText(panel, label='Name:', pos=(30,70))
        wx.StaticText(panel, label='Gender:', pos=(30,110))
        wx.StaticText(panel, label='Age:', pos=(30,150))
        wx.StaticText(panel, label='Occupation:', pos=(30,190))

        self.sName = wx.TextCtrl(panel, size=(150, -1), pos=(130, 70))
        self.sGen = wx.TextCtrl(panel, size=(150, -1), pos=(130, 110))
        self.sAge = wx.SpinCtrl(panel, value='0', pos=(130, 150), size=(70, 25))
        self.sOcc = wx.TextCtrl(panel, size=(150, -1), pos=(130, 190))

        save = wx.Button(panel, label="Add Character", pos=(100,230))
        save.Bind(wx.EVT_BUTTON, self.addCharacter)

        #setup table UI as listCtrl
        self.listCtrl = wx.ListCtrl(panel, size=(400,400), pos=(350,40), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.listCtrl.InsertColumn(0,"ID")
        self.listCtrl.InsertColumn(1,"Name")
        self.listCtrl.InsertColumn(2,"Gender")
        self.listCtrl.InsertColumn(3,"Age")
        self.listCtrl.InsertColumn(4,"Occupation")

        self.fillListCtrl()

        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)

        deleteBtn = wx.Button(panel, label="Delete", pos=(640,450))

        deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)

        
    def addCharacter(self, event):
        name = self.sName.GetValue()
        gen = self.sGen.GetValue()
        age = self.sAge.GetValue()
        occ = self.sOcc.GetValue()

        #check that variables have an assigned value
        if (name == '') or (gen == '') or (age == '') or (occ == ''):
            dlg = wx.MessageDialog(None, 'Some character details are missing. Enter values in each text box.', 'Missing Details', wx.OK)
            #displays the dialogue box
            dlg.ShowModal()
            dlg.Destroy()
            #ends the function
            return False
        #printing to the console
        print name
        print gen
        print age
        print occ
        #adding character to database
        db_program.newCharacter(name, gen, age, occ)
        print db_program.viewAll()
        #resetting the frame for new inputs
        self.sName.Clear()
        self.sGen.Clear()
        self.sAge.SetValue(0)
        self.sOcc.Clear()
        #add data to list control table
        self.fillListCtrl()

    def fillListCtrl(self):
        allData = db_program.viewAll()
        self.listCtrl.DeleteAllItems()
        for row in allData:
            self.listCtrl.Append(row)

    def onDelete(self, event):
        db_program.deleteCharacter(self.selectedId)
        self.fillListCtrl()

    def onSelect(self, event):
        #get the id of the selected row to delete
        self.selectedId = event.GetText()
        
    def exit(self, event):
        print "hello"
        self.Destroy()

app = wx.App()
frame = Frame("Python GUI 2")
frame.Show()
app.MainLoop()
        

