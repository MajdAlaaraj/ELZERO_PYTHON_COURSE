#(1) prog to calculate your full age
# _____________________________________________
age=int(input("What\'s Your Age ?").strip())
months=age*12
weeks=months*4
days=age*365
hours=days*24
minutes=hours*60
seconds=minutes*60
print("you lived for :")
print(f"{months} months\n{weeks:,} weeks\n{days:,} days\n{hours:,} hours\n{minutes:,} minutes\n{seconds:,} seconds.")

#________________________________________________