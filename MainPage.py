
# Useful References
#scrollable frames: https://www.geeksforgeeks.org/python/scrollable-frames-in-tkinter/
# switching frames (Make frame for each type):https://www.tutorialspoint.com/article/how-to-switch-between-two-frames-in-tkinter
# responsive sizing: https://medium.com/@anushka25comp/designing-responsive-guis-in-tkinter-b609b6ab7a51

""" Plan
# 

"""
import tkinter as tk
# this contains more widgets we can use.
from tkinter import ttk
# Using this to display images
from PIL import Image, ImageTk
from AddReviews import open_review_form


def display(event):
    item = modeDropdown.get()
    print(item)
    if item == "Restaurants":
        moviefilterDropdown.pack_forget()
        TvShowfilterDropdown.pack_forget()
        movieFrame.pack_forget()
        tvFrame.pack_forget()
        displayRestaurants()
    if item == "Movies":
        restaurantfilterDropdown.pack_forget()
        TvShowfilterDropdown.pack_forget()
        tvFrame.pack_forget()
        restaurantFrame.pack_forget()
        displayMovies()
    if item == "TV-shows":
        restaurantfilterDropdown.pack_forget()
        moviefilterDropdown.pack_forget()
        restaurantFrame.pack_forget()
        movieFrame.pack_forget()
        displayTVShows()

def displayRestaurants():
    restaurantfilterDropdown.pack()
    for i in range(0,10):
        restaurantFrame.pack(pady="20")
        nameLabel = tk.Label(restaurantFrame, text="Name: Restaurant", bg="light grey", fg="black")
        ratingLabel = tk.Label(restaurantFrame, text="Rating: 8", bg="light grey", fg="black")
        reviewLabel = tk.Label(restaurantFrame, text="Review: Nice Restaurant!", bg="light grey", fg="black")
        addressLabel = tk.Label(restaurantFrame, text="Address: 123 Street", bg="light grey", fg="black")
        cuisineLabel = tk.Label(restaurantFrame, text="Cuisine: Indian", bg="light grey", fg="black")
        addButton = tk.Button(restaurantFrame, text="add review", bg="light grey", command=lambda: open_review_form(mainWindow, "Restaurant"))
        deleteButton = tk.Button(restaurantFrame, text="delete review", bg="light grey")
        editButton = tk.Button(restaurantFrame, text="edit review", bg="light grey")
        imageLabel = tk.Label(restaurantFrame, image=ImagePR)
        imageLabel.pack()
        nameLabel.pack()
        ratingLabel.pack()
        reviewLabel.pack()
        addressLabel.pack()
        cuisineLabel.pack()
        addButton.pack(pady="10")
        deleteButton.pack()
        editButton.pack(pady="10")
def displayMovies():
    moviefilterDropdown.pack()
    for i in range(0,10):
        movieFrame.pack( pady="10")
        nameLabel = tk.Label(movieFrame, text="Name: Movie", bg="light grey", fg="black")
        ratingLabel = tk.Label(movieFrame, text="Rating: 8", bg="light grey", fg="black")
        reviewLabel = tk.Label(movieFrame, text="Review: Nice Movie!", bg="light grey", fg="black")
        filmLengthLabel = tk.Label(movieFrame, text="Length: 2 hrs 10 min", bg="light grey", fg="black")
        genreLabel = tk.Label(movieFrame, text="Genre: action", bg="light grey", fg="black")
        addButton = tk.Button(movieFrame, text="add review", bg="light grey", command=lambda: open_review_form(mainWindow, "Movie"))
        deleteButton = tk.Button(movieFrame, text="delete review", bg="light grey")
        editButton = tk.Button(movieFrame, text="edit review", bg="light grey")
        imageLabel = tk.Label(movieFrame, image=ImagePM)
        imageLabel.pack()
        nameLabel.pack()
        ratingLabel.pack()
        reviewLabel.pack()
        filmLengthLabel.pack()
        genreLabel.pack()
        addButton.pack(pady="10")
        deleteButton.pack()
        editButton.pack(pady="10")
