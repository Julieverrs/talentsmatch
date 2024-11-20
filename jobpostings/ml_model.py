import pandas as pd

def recommend_applicants(job_data):

    df = pd.read_csv('datasetss.csv')

    print(df.columns)

    required_skills = job_data.get('required_skills', '')

    if 'Skills' in df.columns:
        # Filter applicants based on matching required skills
        recommended = df[df['Skills'].str.contains(required_skills, na=False, case=False)]

        # Return the recommended applicants (customize this part as needed)
        return recommended[['Name', 'Skills', 'Experience', 'Job_Title']].to_dict(orient='records')
    else:
        raise KeyError("'Skills' column is missing from the dataset.")
