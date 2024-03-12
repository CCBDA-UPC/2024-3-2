import json
from argparse import ArgumentParser
from pathlib import Path

import boto3

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="Faces summary",
        description="Search for images where a face appears and do a summary of their attributes",
    )
    parser.add_argument("face_image", help="An image with the face to search")
    parser.add_argument(
        "--similarity_threshold",
        default=80,
        type=float,
        help="Face image similarity threshold",
    )
    parser.add_argument("directory", help="The images directory to analyze")
    args = parser.parse_args()

    client = boto3.client("rekognition")

    input_image = open(args.face_image, "rb").read()
    images_dir = Path(args.directory)
    for image_file in images_dir.iterdir():
        print()

        with open(image_file, "rb") as directory_image:
            dir_image_bytes = directory_image.read()
            response_match = client.compare_faces(
                SimilarityThreshold=args.similarity_threshold,
                SourceImage={"Bytes": input_image},
                TargetImage={"Bytes": dir_image_bytes},
            )

            if response_match["FaceMatches"]:
                print(f"Face match in {image_file}")

                response = client.detect_faces(
                    Image={"Bytes": dir_image_bytes},
                    Attributes=[
                        "GENDER",
                        "EYEGLASSES",
                        "SUNGLASSES",
                        "AGE_RANGE",
                        "SMILE",
                    ],
                )

                print(f"Detected faces for {image_file}")
                for faceDetail in response["FaceDetails"]:
                    print(
                        "The detected face is between "
                        + str(faceDetail["AgeRange"]["Low"])
                        + " and "
                        + str(faceDetail["AgeRange"]["High"])
                        + " years old"
                    )
                    if faceDetail["Gender"]["Confidence"] > 60:
                        print(f"The detected gender is {faceDetail['Gender']['Value']}")
                    if (
                        faceDetail["Smile"]["Confidence"] > 60
                        and faceDetail["Smile"]["Value"]
                    ):
                        print("The person is smiling")
                    if (
                        faceDetail["Eyeglasses"]["Confidence"] > 60
                        and faceDetail["Eyeglasses"]["Value"]
                    ):
                        print("And its wearing eyeglasses")
            else:
                print(f"No match in {image_file}")
