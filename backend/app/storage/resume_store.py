class ResumeStore:
    """
    Temporary in-memory storage.
    """

    resumes = {}

    @classmethod
    def save(cls, resume_id, data):
        cls.resumes[resume_id] = data

    @classmethod
    def get(cls, resume_id):
        return cls.resumes.get(resume_id)

    @classmethod
    def exists(cls, resume_id):
        return resume_id in cls.resumes

    @classmethod
    def clear(cls):
        cls.resumes.clear()