import matplotlib.pyplot as plt

age_groups = ['0-20', '21-40', '41-60', '60+']
population = [512, 807, 98, 85]

plt.bar(age_groups, population)
plt.xlabel('Age Groups')
plt.ylabel('Population (in millions)')
plt.title('Population Distribution by Age Group')

plt.savefig('chart.png')
plt.show()