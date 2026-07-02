class ATSMatcher:
    """
    Compares resume skills with job description skills
    and calculates the ATS score.
    """

    @staticmethod
    def match(resume_skills: dict, job_skills: dict):

        resume_set = set()
        job_set = set()

        for skills in resume_skills.values():
            resume_set.update(skill.lower() for skill in skills)

        for skills in job_skills.values():
            job_set.update(skill.lower() for skill in skills)

        matched = sorted(resume_set.intersection(job_set))
        missing = sorted(job_set.difference(resume_set))

        if not job_set:
            ats_score = 0
        else:
            ats_score = round((len(matched) / len(job_set)) * 100)

        return {
            "ats_score": ats_score,
            "matched_skills": matched,
            "missing_skills": missing
        }