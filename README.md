# job-search-engine-backend
Utilizing the JobSpy repository, this is a website where you can search multiple locations for jobs. This is just the backend, [another repository handles the backend](https://github.com/ebarr10/job-search-engine-frontend)

To run:
1. Create an virtual environment: `python3 -m venv env`
2. Activate the environment: `.\env\Scripts\Activate` in powershell (might need to adjust permissions in cmd if it doesn't work)
3. Install all packages `pip install -r requirements.txt`
4. cd into the backend folder
5. Run: `waitress-serve --port=8000 backend.wsgi:application`
6. You can now go to `127.0.0.1:8000/api/jobs` and the django restframework display should show up with some results

