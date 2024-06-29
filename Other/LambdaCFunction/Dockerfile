FROM public.ecr.aws/lambda/python:3.12

RUN dnf install -y gcc

COPY lambda_function.py ${LAMBDA_TASK_ROOT}
COPY example.so ${LAMBDA_TASK_ROOT}

CMD [ "lambda_function.handler" ]