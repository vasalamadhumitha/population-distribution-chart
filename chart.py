import matplotlib.pyplot as plt

# Sample population data
age_groups = ['0-14', '15-24', '25-54', '55-64', '65+']
population = [30, 20, 25, 15, 10]

# Create bar chart
plt.bar(age_groups, population)
plt.xlabel('Age Groups')
plt.ylabel('Population (%)')
plt.title('Population Distribution Chart')

# Save and show chart
plt.savefig('chart.png')
plt.show()
