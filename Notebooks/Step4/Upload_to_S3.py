import boto3

s3_resource = boto3.resource('s3')

BUCKET_NAME = "dsd-tes-fpdr"
bucket_obj = s3_resource.Bucket(name=BUCKET_NAME)

print(f"Uploading Grobid text files to bucket {BUCKET_NAME}")

file_names = ["Grobid_RR_2024_l1_combined.txt", "Grobid_RR_2024_l2_combined.txt", "Grobid_RR_2024_l3_combined.txt","PyPDF_RR_2024_l1_combined.txt","PyPDF_RR_2024_l2_combined.txt","PyPDF_RR_2024_l3_combined.txt","content.csv"]

for file_name in file_names:
    bucket_obj.upload_file(Filename=file_name, Key=file_name)