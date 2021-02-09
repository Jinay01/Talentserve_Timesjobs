import mysql.connector


def database_storage(company, time_period, salary, location, description, job_details, skills_required, company_details_dict, url):

    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    # print(mydb)

    # dictionary
    job_function = job_details.get('Job Function:', None)
    industry = job_details.get('Industry:', None)
    specialization = job_details.get('Specialization:', None)
    qualification = job_details.get('Qualification:', None)
    employment_type = job_details.get('Employment Type:', None)
    website = company_details_dict.get('Website', None)
    mycursor = mydb.cursor()
    sql = "INSERT INTO job (company_name, time_period, salary, location, job_description, job_function, industry, specialization, qualification, employement_type, skills, website, home_page) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (company, time_period, salary, location, description, job_function, industry,
           specialization, qualification, employment_type, skills_required, website, url)
    mycursor.execute(sql, val)
    # mycursor.execute("""INSERT INTO job (company_name, time_period, salary, location, job_description,job_function, industry, specialization, qualification, employement_type, skills, website, home_page) VALUES ("%s", "%s","%s", "%s","%s", "%s","%s", "%s","%s", "%s","%s", "%s","%s")""", (company, time_period, salary, location, description, job_function, industry,
    #                                                                                                                                                                                                                                                                                             specialization, qualification, employment_type, skills_required, website, url))
    mydb.commit()
    # print(mycursor)
