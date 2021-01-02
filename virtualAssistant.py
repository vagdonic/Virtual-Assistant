import wx
import wikipedia
import wolframalpha

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(400, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Virtual Assistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Ask me a question!")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        question = self.txt.GetValue()
        question = question.lower()
        try:
            #wolframalpha code:
            app_id = 'Your App ID'
            client = wolframalpha.Client(app_id)
            result = client.query(question)
            answer = next(result.results).text
            print(answer)
        except:
            try:
                #wikipedia code:
                question = question.split(' ')
                question = ' '.join(question[2:])
                print(wikipedia.summary(question))

            except:
                print("Sorry, i don't know.")            


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()