def match_jobs(found_skills, jobs):
    results = []

    for job in jobs:
        req = job["skills_required"]
        common = set(found_skills).intersection(set(req))
        score = len(common)

        results.append({
            "job_title": job["title"],
            "skills_matched": list(common),
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
