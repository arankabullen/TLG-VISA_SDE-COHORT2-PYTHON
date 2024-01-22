challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

a= challenge[2][1]
b= challenge[2][0]
c= challenge[3]

print(f"My {a}! The {b} do {c}!")


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

a= trial[2]["goggles"]
b= trial[2]["eyes"]
c= trial[-1]

print(f"My {a}! The {b} do {c}!")

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

a= nightmare[0]["user"]["name"]["first"]
b= nightmare[0]["kumquat"]
c= nightmare[0]["d"]

print(f"My {a}! The {b} do {c}!")
