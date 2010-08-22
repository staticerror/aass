import wx
import wx.xrc as xrc
from html2text import html2text
from artdirs import *
import time, thread
from yanswers import Answers
import Queue, threading, sys, os
import sqlite3


GUI_FILENAME  = "gui.xrc"
GUI_MAINFRAME_NAME = "MyFrame1"

class MyApp(wx.App):
    def OnInit(self):
        # Load all controls:
        self._do_layout()

        self.txt = xrc.XRCCTRL( self.frame, "keyword_text")
        self.articleResults = xrc.XRCCTRL( self.frame, "results_text")
        self.keyword = self.txt.GetValue()
        self.choice = xrc.XRCCTRL( self.frame, "the_choice")

        self.separator = """----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n"""


        self.resnote = xrc.XRCCTRL( self.frame, "note_text")
        self.allnotes = xrc.XRCCTRL( self.frame, "all_notes_text")
        
        self.init_list()
        return True


    def init_list(self):
        self.the_list = xrc.XRCCTRL( self.frame, "the_list")
        self.the_list.InsertColumn(0, 'Keywords', width = 200)
        self.the_list.InsertColumn(1, 'Notes',width = 500)
        self.the_list.InsertColumn(2, ' Saved On ' ,width = 100)
        self.updateList()


    def _do_layout(self):
        self.res = xrc.XmlResource( GUI_FILENAME )
        self.frame = self.res.LoadFrame( None,  GUI_MAINFRAME_NAME )
        self.SetTopWindow(self.frame)
        self.frame.Show()
        self.go_button =  xrc.XRCCTRL(self.frame, "go_button")
        self.choice = xrc.XRCCTRL( self.frame, "the_choice")        
        self.frame.Bind(wx.EVT_BUTTON, self.delegateResult, self.go_button)

        self.addnote_button = xrc.XRCCTRL( self.frame, "add_note_button")
        self.frame.Bind(wx.EVT_BUTTON, self.addNote, self.addnote_button)

        self.save_all = xrc.XRCCTRL( self.frame, "save_all")
        self.Bind(wx.EVT_TOOL, self.insertToDb, self.save_all)
        
        self.toolbar = xrc.XRCCTRL( self.frame, "the_toolbar")
#        self.toolbar.EnableTool(self.save_all, False)

        self.all_notes = xrc.XRCCTRL( self.frame, "all_notes_text")
        self.keywords_text = xrc.XRCCTRL( self.frame, "keywords_text")

        self.frame.Maximize()


    def delegateResult(self,event):
        if (self.choice.GetStringSelection()=="Articles"):
            self.getArticleResult(event)
        else:
            self.getAnswersResult(event)

    def getArticleResult(self, event):
        self.articleResults.Clear()
        self.keyword = self.txt.GetValue().replace(" ","+")
        thread.start_new_thread(self.fetcharticle, (self.keyword,))

    def fetcharticle(self, keyword):
        articlelist = [Ezine, Dashboard, Snatch, ABase, Buzzle]
        def remBlanks(text):
            text.replace("\n\n\n", "\n")
            
            
        for model in articlelist:
            art = model()
            art.fetchArticle(self.keyword)
            article = art.article
            article = map(str, article)
            article = map(html2text.html2text, article)
            wx.CallAfter(self.updateArticleUI, article)

    def updateArticleUI(self,article):
        self.articleResults.AppendText(article[0] + article[1] + article[2])
        self.articleResults.AppendText(self.separator)


    def getAnswersResult(self, event):
        self.articleResults.Clear()
        self.keyword = self.txt.GetValue().replace(" ","+")
        thread.start_new_thread(self.fetchanswers,(self.keyword,))

        
    def fetchanswers(self, keyword):
        app = Answers()
        app.appid = "e0U05XjV34HKgxTrrFSZORdBbZPvFdBNR1gx1rd9vsnGc1ph2LjV3kQlUpObW8cSBPc-"
        result = app.questionSearch({'query': keyword, 'search_in':'best_answer', 'results' : '20' })
        wx.CallAfter(self.updateAnswersUI, result)


    def updateAnswersUI(self,result):
        def resultize(text):
            return html2text.html2text(text).encode('utf8')

        for res in result:
            self.articleResults.AppendText("Question:\n" + res['Subject'] + resultize(res['Content']) + "\nAnswer:\n" +resultize(res['ChosenAnswer']) + "\n\n" + self.separator )




# Notes addition and database stuff

    def addNote(self, event):
        note= self.resnote.GetValue()
        self.allnotes.AppendText("*" + note + "\n\n")
        self.resnote.Clear()



    def insertToDb(self, event):
        self.the_list.DeleteAllItems()
        self.conn = sqlite3.connect('db')
        self.c = self.conn.cursor()
        self.c.execute(""" create table if not exists notes (id integer primary key autoincrement not null, keywords string, notes string, date string)""")
        self.conn.commit()
        notes = self.all_notes.GetValue()
        keywords  = self.keywords_text.GetValue()
        self.c.execute(""" insert into notes(keywords, notes, date) values (?, ?,?) """ , (keywords, notes, getTime()))


        self.c.execute(""" select * from notes""")

        for i in self.c.fetchall():
            index = self.the_list.InsertStringItem(sys.maxint, i[1])
            self.the_list.SetStringItem(index, 1, i[2])
            self.the_list.SetStringItem(index, 2, i[3])
        self.conn.commit()
        self.c.close()
        self.conn.close()


    def updateList(self):
        self.the_list.DeleteAllItems()
        self.conn = sqlite3.connect('db')
        self.c = self.conn.cursor()
        self.c.execute(""" create table if not exists notes (id integer primary key autoincrement not null, keywords string,  notes string , date string)""")
        self.c.execute(""" select * from notes""")

        for i in self.c.fetchall():
            index = self.the_list.InsertStringItem(sys.maxint, i[1])
            self.the_list.SetStringItem(index, 1, i[2])
            self.the_list.SetStringItem(index, 2, i[3])

        self.conn.commit()
        self.c.close()
        self.conn.close()


        
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
