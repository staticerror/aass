import wx
import wx.xrc as xrc
from html2text import html2text
from artdirs import *
import time, thread
from yanswers import Answers
import Queue, threading


GUI_FILENAME  = "gui.xrc"
GUI_MAINFRAME_NAME = "MyFrame1"

class MyApp(wx.App):
    def OnInit(self):
        # Load all controls:
        self._do_layout()
        self.txt = xrc.XRCCTRL( self.frame, "keyword_text")
        self.separator = """----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n"""
        self.q = Queue.Queue()



        return True

    def _do_layout(self):
        self.res = xrc.XmlResource( GUI_FILENAME )
        self.frame = self.res.LoadFrame( None,  GUI_MAINFRAME_NAME )
        self.SetTopWindow(self.frame)
        self.frame.Show()
        self.go_button =  xrc.XRCCTRL(self.frame, "go_button")
        self.go_button1 =  xrc.XRCCTRL(self.frame, "go_button1")
        self.frame.Bind(wx.EVT_BUTTON, self.getArticleResult, self.go_button)
        self.frame.Bind(wx.EVT_BUTTON, self.getAnswersResult, self.go_button1)

        self.frame.Maximize()



    def getArticleResult(self, event):
        self.articleResults = xrc.XRCCTRL( self.frame, "results_text")
        self.articleResults.Clear()
        keyword = self.txt.GetValue()
        thread.start_new_thread(self.fetcharticle, (keyword,))


    def fetcharticle(self, keyword):
        articlelist = [Ezine, Dashboard, Snatch, ABase, Buzzle]
        for model in articlelist:
            art = model()
            art.fetchArticle(keyword)
            article = art.article
            article = map(str, article)
            article = map(html2text.html2text, article)
            wx.CallAfter(self.updateArticleUI, article)

    def updateArticleUI(self,article):
        self.articleResults.AppendText(article[0] + article[1] + article[2])
        self.articleResults.AppendText(self.separator)


    def getAnswersResult(self, event):
        self.answersResults1 = xrc.XRCCTRL( self.frame, "results_text1")
        self.answersResults1.Clear()
        self.txt2 = xrc.XRCCTRL( self.frame, "keyword_text1")
        answerskeyword = self.txt2.GetValue().replace(" ","+")

        thread.start_new_thread(self.fetchanswers,(answerskeyword,))

        
    def fetchanswers(self, keyword):
        app = Answers()
        app.appid = "e0U05XjV34HKgxTrrFSZORdBbZPvFdBNR1gx1rd9vsnGc1ph2LjV3kQlUpObW8cSBPc-"
        result = app.questionSearch({'query': keyword, 'search_in':'best_answer', 'results' : '10' })
        wx.CallAfter(self.updateAnswersUI, result)


    def updateAnswersUI(self,result):
        for res in result:
            self.answersResults1.AppendText("Question:\n" + res['Subject'].encode('utf8') + res['Content'].encode('utf8') + "\nAnswer:\n" +res['ChosenAnswer'].encode('utf8') + "\n\n" + self.separator )




        
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
