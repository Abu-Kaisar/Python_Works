import matplotlib.pyplot as plt

year = [1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020]
pop = [1.28, 2.36, 3.25, 3.89, 3.99, 4.02, 4.44, 4.91, 5.21, 5.88, 6.02, 6.88, 7.2]
hover = [0,0,1,5,9,7,6,3,2,1,5,4,8,9,6,1,4,7,8,6,9,3,5,4,1,3,6,9,8,10]


#pyplot --- LINE PLOT ---

plt.plot(year, pop, c="pink", linewidth=4, linestyle='dashed')
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Imaginary Population by Years")
plt.yticks([0,2,4,6,8,10], ["0B","2B","4B","6B","8B","10B"])
plt.show()




