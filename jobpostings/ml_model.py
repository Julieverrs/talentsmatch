import pandas as pd

def recommend_applicants(job_data):
    # Load the updated dataset
    df = pd.read_csv('datasetss.csv')

    # Print columns to check for any issues (debugging step)
    print(df.columns)

    # Example: Matching applicants based on job required skills
    required_skills = job_data.get('required_skills', '')
    
    # Ensure the 'Skills' column exists (case-sensitive)
    if 'Skills' in df.columns:
        # Filter applicants based on matching required skills
        recommended = df[df['Skills'].str.contains(required_skills, na=False, case=False)]

        # Return the recommended applicants (customize this part as needed)
        return recommended[['Name', 'Skills', 'Experience', 'Job_Title']].to_dict(orient='records')
    else:
        raise KeyError("'Skills' column is missing from the dataset.")
