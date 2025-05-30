FROM public.ecr.aws/lambda/python:3.12

# Copy requirements (if any)
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy Lambda function code
COPY lambda_function.py ./

# Set the Lambda handler
CMD ["lambda_function.handler"]

