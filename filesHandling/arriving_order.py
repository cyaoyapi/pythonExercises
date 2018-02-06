#-*- coding:utf-8 -*-

team_members = ["Célestin N'Chot","Lénau Sévérin", "Larissa N'Guessan","Cyrille YAO","Elvis Amani",
"Anago Gildas","Dominique YAO","Serge ModèleCI"]

# Save the list in a file

file_obj1 = open(r"members1", "w", encoding="utf-8")

for order, member in enumerate(team_members):
	file_obj1.write(f"{order + 1} {member}\n")

file_obj1.close()

# Read the content of the fisrt file and copie into the second file with juste
# a few form changing

file_obj1 = open(r"members1", "r", encoding="utf-8")
file_obj2 = open(r"members2", "w", encoding="utf-8")

for line in file_obj1:
	line = line.split()
	file_obj2.write(f"{line[0]}, {line[1]} {line[2]}\n")

file_obj1.close()
file_obj2.close()
