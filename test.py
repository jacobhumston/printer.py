import dev_printer as p


i = p.Input.select("please select an option", ["example option", "another example option", "ANOTHER example option"], "heyy", hide_instructions=True)
print(i)
