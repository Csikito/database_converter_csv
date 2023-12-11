import wx
from src.databaseConverter import DatabaseConverter


if __name__ == '__main__':
    app = wx.App(False)
    frame = DatabaseConverter(None, "Database Tables")
    frame.Show()
    app.MainLoop()