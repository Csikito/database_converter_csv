import mysql.connector
import wx
import wx.grid as grid
from src.config_loader import load_database_config
from src.export_csv_file import export_tables


class DatabaseConverter(wx.Frame):
    def __init__(self, parent, title):
        super(DatabaseConverter, self).__init__(parent, title=title, size=(300, 400))
        
        # Load the database
        db_config = load_database_config()

        # Create a database connection
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()

        # Query tables
        self.cursor.execute("SHOW TABLES")
        tables = [table[0] for table in self.cursor.fetchall()]
       
        # Defining Panel and BoxSizer
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Create a table
        self.grid = wx.grid.Grid(panel, style=wx.LC_REPORT)
        self.grid.CreateGrid(len(tables), 2)  
        self.grid.SetColLabelValue(0, " ")
        self.grid.SetColLabelValue(1, "Tables")

        # Add Checkboxes and Table Names
        self.grid.SetColFormatBool(0)
        for index, table in enumerate(tables):
            self.grid.SetCellValue(index, 1, table)

        # Removing serial numbers
        self.grid.SetRowLabelSize(0)

        # Display table
        vbox.Add(self.grid, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(vbox)

        # Save btn
        save_button = wx.Button(panel, label="Save")
        save_button.Bind(wx.EVT_BUTTON, self.export_tables)
        vbox.Add(save_button, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)
        panel.SetSizer(vbox)
    
    
    def export_tables(self, event):
        export_tables(self.grid, self.cursor)

    
        self.conn.close()
        self.Destroy()