football = {"Ram", "Shyam", "Om"}
cricket = {"Ram", "Om", "Akash"}

both_sports = football & cricket
only_football = football - cricket
only_cricket = cricket - football
all_students = {"Ram", "Shyam", "Om", "Akash", "Binod"}
none_sports = all_students - (football | cricket)

print("Both sports:", both_sports)
print("Only football:", only_football)
print("Only cricket:", only_cricket)
print("None:", none_sports)