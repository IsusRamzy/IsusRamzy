class Person():
  def __init__(self, name: str, knowledge: list[str], languages: list[str]):
    self.name = name
    self.knowledge = knowledge
    self.languages = languages

Isus = Person(name="Isus Ramzy Beshara",
  knowledge=["Unity & C# (Learning...)", "HTML & CSS", "CustomTkinter", "Ursina", "Flask", "MongoDB"],
  languages=["English (advanced)", "Arabic (Native)"]
)
print(f"Hello! I'm {Isus.name}")
print("For programming, I know:")
for item in Isus.knowledge:
  print(item)
print("When speaking, I know:")
for item in Isus.languages:
  print(item)