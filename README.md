# Finance Professional Development Resource Project Report

## Related Links

[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1PG95JnUns66L2cMYGrrU4qmEThuvEntGLV3w98p1TFg/edit#0)

[![Colab Notebook](https://img.shields.io/badge/Google_Colab-Notebook-orange?style=flat&logo=googlecolab)](https://colab.research.google.com/drive/1B-cStyriTOmnb8g1QD8eqmmaQATxIoPo) for web scraping

[![Colab Notebook](https://img.shields.io/badge/Google_Colab-Notebook-orange?style=flat&logo=googlecolab)](https://colab.research.google.com/drive/1OoP_DLY4BKGO3i_16wjBfodK_msmrR9q) PDF Extractioni

[![Colab Notebook](https://img.shields.io/badge/Google_Colab-Notebook-orange?style=flat&logo=googlecolab)](https://colab.research.google.com/drive/1ypw7U38NmmvOOX6EyAw5e-cj0nC-BCmW) for SQLalchemy

[![Colab Notebook](https://img.shields.io/badge/Google_Colab-Notebook-orange?style=flat&logo=googlecolab)](https://colab.research.google.com/drive/1fATFkifeMqqv8-Ooq-iqDbgYAAmmx_Gi) S3 Cloud Storage

## Overview

This case study required us to create a robust data pipeline that would enable the extraction, transformation, and loading (ETL) of finance professional development materials into a structured database. The primary goal was to automate the collection and processing of data from various sources, including web pages and PDF files

## Project Goals

- **Web Scraping**: Obtaining information from the CFA Institute’s websites and storing it in structured datasets

- **Text Extraction**: Utilize PyPDF2 and Grobid for efficient extraction of text from PDF documents.
- **Database Management**: Store structured data in a Snowflake database for easy access and analysis.
- **Cloud Integration**: Ensure all data and extracted information are securely stored in AWS S3 buckets.

## Technologies Used

[![AWS](https://img.shields.io/badge/AWS-411120?style=for-the-badge)](https://aws.amazon.com/)
[![Snowflake](https://img.shields.io/badge/snowflake-0000FF?style=for-the-badge&logo=snowflake&logoColor=white)](https://docs.snowflake.com/ )

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)

- Web scrapping with Python (Beautiful Soup, Selenium)
- PDF Extraction with python (PyPDF2, Grobid)
- Snowflake with python (SQLAlchemy)
- AWS S3 with python (boto3)

## Data Sources

- CFA Institute’s website
- Provided PDF files of finance-related materials

## Project Structure

```
Assignment-02s
├── Diagrams
│   ├── CFA.png
│   ├── Data Architecture-02.ipynb
│   └── data_scraping_architecture.png
├── Notebooks
│   ├── Step1
│   │   ├── Webscraping.ipynb
│   │   └── content.csv
│   ├── Step2
│   │   ├── Grobid_RR_2024_l1_combined.txt
│   │   ├── Grobid_RR_2024_l1_combined_metadata.json
│   │   ├── Grobid_RR_2024_l1_combined_metadata.xml
│   │   ├── Grobid_RR_2024_l2_combined.txt
│   │   ├── Grobid_RR_2024_l2_combined_metadata.json
│   │   ├── Grobid_RR_2024_l2_combined_metadata.xml
│   │   ├── Grobid_RR_2024_l3_combined.txt
│   │   ├── Grobid_RR_2024_l3_combined_metadata.json
│   │   ├── Grobid_RR_2024_l3_combined_metadata.xml
│   │   ├── PDF_Parsing.py
│   │   ├── PyPDF_RR_2024-l1_combined.txt
│   │   ├── PyPDF_RR_2024-l2_combined.txt
│   │   ├── PyPDF_RR_2024-l3_combined.txt
│   │   └── metadata.csv
│   ├── Step3
│   │   ├── content.csv
│   │   └── csv_upload_sqlalchemy.ipynb
│   └── Step4
│       ├── Upload_to_S3.py
│       ├── metadata.csv
│       ├── metadata_new.csv
│       └── pdfmetadata_upload_sqlalchemy.ipynb
├── README.md
└── requirements.txt

```



## Prerequisites

- General recommendation Python 3.8+
- Access to AWS and Snowflake
- Virtual environment for the jupyter python files

## Running the Application

- Starting the python virtual environment
- Run 'pip install -r requirements.txt'
- Start jupyter notebook
- Ensure that the Jupyter kernel matches the virtual environment
- Add your own .env document for snowflake and AWS in each folder
- Run the files in folder *NoteBooks* and follow the steps.

## Learning Outcomes

1. **Proficiency in Web Scraping**: Learned how to use web scraping tools like Beautiful Soup and Selenium to extract information from web pages systematically. Gained experience in navigating and parsing HTML and CSS to retrieve required data and handle various web scraping challenges like dynamic content and pagination.
2. **Text Extraction from PDFs**: Mastered the use of tools such as PyPDF2 and Grobid for extracting text from PDF documents, understanding the intricacies of different PDF structures and how they can be programmatically accessed and processed.
3. **Snowflake Database Management**: Developed an understanding of SQL and database management systems, specifically using SQLAlchemy and Snowflake. 
4. **Cloud Storage Integration**: Gained practical experience with cloud services by uploading files to AWS S3 buckets and learned how to integrate cloud storage solutions with Python applications.

## References

- https://docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial
- https://github.com/ashrithagoramane/DAMG7245-Spring24/tree/main
- https://medium.com/@jonathanmondaut/scraping-multiple-pages-of-a-javascript-heavy-ecommerce-website-with-selenium-and-beautifulsoup-7c25ae391842
- https://www.geeksforgeeks.org/how-to-scrape-multiple-pages-using-selenium-in-python/
- https://www.codecademy.com/article/caupolicandiaz/web-scrape-with-selenium-and-beautiful-soup
- https://docs.snowflake.com/en/developer-guide/python-connector/sqlalchemy
- https://docs.snowflake.com/en/user-guide/data-unload-s3

## Team

| Name         | Contribution% | Contributions           |
| ------------ | ------------- | ----------------------- |
| Dongyu Liu   | 20%           | Web Scrapping           |
| Ekta Bhatia  | 25%           | PDF Extraction          |
| Parth Kalani | 30%           | Snowflke Data uploading |
| Sumit Sharma | 25%           | S3 Cloud Storage        |

