import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from PIL import Image

class GUI_System:
    def __init__(self):
        # GUI Setup
        self.root = tk.Tk()
        self.root.title("Image Cropper & PDF Converter")
        self.root.geometry("700x500")
        self.root.configure(bg="#e3f2fd")
        self.root.resizable(False, False)

        self.source_var = tk.StringVar()
        self.target_var = tk.StringVar()
        self.target_pdf_var = tk.StringVar()

        self.x1_var = tk.StringVar(value="100")
        self.y1_var = tk.StringVar(value="50")
        self.x2_var = tk.StringVar(value="400")
        self.y2_var = tk.StringVar(value="300")

        title_label = tk.Label(self.root, text="Image Crop to PDF", font=("Arial", 16, "bold"), bg="#e3f2fd", fg="#1e88e5")
        title_label.pack(pady=10)

        frame = tk.Frame(self.root, bg="#e3f2fd")
        frame.pack(pady=10)

        def create_label_entry(parent, text, textvariable, row, col):
            tk.Label(parent, text=text, bg="#e3f2fd", font=("Arial", 10, "bold")).grid(row=row, column=col, padx=5,
                                                                                       pady=5,
                                                                                       sticky="w")
            tk.Entry(parent, textvariable=textvariable, width=10).grid(row=row, column=col + 1, padx=5, pady=5)

        tk.Label(frame, text="Source Folder:", bg="#e3f2fd", font=("Arial", 10, "bold")).grid(row=0, column=0,
                                                                                              sticky="w")
        tk.Entry(frame, textvariable=self.source_var, width=30).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Browse", command=self.select_source_folder, bg="#64b5f6", fg="white").grid(row=0, column=2,
                                                                                                     padx=5)

        tk.Label(frame, text="Target Folder:", bg="#e3f2fd", font=("Arial", 10, "bold")).grid(row=1, column=0,
                                                                                              sticky="w")
        tk.Entry(frame, textvariable=self.target_var, width=30).grid(row=1, column=1, padx=5)
        tk.Button(frame, text="Browse", command=self.select_target_folder, bg="#64b5f6", fg="white").grid(row=1, column=2,
                                                                                                     padx=5)


        tk.Label(frame, text="PDF Target Folder:", bg="#e3f2fd", font=("Arial", 10, "bold")).grid(row=2, column=0,
                                                                                              sticky="w")
        tk.Entry(frame, textvariable=self.target_pdf_var, width=30).grid(row=2, column=1, padx=5)
        tk.Button(frame, text="Browse", command=self.select_PDFtarget_folder, bg="#64b5f6", fg="white").grid(row=2,
                                                                                                          column=2,
                                                                                                          padx=5)
        tk.Label(frame, text="Crop Coordinates (x1, y1, x2, y2):", bg="#e3f2fd", font=("Arial", 10, "bold")).grid(row=3,
                                                                                                                  column=0,                                                                                    pady=5)

        create_label_entry(frame, "X1:", self.x1_var, 4, 0)
        create_label_entry(frame, "Y1:", self.y1_var, 4, 2)
        create_label_entry(frame, "X2:", self.x2_var, 5, 0)
        create_label_entry(frame, "Y2:", self.y2_var, 5, 2)

        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=500, mode="determinate")
        self.progress_bar.pack(pady=10)

        tk.Button(self.root, text="Crop Images", command=self.crop_images, bg="#43a047", fg="white", font=("Arial", 12, "bold"),
                  width=20).pack(pady=10)
        tk.Button(self.root, text="Convert to PDF", command=self.convert_to_pdf, bg="#1e88e5", fg="white",
                  font=("Arial", 12, "bold"),
                  width=20).pack(pady=10)

        tk.Label(self.root, text="Created by SERENGOKYILDIZ", bg="#e3f2fd", font=("Arial", 9, "italic")).pack(pady=10)

        self.root.mainloop()

    def select_source_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.source_var.set(folder)


    def select_target_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.target_var.set(folder)

    def select_PDFtarget_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.target_pdf_var.set(folder)

    def crop_images(self):
        source = self.source_var.get()
        target = self.target_var.get()

        if not source or not target:
            messagebox.showerror("Error", "Please select both source and target folders.")
            return

        os.makedirs(target, exist_ok=True)
        crop_coords = (
            int(self.x1_var.get()), int(self.y1_var.get()), int(self.x2_var.get()), int(self.y2_var.get())
        )

        files = [file for file in os.listdir(source) if file.lower().endswith((".png", ".jpg", ".jpeg"))]
        total_files = len(files)

        if total_files == 0:
            messagebox.showerror("Error", "No images found in source folder!")
            return

        self.progress_bar["maximum"] = total_files
        self.progress_bar["value"] = 0

        for i, file in enumerate(files):
            img_path = os.path.join(source, file)
            output_path = os.path.join(target, file)

            with Image.open(img_path) as img:
                cropped_img = img.crop(crop_coords)
                cropped_img.save(output_path)

            self.progress_bar["value"] = i + 1
            self.root.update_idletasks()

        messagebox.showinfo("Success", "Images cropped successfully!")
        self.progress_bar["value"] = 0

    def convert_to_pdf(self):
        target = self.target_var.get()
        targetPDF = self.target_pdf_var.get()
        if not target:
            messagebox.showerror("Error", "Please select the target folder.")
            return

        files = [f for f in os.listdir(target) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        files.sort()

        if not files:
            messagebox.showerror("Error", "No images found in target folder!")
            return

        self.progress_bar["maximum"] = len(files)
        self.progress_bar["value"] = 0

        first_img_path = os.path.join(target, files[0])
        first_img = Image.open(first_img_path).convert("RGB")
        extra_images = []

        for i, file in enumerate(files[1:]):
            img = Image.open(os.path.join(target, file)).convert("RGB")
            extra_images.append(img)
            self.progress_bar["value"] = i + 1
            self.root.update_idletasks()

        pdf_path = os.path.join(targetPDF, "output.pdf")
        first_img.save(pdf_path, save_all=True, append_images=extra_images)

        messagebox.showinfo("Success", f"PDF created: {pdf_path}")
        self.progress_bar["value"] = 0


UI = GUI_System()
