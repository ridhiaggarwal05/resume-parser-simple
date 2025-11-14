import re

def extract_email(text):
    pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
    match = re.search(pattern, text)
    return match.group(0) if match else "Not found"


def extract_phone(text):
    pattern = r"(\+?\d[\d\s\-\(\)]{8,}\d)"
    match = re.search(pattern, text)
    return match.group(0) if match else "Not found"


def extract_skills(text, skill_list):
    text_lower = text.lower()
    found = []

    for skill in skill_list:
        if skill.lower() in text_lower:
            found.append(skill)

    return list(set(found))
