data = {
 "studenter": [
 ("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
 ("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
 ("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
 ("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
 ("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv":
 True}),
 ],
 "kurser": {
 "Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
 "Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
 "Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
 }

 }
