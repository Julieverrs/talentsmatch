import pandas as pd

def recommend_applicants(job_data):
    # Updated file name
    df = pd.read_csv('Datasets.csv')

    # Clean the 'Experience' column: remove non-numeric characters (if any) and convert to integer
    df['Experience'] = df['Experience'].replace(r'[^\d]', '', regex=True).astype(int)

    # Filter out rows where Experience is NaN (if any)
    df = df.dropna(subset=['Experience'])

    required_skills = job_data.get('required_skills', '')  # Comma-separated string
    skill_list = [skill.strip().lower() for skill in required_skills.split(',')]  # Split and clean skills

    print("Required Skills:", skill_list)  # Debug print to show what skills were passed in

    if 'Skills' in df.columns:
        df['Skills'] = df['Skills'].str.lower()  # Ensure all skills in the dataset are lowercase for comparison

        # Filter applicants based on required skills
        recommended = df[df['Skills'].apply(lambda skills: any(skill in skills for skill in skill_list))]

        # Optional: filter by Experience level if provided
        if 'experience_level' in job_data:
            experience_level = job_data['experience_level']
            recommended = recommended[recommended['Experience'] >= experience_level]

        # Display the filtered applicants
        print("Filtered Applicants:", recommended)  # Debug print to show applicants after filtering

        # Ensure that Experience is displayed as an integer without the .0
        recommended['Experience'] = recommended['Experience'].astype(int)

        return recommended[['Name', 'Skills', 'Experience', 'Job_Title']].to_dict(orient='records')
    else:
        raise KeyError("'Skills' column is missing from the dataset.")
