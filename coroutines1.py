def searcher():
    import time
    #Some 4 secs time consuming task.
    time.sleep(4.0)
    book = "This is a book of Shahab ud din named as Shahab nama. He was a top beaurucrate of Pakistan."

    while True:
        text = (yield)
        if text in book:
            print("Text is in the book.")
        else:
            print("Text is not the book.")

search = searcher()
next(search)
search.send("Shahab")
text = input("Now enter the text to find in the book.")
search.send(text)
text = input("Now enter the text to find in the book.")
search.send(text)
text = input("Now enter the text to find in the book.")
search.send(text)
search.close()
try:
    text = input("Now enter the text to find in the book.")
    search.send(text)
except StopIteration as e:
    print("Error occurred")
else:
    print("No error occurred.")
