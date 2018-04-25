FROM lambci/lambda:python3.6

USER root
RUN mkdir -p /home/sbx_user1051 && chown sbx_user1051: /home/sbx_user1051
#RUN pip install --upgrade pip
RUN pip install pipenv
USER sbx_user1051
ENV PIPENV_VENV_IN_PROJECT=1
ENV SHELL=/bin/bash
ENTRYPOINT []