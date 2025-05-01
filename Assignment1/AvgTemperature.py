temperatures=[]

for i in range(5):
    temp= float(input(f"Enter temperature of Day{i+1}:"))
    temperatures.append(temp)

average=sum(temperatures)/len(temperatures)
print(f"Average temperature:{average:.2f}\u00B0 C")
