"""Pop-up form for adding a review.

Usage from MainPage.py:
    from ReviewForm import open_review_form
    open_review_form(mainWindow, "Movie", on_submit=save_review)

on_submit is optional. It receives a dict like:
    {"category": "Movie", "name": "...", "rating": 8, "review": "...",
     "image": "/path/to/pic.jpg" or None, "Genre": "...", "Length": "..."}
If it is not given, the dict is just printed.
"""
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Extra fields shown for each category (match the labels on the review cards)
EXTRA_FIELDS = {
    "Restaurant": ["Address", "Cuisine"],
    "Movie": ["Genre", "Length"],
    "TV show": ["Genre", "Number of episodes"],
}


def open_review_form(parent, category, on_submit=None):
    print("ReviewForm v2 loaded from:", os.path.abspath(__file__))
    win = tk.Toplevel(parent)
    win.title(f"Add {category} review (v2)")
    win.minsize(440, 520)   # grows automatically if the content needs more room
    win.transient(parent)   # stay on top of the main window
    win.grab_set()          # block the main window until closed

    body = ttk.Frame(win, padding=15)
    body.pack(fill="both", expand=True)
    body.columnconfigure(1, weight=1)

    ttk.Label(body, text=f"Add a {category} review",
              font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2,
                                                   sticky="w", pady=(0, 12))

    fields = {}   # label -> ttk.Entry
    row = 1

    def add_entry(label):
        nonlocal row
        ttk.Label(body, text=label).grid(row=row, column=0, sticky="w", pady=4, padx=(0, 10))
        entry = ttk.Entry(body)
        entry.grid(row=row, column=1, sticky="ew", pady=4)
        fields[label] = entry
        row += 1

    add_entry("Name")

    # Rating 0-10
    ttk.Label(body, text="Rating (0-10)").grid(row=row, column=0, sticky="w", pady=4)
    ratingVar = tk.StringVar(value="8")
    ttk.Spinbox(body, from_=0, to=10, width=5, textvariable=ratingVar).grid(
        row=row, column=1, sticky="w", pady=4)
    row += 1

    # Category-specific fields
    for label in EXTRA_FIELDS.get(category, []):
        add_entry(label)

    # Review text
    ttk.Label(body, text="Review").grid(row=row, column=0, sticky="nw", pady=4)
    reviewText = tk.Text(body, height=6, wrap="word")
    reviewText.grid(row=row, column=1, sticky="ew", pady=4)
    row += 1

    # Optional image
    imagePath = {"value": None}

    def choose_image():
        path = filedialog.askopenfilename(
            parent=win, title="Choose an image",
            filetypes=[("Images", "*.png *.jpg *.jpeg *.gif"), ("All files", "*.*")])
        if path:
            imagePath["value"] = path
            imageLabel.config(text=os.path.basename(path))

    ttk.Label(body, text="Image").grid(row=row, column=0, sticky="w", pady=4)
    imgFrame = ttk.Frame(body)
    imgFrame.grid(row=row, column=1, sticky="ew", pady=4)
    imageLabel = ttk.Label(imgFrame, text="No image chosen")
    ttk.Button(imgFrame, text="Choose...", command=choose_image).pack(side="left")
    imageLabel.pack(side="left", padx=8)
    row += 1

    def submit():
        name = fields["Name"].get().strip()
        if not name:
            messagebox.showwarning("Missing name", "Please enter a name.", parent=win)
            return
        try:
            rating = int(ratingVar.get())
            if not 0 <= rating <= 10:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Invalid rating",
                                   "Rating must be a whole number from 0 to 10.", parent=win)
            return
        review = reviewText.get("1.0", "end").strip()
        if not review:
            messagebox.showwarning("Missing review", "Please write a review.", parent=win)
            return

        data = {"category": category, "name": name, "rating": rating,
                "review": review, "image": imagePath["value"]}
        for label in EXTRA_FIELDS.get(category, []):
            data[label] = fields[label].get().strip()

        if on_submit:
            on_submit(data)
        else:
            print(data)
        win.destroy()

    # Pinned to the bottom of the window so it can never be pushed off-screen
    buttons = ttk.Frame(win, padding=(15, 10))
    buttons.pack(side="bottom", fill="x", before=body)
    ttk.Button(buttons, text="Submit review", command=submit).pack(side="right")
    ttk.Button(buttons, text="Cancel", command=win.destroy).pack(side="right", padx=6)

    fields["Name"].focus()
    win.bind("<Escape>", lambda e: win.destroy())