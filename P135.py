import matplotlib.pyplot as plt
x=["Alice", "Chris", "Mary", "Matteo"]
y=[89,70,86,87]

def marks_line_chart():
    plt.plot(x,y)
    plt.title("Demo")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.show()
marks_line_chart()