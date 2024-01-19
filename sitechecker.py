import tkinter as tk
import urllib.request
# importing libraries

def siteChecker(): # main function to check site
    window = tk.Tk() # create window
    window.geometry("501x200") # set dimensions
    window.title("Site Connection Checker") # set title
    
    tk.Label(window, text="Site Connection Checker", font=("Playbill")).place(x=170, y=20) # create title

    def check_URL(): # function to actually check the status code of the url
        website = (url.get()) # get the url
        statusCode = urllib.request.urlopen(website).getcode() # get the status code
        if statusCode == 200: # if status is good
            tk.Label(window, text="Site Available").place(x=207, y=150) # create available label
        else: # else the status is not good
            tk.Label(window, text="Site Unavailable - Status Code: " + str(statusCode)).place(x=140, y=150) # create not available label
    url = tk.StringVar() # get url in a string
    tk.Entry(window, textvariable=url).place(x=126, y=60, height=25, width=250) # create the input box
    tk.Button(window, text='Check', command=check_URL).place(x=215, y=100) # create button
    window.mainloop() # tkinter mainloop
    
if __name__ == "__main__": # main function
    siteChecker()