import printer as p

color = p.add_custom_rgb_color(100, 117, 255)

e = ["first option", "second option", "another option", "fourth option!"]
i = p.Input.select("please select an option", e, "heyy", hide_instructions=False, color=color)
print(i)

