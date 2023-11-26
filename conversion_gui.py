# path/filename: conversion_gui.py

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from bulk_converter import BulkConverter
import threading

class ConversionGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("XLSX to Text Converter")
        self.master.configure(background='#f0f0f0')

        self.file_paths = []  # Store selected file paths
        self.output_directory = ''  # Store output directory
        self.conversion_complete = threading.Event()  # Event to track conversion completion


        # Initialize GUI components
        self.init_widgets()

    def init_widgets(self):
        padding = {'padx': 10, 'pady': 10}  # Padding for widgets

        # File Selection Interface
        self.file_label = tk.Label(self.master, text="Select Files:", bg='#f0f0f0')
        self.file_label.pack(**padding)

        self.file_button = tk.Button(self.master, text="Browse", command=self.select_files)
        self.file_button.pack(**padding)

        self.file_listbox = tk.Listbox(self.master)
        self.file_listbox.pack(padx=10, pady=5, fill='both', expand=True)

        # Output Configuration
        self.output_label = tk.Label(self.master, text="Output Directory:", bg='#f0f0f0')
        self.output_label.pack(**padding)

        self.output_button = tk.Button(self.master, text="Browse", command=self.select_output_directory)
        self.output_button.pack(**padding)

        self.output_entry = tk.Entry(self.master, state='readonly')
        self.output_entry.pack(padx=10, pady=5, fill='x')

        # Delimiter Selection
        self.delimiter_label = tk.Label(self.master, text="Custom Delimiter:", bg='#f0f0f0')
        self.delimiter_label.pack(**padding)

        self.delimiter_entry = tk.Entry(self.master)
        self.delimiter_entry.pack(padx=10, pady=5, fill='x')

        # Thread Count Configuration
        self.thread_label = tk.Label(self.master, text="Number of Threads:", bg='#f0f0f0')
        self.thread_label.pack(**padding)

        self.thread_spinbox = tk.Spinbox(self.master, from_=1, to=16)  # Allows values from 1 to 16
        self.thread_spinbox.pack(padx=10, pady=5, fill='x')

        # Progress Bar
        self.progress_label = tk.Label(self.master, text="Conversion Progress:", bg='#f0f0f0')
        self.progress_label.pack(**padding)

        self.progress_bar = ttk.Progressbar(self.master, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress_bar.pack(padx=10, pady=5, fill='x')

        # Add some space before the Start Conversion button
        self.space_label = tk.Label(self.master, bg='#f0f0f0')
        self.space_label.pack(**padding)

        # Start Conversion Button
        self.convert_button = tk.Button(self.master, text="Start Conversion", command=self.start_conversion)
        self.convert_button.pack(**padding)

    def select_files(self):
        self.file_paths = filedialog.askopenfilenames()
        self.file_listbox.delete(0, tk.END)
        for file in self.file_paths:
            self.file_listbox.insert(tk.END, file)
        

    def select_output_directory(self):
        self.output_directory = filedialog.askdirectory()
        self.output_entry.config(state='normal')
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_directory)
        self.output_entry.config(state='readonly')

    def update_progress_bar(self, increment):
        current_value = self.progress_bar['value']
        new_value = current_value + increment
        max_value = len(self.file_paths)
        self.progress_bar['value'] = min(new_value, max_value)
        self.master.update_idletasks()

    def start_conversion(self):
        if not self.file_paths or not self.output_directory:
            messagebox.showwarning("Warning", "Please select files and an output directory")
            return

        self.progress_bar['value'] = 0  # Reset progress bar
        self.master.update_idletasks()
        self.conversion_complete.clear()  # Reset conversion completion status
        
        
        # Fetch values from GUI components
        custom_delimiter = self.delimiter_entry.get()
        num_threads = int(self.thread_spinbox.get())

        # Use the fetched values in the conversion process
        def conversion_task():
            converter = BulkConverter(
                output_dir=self.output_directory,
                delimiter=custom_delimiter,
                max_threads=num_threads,
                progress_callback=self.update_progress_bar
            )
            # Start the conversion process
            results = converter.convert_xlsx_to_text(self.file_paths)
            self.conversion_complete.set()  # Update conversion completion status
            self.master.after(0, self.handle_conversion_results, results)

        # Run the conversion task in a separate thread
        threading.Thread(target=conversion_task, daemon=True).start()

    def handle_conversion_results(self, results):
        # This will be called after the conversion is done
        if self.conversion_complete.is_set():  # Check if the conversion is actually complete
            if all(results):
                messagebox.showinfo("Success", "Conversion completed successfully")
            elif any(results):
                messagebox.showwarning("Warning", "Some files could not be converted")
            else:
                messagebox.showerror("Error", "Conversion failed")
            self.progress_bar['value'] = 0  # Reset progress bar


def main():
    root = tk.Tk()
    app = ConversionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()