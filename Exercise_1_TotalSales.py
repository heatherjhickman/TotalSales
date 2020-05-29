"""
1)	We are going to sum each day’s sales into an accumulator/sum variable for display.
2)	Make sure the user enters a valid number.

3)	Step 1: Initialize input variables:
daysOfWeek[] – holds our 7 days
dailySales[] – holds our sales for each day of week
totalSales – accumulator to hold total sales

Step 2: Processing:
Loop through 7 days len(daysOfWeek)
  prompt the user to enter sales for day
  add sales to total (totalSales +=dailySales)

Step3: Output
Print the results
"""

# create a single dimension list for daily sales (variables)
dailySales = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
daysOfWeek = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
totalSales = 0.0 # accumulator to sum our totals

# loop seven days and grab sales for the day
for i in range(len(dailySales)): # this is the appropriate way to code
    dailySales[i] = float(input("Enter the sales for: " + daysOfWeek[i]+": "))
    # accumulate the total sales from the week and display the results
    totalSales += dailySales[i] # using [i] refers back to the indexed days of the week, goes through the sales for each day

print("The total sales for the week was:\t", totalSales)
# print("The average sales for the week was:\t", totalSales/len(dailySales)) IF THE AVERAGE WAS WANTED AS WELL