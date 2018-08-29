from matplotlib import pyplot

ref_counts = [1938, 1131, 3900]

ref_names = ["Advertisements", "Word of Mouth", "Events"]

pyplot.pie(ref_counts, labels = ref_names, autopct="%.1f%%", 
shadow=True, explode=[0, 0, 0])
pyplot.title("Types of References")
pyplot.axis("equal")


pyplot.show()