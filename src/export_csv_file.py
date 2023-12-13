import wx
import os
import csv


def export_tables(grid, cursor):
    """
    Export selected database tables to CSV files.

    Parameters:
    - grid: wxPython Grid containing the database tables and checkboxes.
    - cursor: Cursor object for executing MySQL queries.

    The function iterates through the rows of the wxPython Grid and exports the
    tables corresponding to the checked checkboxes to CSV files. Each CSV file
    is saved in a separate folder named "csv" within the current working directory.

    Args:
    - grid (wx.grid.Grid): The wxPython Grid containing database tables and checkboxes.
    - cursor (mysql.connector.cursor.MySQLCursor): Cursor object for executing MySQL queries.

    """
    # Tables based on the checked fields.
    selected_tables = [grid.GetCellValue(item, 1) for item in range(grid.GetNumberRows()) if grid.GetCellValue(item, 0)]

    # Separate folder for CSV files
    output_folder = "csv"
    os.makedirs(output_folder, exist_ok=True)

    for table in selected_tables:
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        # Save CSV file
        csv_filename = os.path.join(output_folder, f"{table}.csv")
        with open(csv_filename, mode='w', newline='',
                  encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([i[0] for i in cursor.description])
            writer.writerows(rows)

    wx.MessageBox("CSV export completed!",
                  "Notification", wx.OK | wx.ICON_INFORMATION)
