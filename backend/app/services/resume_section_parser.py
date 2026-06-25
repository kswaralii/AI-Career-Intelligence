class ResumeSectionParser:

    SECTION_HEADERS = [
        "education",
        "experience",
        "projects",
        "skills",
        "certifications",
        "internships",
        "achievements",
        "summary",
    ]

    @staticmethod
    def split_sections(text: str):

        sections = {}

        current_section = "other"

        sections[current_section] = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            if lower in ResumeSectionParser.SECTION_HEADERS:
                current_section = lower
                sections[current_section] = []
                continue

            sections[current_section].append(line)

        return sections