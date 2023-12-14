import mysql.connector
import wx
import wx.grid as grid
from src.config_loader import load_database_config
from src.export_csv_file import export_tables


class DatabaseConverter(wx.Frame):
    """
    A graphical user interface for converting database tables and exporting them to CSV files.

    Attributes:
    - conn: MySQL database connection object.
    - cursor: Cursor object for executing MySQL queries.
    - grid: wxPython Grid for displaying database tables.
    """
    def __init__(self, parent, title):
        super(DatabaseConverter, self).__init__(
            parent, title=title, size=(300, 400)
        )

        # Load the database
        db_config = load_database_config()

        try:
            # Create a database connection
            self.conn = mysql.connector.connect(**db_config)
            self.cursor = self.conn.cursor()

            # Query tables
            self.cursor.execute("SHOW TABLES")
            self.tables = [table[0] for table in self.cursor.fetchall()]

            # Defining Panel and BoxSizer
            panel = wx.Panel(self)
            vbox = wx.BoxSizer(wx.VERTICAL)

            # Create a table
            self.grid = wx.grid.Grid(panel, style=wx.LC_REPORT)
            self.grid.CreateGrid(len(self.tables), 2)
            self.grid.SetColLabelValue(0, "✔")
            self.grid.SetColLabelValue(1, "Tables")

            # Add Checkboxes and Table Names
            self.grid.SetColFormatBool(0)
            for index, table in enumerate(self.tables):
                self.grid.SetCellValue(index, 1, table)
                self.grid.SetCellAlignment(
                    index, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE,
                )
                self.grid.SetCellAlignment(
                    index, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE,
                )

            # Removing serial numbers
            self.grid.SetRowLabelSize(0)

            # Setting the width of the first column
            self.grid.SetColSize(0, 30)

            # Set text size
            font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            self.grid.SetDefaultCellFont(font)

            # Automatically adjust cell size to text size
            self.grid.AutoSize()

            # Select a cell with one click
            self.grid.Bind(grid.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_click)

            # Display table
            vbox.Add(
                self.grid, proportion=1, flag=wx.EXPAND | wx.ALL, border=5
            )
            panel.SetSizer(vbox)

            # Save btn
            save_button = wx.Button(panel, label="Save")
            save_button.Bind(wx.EVT_BUTTON, self.export_tables)
            vbox.Add(save_button, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM,
                        border=10)
            panel.SetSizer(vbox)
        except mysql.connector.Error as e:
            # Connection to MySQL server failed
            wx.MessageBox(f"Failed to connect to the MySQL server: {e}",
                            "Error", wx.OK | wx.ICON_ERROR)
            self.Destroy()

    def on_cell_click(self, event):
        """
        Event handler for a left-click on a cell in the wxPython Grid.

        Parameters:
        - event: The wxPython event object.
        """
        row = event.GetRow()
        col = event.GetCol()

        self.grid.EnableCellEditControl()
        self.grid.SetGridCursor(row, col)
        event.Skip()

    def export_tables(self, event):
        """
        Event handler for the "Save" button click.

        Parameters:
        - event: The wxPython event object.
        """
        export_tables(self.grid, self.cursor, self.tables)
