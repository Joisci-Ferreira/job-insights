from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    return list({
        job["job_type"] for job in read(path)
        if job["job_type"]
    })


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return [
        job for job in jobs
        if job["job_type"] == job_type
    ]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    return list({
        job["industry"] for job in read(path)
        if job["industry"]
    })


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [
        job for job in jobs
        if job["industry"] == industry
    ]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    return max([
        int(job["max_salary"]) for job in read(path)
        if job["max_salary"].isdecimal()
    ])


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """

    return min([
        int(job["min_salary"]) for job in read(path)
        if job["min_salary"].isdecimal()
    ])


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if ('min_salary' not in job or 'max_salary' not in job):
        raise ValueError('min salary or max salary does not exist')

    if (type(job['min_salary']) != int or type(job['max_salary']) != int):
        raise ValueError('min salary or max salary is not an integer')

    if (job['min_salary'] > job['max_salary']):
        raise ValueError('The min salary cannot be higher than max salary')

    if (type(salary) != int):
        raise ValueError('Salary is not integer')

    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    valid_jobs = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                valid_jobs.append(job)

        except ValueError:
            pass
    return valid_jobs
