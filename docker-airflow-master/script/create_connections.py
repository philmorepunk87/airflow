from __future__ import print_function

import os
import sys

from airflow import settings
from airflow.models import Connection
from sqlalchemy.orm import exc


class InitializeConnections(object):

    def __init__(self):
        self.session = settings.Session()

    def has_connection(self, conn_id):
        try:
            (
                self.session.query(Connection)
                .filter(Connection.conn_id == conn_id)
                .one()
            )
        except exc.NoResultFound:
            return False
        return True

    def delete_all_connections(self):
        self.session.query(Connection.conn_id).delete()
        self.session.commit()

    def add_connection(self, **args):
        """
        conn_id, conn_type, extra, host, login,
        password, port, schema, uri
        """
        self.session.add(Connection(**args))
        self.session.commit()


if __name__ == "__main__":

    ic = InitializeConnections()
    ic.add_connection(conn_id="test-s3", 
                      conn_type="postgres",
                      host = "localhost",
                      password = "postgres",
                      login = "postgres",
                      port = "5432")