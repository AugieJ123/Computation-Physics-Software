import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import pandas as pd
import numpy as np


def resource_path(relative_path) -> str:
    """Find the path of the ui fine..."""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class HomeScreen(QMainWindow):
    '''
        Responsible for the home screen...
    '''
    def __init__(self):
        super(HomeScreen, self).__init__()
        self.ui = loadUi(resource_path("exp_phy_soft.ui"), self)
        self.ui.setWindowTitle("Experimental Physics Software")

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering point
        self.move(qr.topLeft())

        #------------------------- Simple pendulum buttons section ---------------------#
        self.ui.file_btn.clicked.connect(self.s_choose_file)
        self.ui.no_table_graph_btn.clicked.connect(self.s_plot_no_table_data)
        self.ui.table_graph_btn.clicked.connect(self.s_plot_table_data)
        #-------------------------------------------------------------------------------#

        #------------------------- Hooke's Law buttons section -------------------------#
        self.ui.file_btn_2.clicked.connect(self.h_choose_file)
        self.ui.no_table_graph_btn_2.clicked.connect(self.h_plot_no_table_data)
        self.ui.table_graph_btn_2.clicked.connect(self.h_plot_table_data)
        #-------------------------------------------------------------------------------#

        #------------------------- Newton's Cooling buttons section --------------------#
        self.ui.file_btn_3.clicked.connect(self.n_choose_file)
        self.ui.no_table_graph_btn_3.clicked.connect(self.n_plot_no_table_data)
        self.ui.table_graph_btn_3.clicked.connect(self.n_plot_table_data)
        #-------------------------------------------------------------------------------#

    #--------------------------- Beginning of simple pendulum section ------------------#

    def s_choose_file(self) -> str:
        """
            Responsible for choosing the data file and store the path.
        """

        file_filter: str = (
            "Choose the data file(*.csv *.xlsx);; Data File(*.csv, *.xlsx)"
        )
        self.file_path = QFileDialog.getOpenFileName(
            parent=self,
            caption="Choose the data file",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter="data file(*.csv *.xlsx)",
        )

        self.file_path: str = self.file_path[0]

        # Check if the file format is csv or xlsx
        if self.file_path.split(".")[-1] not in ["csv", "xlsx"]:
            # Do a QMessage box
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Please select the right file format.")
            msg.setIcon(QMessageBox.Warning)

            x: int = msg.exec_()

        else:
            self.ui.data_file_path.setText(self.file_path)
            self.s_data_table(self.file_path)

        return self.file_path

    def s_data_table(self, file_path: str):
        """
            Responsible for passing the data from the file to the table...
        """

        if file_path.split(".")[-1] == "xlsx":
            workbook = pd.read_excel(file_path)
            self.ui.tableWidget.setRowCount(workbook.shape[0])
            self.ui.tableWidget.setColumnCount(workbook.shape[1])
            self.ui.tableWidget.setHorizontalHeaderLabels(workbook.columns)

            for row in workbook.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    table_item = QTableWidgetItem(str(value))
                    self.ui.tableWidget.setItem(row[0], col_index, table_item)

        else:
            workbook = pd.read_csv(file_path)
            self.ui.tableWidget.setRowCount(workbook.shape[0])
            self.ui.tableWidget.setColumnCount(workbook.shape[1])
            self.ui.tableWidget.setHorizontalHeaderLabels(workbook.columns)

            for row in workbook.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    tableItem = QTableWidgetItem(str(value))
                    self.ui.tableWidget.setItem(row[0], col_index, tableItem)

        return workbook

    def s_plot_no_table_data(self):
        """Plot the data that passes through the horizontal and vertical axes..."""

        horizontal_axis_values: list = []
        vertical_axis_values: list = []

        # Having the horizontal axis values
        horiz_1: str = self.ui.hori_1.text()
        horiz_2: str = self.ui.hori_2.text()
        horiz_3: str = self.ui.hori_3.text()
        horiz_4: str = self.ui.hori_4.text()
        horiz_5: str = self.ui.hori_5.text()
        horiz_6: str = self.ui.hori_6.text()
        horiz_7: str = self.ui.hori_7.text()
        horiz_8: str = self.ui.hori_8.text()
        horiz_9: str = self.ui.hori_9.text()
        horiz_10: str = self.ui.hori_10.text()

        horizontal_values: list = [
            horiz_1,
            horiz_2,
            horiz_3,
            horiz_4,
            horiz_5,
            horiz_6,
            horiz_7,
            horiz_8,
            horiz_9,
            horiz_10,
        ]

        for hori_value in horizontal_values:
            if hori_value != "":
                float_hori_value: float = float(hori_value)
                horizontal_axis_values.append(float_hori_value)

        # Having the vertical axis values
        vert_1: str = self.ui.vert_1.text()
        vert_2: str = self.ui.vert_2.text()
        vert_3: str = self.ui.vert_3.text()
        vert_4: str = self.ui.vert_4.text()
        vert_5: str = self.ui.vert_5.text()
        vert_6: str = self.ui.vert_6.text()
        vert_7: str = self.ui.vert_7.text()
        vert_8: str = self.ui.vert_8.text()
        vert_9: str = self.ui.vert_9.text()
        vert_10: str = self.ui.vert_10.text()

        vertical_values: list = [
            vert_1,
            vert_2,
            vert_3,
            vert_4,
            vert_5,
            vert_6,
            vert_7,
            vert_8,
            vert_9,
            vert_10,
        ]

        for vert_value in vertical_values:
            if vert_value != "":
                float_vert_value: float = float(vert_value)
                vertical_axis_values.append(float_vert_value)

        if len(horizontal_axis_values) == len(vertical_axis_values):
            # Plot the graph
            self.graph.clear()
            plt = self.graph
            plt.setTitle("Simple Pendulum", size="20px")
            plt.setLabel("left", "Time (seconds square)")
            plt.setLabel("bottom", "Length (meters)")
            plt.showGrid(x=True, y=True)
            graph = self.graph.plot(horizontal_axis_values, vertical_axis_values)

            # Find the gradient or slope of the graph
            slope = np.gradient(horizontal_axis_values, vertical_axis_values)
            print(slope)
            correct_slope = all(element == slope[0] for element in slope)
            self.ui.slope_value.clear()
            if correct_slope:
                self.ui.slope_value.setText(str(round(slope[0], 4)))

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(
                    f"The slope of the points are not the same when rounded to the nearest whole number or a one decimal point.\n The slope are {slope}"
                    )
                msg.setIcon(QMessageBox.Warning)

                x: int = msg.exec_()

                return x

            return graph

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The number of values of the horizontal and vertical axis must be the same... ")
            msg.setIcon(QMessageBox.Warning)

            x: int = msg.exec_()

            return x

    def s_plot_table_data(self):
        """Plot the data that passes through the table for the simple pendulum"""

        horizontal_axis_values: list = []
        vertical_axis_values: list = []

        file_path = self.file_path
        workbook_values = self.s_data_table(file_path)
        keys = workbook_values.keys()

        horizontal_axis_values: list = workbook_values[keys[0]].to_list()
        vertical_axis_values: list = workbook_values[keys[-1]].to_list()

            # Plot the graph
        if len(horizontal_axis_values) == len(vertical_axis_values):
            self.graph.clear()
            plt = self.graph
            plt.setTitle("Simple Pendulum", size="20px")
            plt.setLabel("left", "Time (seconds square)")
            plt.setLabel("bottom", "Length (meters)")
            plt.showGrid(x=True, y=True)
            graph = self.graph.plot(horizontal_axis_values, vertical_axis_values)

            # Find the gradient or slope of the graph
            slope = np.gradient(horizontal_axis_values, vertical_axis_values)
            print(slope)
            correct_slope = all(round(element, 1) == round(slope[0], 1) for element in slope)
            if correct_slope:
                self.ui.slope_value.clear()
                self.ui.slope_value.setText(str(round(slope[0], 4)))

            return graph

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The number of values of the horizontal and vertical axis must be the same... ")
            msg.setIcon(QMessageBox.Warning)

            x: int = msg.exec_()

            return x
   
    #--------------------------- End of simple pendulum section -------------------------#

    #--------------------------- Beginning of hooke's law section -----------------------#

    def h_choose_file(self) -> str:
        """
            Responsible for choosing the data file and store the path.
        """

        file_filter: str = (
            "Choose the data file(*.csv *.xlsx);; Data File(*.csv, *.xlsx)"
        )
        self.file_path = QFileDialog.getOpenFileName(
            parent=self,
            caption="Choose the data file",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter="data file(*.csv *.xlsx)",
        )

        self.file_path: str = self.file_path[0]

        # Check if the file format is csv or xlsx
        if self.file_path.split(".")[-1] not in ["csv", "xlsx"]:
            # Do a QMessage box
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Please select the right file format.")
            msg.setIcon(QMessageBox.Warning)

            x: int = msg.exec_()

        else:
            self.ui.data_file_path_2.setText(self.file_path)
            self.h_data_table(self.file_path)

        return self.file_path
    
    def h_data_table(self, file_path: str):
        """
            Responsible for passing the data from the file to the table...
        """

        if file_path.split(".")[-1] == "xlsx":
            workbook = pd.read_excel(file_path)
            self.ui.tableWidget_2.setRowCount(workbook.shape[0])
            self.ui.tableWidget_2.setColumnCount(workbook.shape[1])
            self.ui.tableWidget_2.setHorizontalHeaderLabels(workbook.columns)

            for row in workbook.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    table_item = QTableWidgetItem(str(value))
                    self.ui.tableWidget_2.setItem(row[0], col_index, table_item)

        else:
            workbook = pd.read_csv(file_path)
            self.ui.tableWidget_2.setRowCount(workbook.shape[0])
            self.ui.tableWidget_2.setColumnCount(workbook.shape[1])
            self.ui.tableWidget_2.setHorizontalHeaderLabels(workbook.columns)

            for row in workbook.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    tableItem = QTableWidgetItem(str(value))
                    self.ui.tableWidget_2.setItem(row[0], col_index, tableItem)

        return workbook

    def h_plot_table_data(self):
        """Plot the data that passes through the table for the simple pendulum"""

        horizontal_axis_values: list = []
        vertical_axis_values: list = []

        file_path = self.file_path
        workbook_values = self.h_data_table(file_path)
        keys = workbook_values.keys()

        horizontal_axis_values: list = workbook_values[keys[0]].to_list()
        vertical_axis_values: list = workbook_values[keys[-1]].to_list()

            # Plot the graph
        if len(horizontal_axis_values) == len(vertical_axis_values):
            self.graph.clear()
            plt = self.graph_2
            plt.setTitle("Hooke's Law", size="20px")
            plt.setLabel("left", "Time (seconds square)")
            plt.setLabel("bottom", "Length (meters)")
            plt.showGrid(x=True, y=True)
            graph = self.graph_2.plot(horizontal_axis_values, vertical_axis_values)

            # Find the gradient or slope of the graph
            slope = np.gradient(horizontal_axis_values, vertical_axis_values)
            print(slope)
            correct_slope = all(round(element, 1) == round(slope[0], 1) for element in slope)
            if correct_slope:
                self.ui.slope_value_2.clear()
                self.ui.slope_value_2.setText(str(round(slope[0], 1)))

            return graph

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The number of values of the horizontal and vertical axis must be the same... ")
            msg.setIcon(QMessageBox.Warning)

            x: int = msg.exec_()

            return x

    def h_plot_no_table_data(self):
        """Plot the data that passes through the horizontal and vertical axes..."""

        horizontal_axis_values: list = []
        vertical_axis_values: list = []

        # Having the horizontal axis values
        horiz_11: str = self.ui.hori_11.text()
        horiz_12: str = self.ui.hori_12.text()
        horiz_13: str = self.ui.hori_13.text()
        horiz_14: str = self.ui.hori_14.text()
        horiz_15: str = self.ui.hori_15.text()
        horiz_16: str = self.ui.hori_16.text()
        horiz_17: str = self.ui.hori_17.text()
        horiz_18: str = self.ui.hori_18.text()
        horiz_19: str = self.ui.hori_19.text()
        horiz_20: str = self.ui.hori_20.text()

        horizontal_values: list = [
            horiz_11,
            horiz_12,
            horiz_13,
            horiz_14,
            horiz_15,
            horiz_16,
            horiz_17,
            horiz_18,
            horiz_19,
            horiz_20,
        ]

        for hori_value in horizontal_values:
            if hori_value != "":
                float_hori_value: float = float(hori_value)
                horizontal_axis_values.append(float_hori_value)

        # Having the vertical axis values
        vert_11: str = self.ui.vert_11.text()
        vert_12: str = self.ui.vert_12.text()
        vert_13: str = self.ui.vert_13.text()
        vert_14: str = self.ui.vert_14.text()
        vert_15: str = self.ui.vert_15.text()
        vert_16: str = self.ui.vert_16.text()
        vert_17: str = self.ui.vert_17.text()
        vert_18: str = self.ui.vert_18.text()
        vert_19: str = self.ui.vert_19.text()
        vert_20: str = self.ui.vert_20.text()

        vertical_values: list = [
            vert_11,
            vert_12,
            vert_13,
            vert_14,
            vert_15,
            vert_16,
            vert_17,
            vert_18,
            vert_19,
            vert_20,
        ]

        for vert_value in vertical_values:
            if vert_value != "":
                float_vert_value: float = float(vert_value)
                vertical_axis_values.append(float_vert_value)

        if len(horizontal_axis_values) == len(vertical_axis_values):
            # Plot the graph
            self.graph_2.clear()
            plt = self.graph
            plt.setTitle("Hooke's Law", size="20px")
            plt.setLabel("left", "Extension (meter)")
            plt.setLabel("bottom", "Length (meters)")
            plt.showGrid(x=True, y=True)
            graph = self.graph_2.plot(horizontal_axis_values, vertical_axis_values)

            # Find the gradient or slope of the graph
            slope = np.gradient(horizontal_axis_values, vertical_axis_values)
            print(slope)
            correct_slope = all(element == slope[0] for element in slope)
            self.ui.slope_value.clear()
            if correct_slope:
                self.ui.slope_value_2.setText(str(round(slope[0], 1)))

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(
                    f"The slope of the points are not the same when rounded to the nearest whole number or a one decimal point.\n The slope are {slope}"
                    )
                msg.setIcon(QMessageBox.Warning)

                x: int = msg.exec_()

                return x

            return graph

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The number of values of the horizontal and vertical axis must be the same... ")
            msg.setIcon(QMessageBox.Warning)

            x: int = msg.exec_()

            return x

    #--------------------------- End of hooke's law section -----------------------------#

    #--------------------------- Beginning of newton's cooling law section --------------#

    def n_choose_file(self) -> str:
        """
            Responsible for choosing the data file and store the path.
        """

        file_filter: str = (
            "Choose the data file(*.csv *.xlsx);; Data File(*.csv, *.xlsx)"
        )
        self.file_path = QFileDialog.getOpenFileName(
            parent=self,
            caption="Choose the data file",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter="data file(*.csv *.xlsx)",
        )

        self.file_path: str = self.file_path[0]

        # Check if the file format is csv or xlsx
        if self.file_path.split(".")[-1] not in ["csv", "xlsx"]:
            # Do a QMessage box
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Please select the right file format.")
            msg.setIcon(QMessageBox.Warning)

            x: int = msg.exec_()

        else:
            self.ui.data_file_path_3.setText(self.file_path)
            self.n_data_table(self.file_path)

        return self.file_path
    
    def n_data_table(self, file_path: str):
        """
            Responsible for passing the data from the file to the table...
        """

        if file_path.split(".")[-1] == "xlsx":
            workbook = pd.read_excel(file_path)
            self.ui.tableWidget_3.setRowCount(workbook.shape[0])
            self.ui.tableWidget_3.setColumnCount(workbook.shape[1])
            self.ui.tableWidget_3.setHorizontalHeaderLabels(workbook.columns)

            for row in workbook.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    table_item = QTableWidgetItem(str(value))
                    self.ui.tableWidget_3.setItem(row[0], col_index, table_item)

        else:
            workbook = pd.read_csv(file_path)
            self.ui.tableWidget_3.setRowCount(workbook.shape[0])
            self.ui.tableWidget_3.setColumnCount(workbook.shape[1])
            self.ui.tableWidget_3.setHorizontalHeaderLabels(workbook.columns)

            for row in workbook.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    tableItem = QTableWidgetItem(str(value))
                    self.ui.tableWidget_3.setItem(row[0], col_index, tableItem)

        return workbook

    def n_plot_table_data(self):
        """Plot the data that passes through the table for the simple pendulum"""

        horizontal_axis_values: list = []
        vertical_axis_values: list = []

        file_path = self.file_path
        workbook_values = self.h_data_table(file_path)
        keys = workbook_values.keys()

        horizontal_axis_values: list = workbook_values[keys[0]].to_list()
        vertical_axis_values: list = workbook_values[keys[-1]].to_list()

            # Plot the graph
        if len(horizontal_axis_values) == len(vertical_axis_values):
            self.graph_3.clear()
            plt = self.graph_3
            plt.setTitle("Newton's Cooling Law", size="20px")
            plt.setLabel("left", "Temperature (degree celsius)")
            plt.setLabel("bottom", "Elapse Time (seconds)")
            plt.showGrid(x=True, y=True)
            graph = self.graph_3.plot(horizontal_axis_values, vertical_axis_values)

            # Find the gradient or slope of the graph
            slope = np.gradient(horizontal_axis_values, vertical_axis_values)
            print(slope)
            correct_slope = all(round(element, 1) == round(slope[0], 1) for element in slope)
            if correct_slope:
                self.ui.slope_value_3.clear()
                self.ui.slope_value_3.setText(str(round(slope[0], 1)))

            return graph

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The number of values of the horizontal and vertical axis must be the same... ")
            msg.setIcon(QMessageBox.Warning)

            x: int = msg.exec_()

            return x

    def n_plot_no_table_data(self):
        """Plot the data that passes through the horizontal and vertical axes..."""

        horizontal_axis_values: list = []
        vertical_axis_values: list = []

        # Having the horizontal axis values
        horiz_21: str = self.ui.hori_21.text()
        horiz_22: str = self.ui.hori_22.text()
        horiz_23: str = self.ui.hori_23.text()
        horiz_24: str = self.ui.hori_24.text()
        horiz_25: str = self.ui.hori_25.text()
        horiz_26: str = self.ui.hori_26.text()
        horiz_27: str = self.ui.hori_27.text()
        horiz_28: str = self.ui.hori_28.text()
        horiz_29: str = self.ui.hori_29.text()
        horiz_30: str = self.ui.hori_30.text()

        horizontal_values: list = [
            horiz_21,
            horiz_22,
            horiz_23,
            horiz_24,
            horiz_25,
            horiz_26,
            horiz_27,
            horiz_28,
            horiz_29,
            horiz_30,
        ]

        for hori_value in horizontal_values:
            if hori_value != "":
                float_hori_value: float = float(hori_value)
                horizontal_axis_values.append(float_hori_value)

        # Having the vertical axis values
        vert_21: str = self.ui.vert_21.text()
        vert_22: str = self.ui.vert_22.text()
        vert_23: str = self.ui.vert_23.text()
        vert_24: str = self.ui.vert_24.text()
        vert_25: str = self.ui.vert_25.text()
        vert_26: str = self.ui.vert_26.text()
        vert_27: str = self.ui.vert_27.text()
        vert_28: str = self.ui.vert_28.text()
        vert_29: str = self.ui.vert_29.text()
        vert_30: str = self.ui.vert_30.text()

        vertical_values: list = [
            vert_21,
            vert_22,
            vert_23,
            vert_24,
            vert_25,
            vert_26,
            vert_27,
            vert_28,
            vert_29,
            vert_30,
        ]

        for vert_value in vertical_values:
            if vert_value != "":
                float_vert_value: float = float(vert_value)
                vertical_axis_values.append(float_vert_value)

        if len(horizontal_axis_values) == len(vertical_axis_values):
            # Plot the graph
            self.graph_3.clear()
            plt = self.graph_3
            plt.setTitle("Newton's Cooling Law", size="20px")
            plt.setLabel("left", "Temperature (degree celsius)")
            plt.setLabel("bottom", "Elapse Time (seconds)")
            plt.showGrid(x=True, y=True)
            graph = self.graph_3.plot(horizontal_axis_values, vertical_axis_values)

            # Find the gradient or slope of the graph
            slope = np.gradient(horizontal_axis_values, vertical_axis_values)
            print(slope)
            correct_slope = all(element == slope[0] for element in slope)
            self.ui.slope_value_3.clear()
            if correct_slope:
                self.ui.slope_value_3.setText(str(round(slope[0], 1)))

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(
                    f"The slope of the points are not the same when rounded to the nearest whole number or a one decimal point.\n The slope are {slope}"
                    )
                msg.setIcon(QMessageBox.Warning)

                x: int = msg.exec_()

                return x

            return graph

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The number of values of the horizontal and vertical axis must be the same... ")
            msg.setIcon(QMessageBox.Warning)

            x: int = msg.exec_()

            return x

    #--------------------------- End of newton's cooling law section -------------------#

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = HomeScreen()
    main.show()

    app.setApplicationName("Experimental Physics Software")
    app.exec()
