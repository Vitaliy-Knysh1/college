dict = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
    "k": "9",
    "l": "10",
}

dict["b"] = "11"
dict["g"] = "12"
del dict["c"]
dict["d"] = None

print(dict)