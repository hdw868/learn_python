import os
import traceback

import Tkinter as tk
import tkFileDialog as filedialog
import tkMessageBox as messagebox
import ttk

import baseline_api
from scrollframe import VerticalScrolledFrame


class ImporterUI:
    def __init__(self, parent):
        """Create the GUI"""
        # Framework.
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame.grid()

        # Variable.
        self.test_suites = []
        self.test_suites_dict = {}
        self._ts_selected = []
        self.objects = []
        self.objects_dict = {}
        self._obj_selected = []
        self.all_obj = tk.IntVar()
        self.all_ts = tk.IntVar()
        self.ts_root = tk.StringVar()
        self.bs_path = tk.StringVar()
        self.dst_bs_name = tk.StringVar()

        # Widgets.
        self.src_label = ttk.Label(self.frame, text='Path of source baseline:')
        self.src_label.grid(row=0, column=0, padx=5, pady=5)
        self.src_entry = ttk.Entry(self.frame, width=50, textvariable=self.bs_path)
        self.src_entry.grid(row=0, column=1, padx=5, pady=5)
        self.src_button = ttk.Button(self.frame, text='Browse', command=self.src_fd)
        self.src_button.grid(row=0, column=2, padx=5, pady=5)

        self.dst_label = ttk.Label(self.frame, text='Root path of test suites:')
        self.dst_label.grid(row=0, column=4, padx=5, pady=5, sticky=tk.E)
        self.dst_entry = ttk.Entry(self.frame, width=50, textvariable=self.ts_root)
        self.dst_entry.grid(row=0, column=5, padx=5, pady=5)
        self.dst_button = ttk.Button(self.frame, text='Browse', command=self.dst_fd)
        self.dst_button.grid(row=0, column=6, padx=5, pady=5)
        # Row 1
        self.dst_bs_name_label = ttk.Label(self.frame,
                                           text='Name of the baseline (e.g: 2.VLDB):')
        self.dst_bs_name_label.grid(row=1, column=4, padx=5, pady=5)
        self.dst_bs_name_entry = ttk.Entry(self.frame, width=50, textvariable=self.dst_bs_name)
        self.dst_bs_name_entry.grid(row=1, column=5, padx=5, pady=5)

        # Row 2
        self.desc = ttk.Label(self.frame, text='Import Object(s) to Test-suite(s)')
        self.desc.grid(row=2, column=3, padx=5, pady=5)

        # Source Frame
        self.src_frame = VerticalScrolledFrame(self.frame, borderwidth=5, relief="groove")
        self.src_frame.grid(row=2, column=0, columnspan=3, ipady=128, sticky=(tk.N + tk.S + tk.E + tk.W))
        self.select_all_src = ttk.Checkbutton(self.frame, text='Select/Deselect All',
                                              command=self.select_all_obj,
                                              variable=self.all_obj)
        self.select_all_src.grid(row=3, column=0, padx=5, pady=5)

        # Destination Frame
        self.dst_frame = VerticalScrolledFrame(self.frame, height=500, borderwidth=5, relief="groove")
        self.dst_frame.grid(row=2, column=4, columnspan=3, ipady=128, sticky=(tk.N + tk.S + tk.E + tk.W))
        self.select_all_dst = ttk.Checkbutton(self.frame, text='Select/Deselect All',
                                              command=self.select_all_ts,
                                              variable=self.all_ts)
        self.select_all_dst.grid(row=3, column=4, padx=5, pady=5, sticky=tk.W)

        self.import_button = ttk.Button(self.frame, text='Import', command=self.apply)
        self.import_button.grid(row=1, column=6, padx=5, pady=5, sticky=tk.E)

        # Mainloop
        self.parent.mainloop()

    @property
    def obj_selected(self):
        self._obj_selected = []
        for obj, state in self.objects_dict.items():
            if state.get():
                self._obj_selected.append(obj)
        return self._obj_selected

    @property
    def ts_selected(self):
        self._ts_selected = []
        for test_suite, state in self.test_suites_dict.items():
            if state.get():
                self._ts_selected.append(test_suite)
        return self._ts_selected

    def select_all_obj(self):
        if self.all_obj.get():
            value = 1
        else:
            value = 0
        for test_suite, state in self.objects_dict.items():
            state.set(value)

    def select_all_ts(self):
        if self.all_ts.get():
            value = 1
        else:
            value = 0
        for test_suite, state in self.test_suites_dict.items():
            state.set(value)

    def get_test_suites(self):
        test_suites = [name for name in os.listdir(self.ts_root.get()) if
                       os.path.isdir("{}\{}".format(self.ts_root.get(), name))]
        return test_suites

    def get_baseline_obj(self):
        try:
            bs = baseline_api.BaseLine(self.bs_path.get(), strict=True)
            bs_objs = []
            for report in bs.reports:
                bs_objs.append(report)
            return bs_objs
        except Exception:
            messagebox.showerror(title="Caught exception",
                                 message=("Error while parsing xml file, please check if it is a valid baseline file.\n"
                                          + traceback.format_exc()))

    def load_src(self):
        # List the objects in checkbox
        self.objects = self.get_baseline_obj()
        # need to destroy children first to clear the content
        for widget in self.src_frame.interior.winfo_children():
            widget.destroy()
        for obj in self.objects:
            var = tk.IntVar()
            check = ttk.Checkbutton(self.src_frame.interior, text=obj.name, variable=var)
            check.pack(side='top', anchor=tk.W, padx=5)
            self.objects_dict[obj] = var

    def src_fd(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.bs_path.set(filename)
            self.load_src()

    def dst_fd(self):
        dirname = filedialog.askdirectory()
        if dirname:
            self.ts_root.set(dirname)
            self.load_dst()

    def load_dst(self):
        # List the test suites in checkbox
        self.test_suites = self.get_test_suites()
        # need to destroy children first to clear the content
        for widget in self.dst_frame.interior.winfo_children():
            widget.destroy()
        for test_suite in self.test_suites:
            var = tk.IntVar()
            check = ttk.Checkbutton(self.dst_frame.interior, text=test_suite, variable=var)
            check.pack(side='top', anchor=tk.W, padx=5)
            self.test_suites_dict[test_suite] = var

    def apply(self):
        if self.obj_selected and self.ts_selected and self.dst_bs_name.get():
            ret = baseline_api.insert_reports(reports=self.obj_selected,
                                              baseline_name=self.dst_bs_name.get(),
                                              test_suites=self.ts_selected)
            if not ret:
                messagebox.showinfo(message='Import object(s) to test suite(s) succeed!')
            else:
                messagebox.showerror(message='Import object(s) to test suite(s) failed! Please contact the author.')
        else:
            messagebox.showwarning(
                title='Incomplete arguments',
                message='You should select at least one object, one test suite and define the baseline name!')
        print('objects selected: %s' % self.obj_selected)
        print('test suites selected: %r' % self.ts_selected)
        print('baseline_name: %r' % self.dst_bs_name.get())


if __name__ == '__main__':
    window = tk.Tk()
    selector = ImporterUI(parent=window)
