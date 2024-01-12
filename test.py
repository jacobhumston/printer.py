import printer as p

e = ["example option", "another example option", "ANOTHER example option", "meow", "lol", "haha", "ok", "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH", "LOL"]
i = p.Input.select("please select an option", e, "heyy", hide_instructions=True)
print(i)
