import os
from linkedin_api import Linkedin
import nest_asyncio
nest_asyncio.apply()

# Initialize LinkedIn API
api = Linkedin(os.getenv("LINKEDIN_EMAIL"), os.getenv("LINKEDIN_PASS"))

def get_job_type(job_type):
    mapping = {
        "full-time": "F", "contract": "C", "part-time": "P",
        "temporary": "T", "internship": "I", "volunteer": "V", "other": "O"
    }
    return mapping.get(job_type.lower())

def get_job_ids(keywords, location_name, job_type=None, limit=10, companies=None, industries=None, remote=None):
    job_type_code = get_job_type(job_type) if job_type else None
    job_postings = api.search_jobs(
        keywords=keywords,
        job_type=job_type_code,
        location_name=location_name,
        companies=companies,
        industries=industries,
        remote=remote,
        limit=limit
    )
    return [job['trackingUrn'].split('jobPosting:')[1] for job in job_postings]

async def get_job_details(job_id):
    try:
        job_data = api.get_job(job_id)
        return {
            "company_name": job_data.get('companyDetails', {})
                .get('com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany', {})
                .get('companyResolutionResult', {}).get('name', ''),
            "company_url": job_data.get('companyDetails', {})
                .get('com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany', {})
                .get('companyResolutionResult', {}).get('url', ''),
            "job_desc_text": job_data.get('description', {}).get('text', ''),
            "work_remote_allowed": job_data.get('workRemoteAllowed', ''),
            "job_title": job_data.get('title', ''),
            "company_apply_url": job_data.get('applyMethod', {})
                .get('com.linkedin.voyager.jobs.OffsiteApply', {}).get('companyApplyUrl', ''),
            "job_location": job_data.get('formattedLocation', '')
        }
    except Exception as e:
        print(f"[!] Error fetching job {job_id}: {e}")
        return {
            "company_name": '', "company_url": '', "job_desc_text": '',
            "work_remote_allowed": '', "job_title": '', "company_apply_url": '',
            "job_location": ''
        }

async def fetch_all_jobs(job_ids):
    return [await get_job_details(jid) for jid in job_ids]
