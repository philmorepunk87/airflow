#!/usr/bin/env bash

airflow connections --add --conn_id test_postgres --conn_type postgres --conn_host localhost --conn_login postgres --conn_password postgres --conn_port 5432