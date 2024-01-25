import printer as p

e = ["first option", "second option", "another option", "fourth option!"]
i = p.Input.select("please select an option", e, "heyy", hide_instructions=False)
print(i)