def displayTVShows():
    TvShowfilterDropdown.pack()
    for i in range(0,10):
        tvFrame.pack( pady="10")
        nameLabel = tk.Label( tvFrame, text="Name: TV show", bg="light grey", fg="black")
        ratingLabel = tk.Label( tvFrame, text="Rating: 8",  bg="light grey", fg="black")
        reviewLabel = tk.Label( tvFrame, text="Review: Nice Show!", bg="light grey", fg="black")
        numberOfEpisodesLabel = tk.Label(tvFrame, text="NumberEps: 10", bg="light grey", fg="black")
        genreLabel = tk.Label( tvFrame, text="Genre: action", bg="light grey", fg="black")
        addButton = tk.Button( tvFrame, text="add review", bg="light grey", command=lambda: open_review_form(mainWindow, "TV show"))
        deleteButton = tk.Button(tvFrame, text="delete review", bg="light grey")
        editButton = tk.Button( tvFrame, text="edit review", bg="light grey")
        imageLabel = tk.Label( tvFrame, image=ImagePT)
        imageLabel.pack()
        nameLabel.pack()
        ratingLabel.pack()
        reviewLabel.pack()
        numberOfEpisodesLabel.pack()
        genreLabel.pack()
        addButton.pack(pady="10")
        deleteButton.pack()
        editButton.pack(pady="10")
mainWindow = tk.Tk()
# this sets starting window size
mainWindow.geometry("400x400")

# mode selector 
modeDropdown = ttk.Combobox(mainWindow, values=["Get reviews", "Restaurants", "Movies", "TV-shows"], state="readonly")
modeDropdown.set("Get reviews")
print(modeDropdown.get())
# Important to remember must use: "<<ComboboxSelected>>" string exactly to get event to work.
modeDropdown.bind("<<ComboboxSelected>>", display)
restaurantfilterDropdown = ttk.Combobox(mainWindow, values=["Filter", "Highest/Lowest", "Lowest/Highest", "Range", "Name", "address", "Cuisine"], state="readonly")
restaurantfilterDropdown.set("Filter")
moviefilterDropdown = ttk.Combobox(mainWindow, values=["Filter", "Highest/Lowest", "Lowest/Highest", "Range", "Name", "Genre", "movieLength"], state="readonly")
moviefilterDropdown.set("Filter")
TvShowfilterDropdown = ttk.Combobox(mainWindow, values=["Filter", "Highest/Lowest", "Lowest/Highest", "Range", "Name", "Genre", "numberofEps"], state="readonly")
TvShowfilterDropdown.set("Filter")
modeDropdown.pack()
restaurantfilterDropdown.pack_forget()
moviefilterDropdown.pack_forget()
TvShowfilterDropdown.pack_forget()
# Search bar
searchFrame = tk.Frame(mainWindow)
searchInput = tk.Entry(searchFrame)
button = tk.Button(searchFrame, text="Search")
# fill changes with window size, this is in the horizontal direction.
searchFrame.pack(fill="x")
searchInput.pack(fill="x")
button.pack()


# Make the scrollable frame to store the frames
canvas = tk.Canvas(mainWindow)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(mainWindow, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

#add the scrollbar to canvas
canvas.configure(yscrollcommand=scrollbar.set)
scrollableFrame = tk.Frame(canvas)
# anchor tells us where to start putting elements, nw means top left.
# this puts the frame in the canvas at x=0, y=0 in the canvas.
canvas.create_window((0,0), window=scrollableFrame,  anchor="nw")

# bbox("all") is used to make the scroll area bigger.
scrollableFrame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

restaurantFrame = tk.Frame(scrollableFrame, bg="light grey")


tvFrame = tk.Frame(scrollableFrame, bg="light grey")


movieFrame = tk.Frame(scrollableFrame, bg="light grey")

imageFile = Image.open("./images/restaurantTestImage.jpg")
smallResImage = imageFile.resize((200, 200))
  # there is a bug if this is not globally referenced.
ImagePR = ImageTk.PhotoImage(smallResImage)

imageFile2 = Image.open("./images/movie.jpg")
smallMovieImage = imageFile2.resize((200, 200))
  # there is a bug if this is not globally referenced.
ImagePM = ImageTk.PhotoImage(smallMovieImage)

imageFile3 = Image.open("./images/tv.jpg")
smallTImage = imageFile3.resize((200, 200))
  # there is a bug if this is not globally referenced.
ImagePT = ImageTk.PhotoImage(smallTImage)

# this keeps the window open and events are handles
mainWindow.mainloop()









