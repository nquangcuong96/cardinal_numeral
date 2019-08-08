import wx
import cardinal_numeral


########################################################################
class MyForm(wx.Frame):
    # ----------------------------------------------------------------------
    ans = ''
    region = 'north'
    language = 'VN'
    tss = False
    n = 0

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "Cardinal Numeral", style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
        panel = wx.Panel(self, wx.ID_ANY)
        a = wx.Button(panel, label="Click here to input a number")
        a.Bind(wx.EVT_BUTTON, self.onButton1)

        c = wx.Button(panel, label="Click here to set Region")
        c.Bind(wx.EVT_BUTTON, self.onButton2)

        d = wx.Button(panel, label="Click here set ask computer spell the number")
        d.Bind(wx.EVT_BUTTON, self.onButton3)

        e = wx.Button(panel, label="Click here set language output")
        e.Bind(wx.EVT_BUTTON, self.onButton4)

        f = wx.Button(panel, label="Click here to see the answer")
        f.Bind(wx.EVT_BUTTON, self.onButton5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(a, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(c, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(d, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(e, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(f, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(sizer)

    # ----------------------------------------------------------------------
    def onButton1(self, event):
        dlg = wx.TextEntryDialog(
            self, 'Please input any number from 0 to 999999999999',
            'Input dialog: ')
        if dlg.ShowModal() == wx.ID_OK:
            for i in dlg.GetValue():
                if ord(i) < 47 or ord(i) > 58:
                    note = wx.GenericMessageDialog(self, 'Wrong input')
                    if note.ShowModal() == wx.ID_OK:
                        note.Destroy()
                        break
            if int(dlg.GetValue()) > 999999999999:
                note = wx.GenericMessageDialog(self, 'Wrong input')
                if note.ShowModal() == wx.ID_OK:
                    note.Destroy()
            MyForm.n = int(dlg.GetValue())
        dlg.Destroy()

    # ----------------------------------------------------------------------
    def onButton5(self, event):
        if MyForm.language == 'VN':
            ans = cardinal_numeral.integer_to_vietnamese_numeral(MyForm.n, MyForm.region, MyForm.tss)
        else:
            ans = cardinal_numeral.integer_to_english_numeral(MyForm.n, MyForm.tss)
        dlg = wx.GenericMessageDialog(
            self, str(MyForm.n) + ' :' + ans
        )
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()

    # ----------------------------------------------------------------------
    def onButton2(self, event):
        if MyForm.region == 'north':
            MyForm.region = 'south'
        else:
            MyForm.region = 'north'
        dlg = wx.GenericMessageDialog(
            self, MyForm.region
        )
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()

    # ----------------------------------------------------------------------
    def onButton3(self, event):
        if not MyForm.tss:
            MyForm.tss = True
            string = 'Speaker On'
        else:
            MyForm.tss = False
            string = 'Speaker Off'
        dlg = wx.GenericMessageDialog(
            self, string
        )
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()

    # ----------------------------------------------------------------------
    def onButton4(self, event):
        if MyForm.language == 'VN':
            MyForm.language = 'EN'
        else:
            MyForm.language = 'VN'
        dlg = wx.GenericMessageDialog(
            self, MyForm.language
        )
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()


# ----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    frame.Center()
    app.MainLoop()
