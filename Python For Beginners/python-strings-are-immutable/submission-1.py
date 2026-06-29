def remove_fourth_character(word: str) -> str:
    string_before = word[:3]
    string_after = word[4:]
    return string_before + string_after


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
