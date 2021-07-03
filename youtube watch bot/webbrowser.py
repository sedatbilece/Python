import webbrowser ,time



url="https://www.youtube.com/watch?v=OAk9RJk06Y4"
dur=5
again=5

for i in range(again):
    webbrowser.open_new(url)
    time.sleep(dur)