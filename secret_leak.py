import os

def connect() -> None:
    """
    Connect using the AWS secret key retrieved from environment variables.

    Raises:
        EnvironmentError: If the AWS_SECRET_KEY environment variable is not set.
    """
    aws_secret_key = os.getenv("AWS_SECRET_KEY")
    if not aws_secret_key:
        raise EnvironmentError("AWS_SECRET_KEY environment variable is not set.")

    print("Connecting with AWS credentials.")


if __name__ == "__main__":
    connect()