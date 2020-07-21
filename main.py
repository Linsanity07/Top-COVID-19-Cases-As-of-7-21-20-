import matplotlib.pyplot as plt


states=['California','Florida','New Jersey','New York','Texas']
num=[400000,360000,179000,412000,346000]

plt.title('Top 5 States With Most Positive Cases')

plt.xlabel('States')
plt.ylabel('Number of COVID-19 Cases')
plt.bar(states,num,color='red',label='Color of graph')
plt.legend(facecolor='mediumpurple')


#plt.barh(Classes,student,color='green')

#plt.plot(Classes,student)

plt.show()