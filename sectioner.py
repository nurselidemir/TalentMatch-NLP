from classifier import classify_cv_section

def segment_and_classify_sections(full_text):
    """
    CV metnini başlıklara göre parçalara ayırır ve her parçayı sınıflandırır.
    """
    lines = full_text.split("\n")
    current_block = ""
    labeled_sections = {}
    first_label_seen = False

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.endswith(":") or line.lower() in ["education", "experience", "skills"]:
            if current_block and first_label_seen:
                label = classify_cv_section(current_block)
                labeled_sections.setdefault(label, []).append(current_block.strip())
            current_block = line + "\n"
            first_label_seen = True
        else:
            current_block += line + "\n"

    if current_block and first_label_seen:
        label = classify_cv_section(current_block)
        labeled_sections.setdefault(label, []).append(current_block.strip())

    return labeled_sections
