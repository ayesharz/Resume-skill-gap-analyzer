def extract_skills(text, skills_list):
    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))
