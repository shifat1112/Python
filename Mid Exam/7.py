name = ["India", "Thailand", "Bhutan", "China", "Nepal", "Myanmar"]

print(name)
d = []
for country in name:
    if country == "Bhutan":
        continue
    #print(country)
    d.append(country)
print(d)