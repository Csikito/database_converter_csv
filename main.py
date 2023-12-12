import wx
from src.database_converter import DatabaseConverter


if __name__ == '__main__':
    app = wx.App(False)
    frame = DatabaseConverter(None, "Database Converter")
    frame.Show()
    app.MainLoop()