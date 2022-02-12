import matplotlib.pyplot as plt

year = [1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020]
pop = [1.28, 2.36, 3.25, 3.89, 3.99, 4.02, 4.44, 4.91, 5.21, 5.88, 6.02, 6.88, 7.2]
hover = [0,0,1,5,9,7,6,3,2,1,5,4,8,9,6,1,4,7,8,6,9,3,5,4,1,3,6,9,8,10]


#pyplot --- SCATTER PLOT ---

plot1 = plt.figure(1)
plt.hist(hover, bins=6, color="green")
plt.xlabel("Random Number")
plt.ylabel("Distribution")
plt.title("Histogram Perks - 6")

plot2 = plt.figure(2)
plt.hist(hover, bins=12, color="red")
plt.xlabel("Random Number")
plt.ylabel("Distribution")
plt.title("Histogram Perks - 12")
plt.show()
