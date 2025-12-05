import matplotlib.pyplot as plt
s_n=["Sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Priya"]
s_m=[35,50,20,45,25,40,25,40]
marks_perc= []
for x in s_m:
    res=(x/50)*100
    marks_perc.append(res)

print(marks_perc)

def marks_line_chart():
    plt.plot(s_n,s_m)
    plt.title("Students Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.show()
marks_line_chart()

def per_bar_chart():
    plt.bar(s_n,marks_perc)
    plt.title("Students' Percentage Graph")
    plt.ylabel("Student Percentage")
    plt.xlabel("Student Names")
    plt.show()
per_bar_chart()