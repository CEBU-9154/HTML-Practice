import matplotlib.pyplot as plt
math_marks=[45,50,55,60,65,70,72,75,80,82,85,88,90]
sci_marks=[40,48,52,58,63,68,71,74,78,81,84,87,92]

type=[math_marks, sci_marks]
colors=['blue','orange']
label=['Math','Science']
bins=[40,60,75,100]

plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.hist(type,bins=bins,width=0.9,color=colors,label=label,orientation='horizontal')
plt.title("Student Mrks Distribution")
plt.legend()
plt.show()