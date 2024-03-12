import boto3

image_file = "shelter.jpg"

client = boto3.client("rekognition")

with open(image_file, "rb") as img_io:
    response = client.detect_labels(Image={"Bytes": img_io.read()})

print(response)
