from typing import Optional

from dbs.generic_db import GenericDB
import psycopg2

from models.resource_model import ResourceModel
from models.scan_model import ScanModel


class PostgresDB(GenericDB):
    def insert_scan(self, scan: ScanModel):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO scan (start) VALUES ('{scan.start}')")

    def insert_resource(self, resource: ResourceModel):
        print('here')
        cur = self.conn.cursor()
        print(resource)
        kvs = {
            'urn': resource.urn,
            'scan_id': resource.scan_id,
            'name': resource.name,
            'type': resource.type,
            'data': resource.data
        }
        keys = ', '.join(kvs.keys())
        print(keys)
        tmp = [f"'{v}'" if k is not 'scan_id' else f"{v}" for (k, v) in kvs.items()]
        print(tmp)
        values = ', '.join(tmp)
        print(values)
        try:
            cur.execute(f"INSERT INTO resource ({keys}) VALUES ({values})")
        except e:
            raise e

    def get_all_scans(self):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM scan")
        return cur.fetchall()

    def get_all_resources(self, type: Optional[str] = None, scan_id: Optional[int] = None):
        cur = self.conn.cursor()
        condition = ''
        if type is not None:
            condition += f"type='{type}'"
        if scan_id is not None:
            if condition != '':
                condition += " AND "
            condition += f"scan_id={scan_id}"
        if condition != '':
            condition = " WHERE " + condition
        try:
            cur.execute(f"SELECT * FROM resource {condition} ")
        except:
            return []
        return cur.fetchall()

    def get_resource_types(self):
        cur = self.conn.cursor()
        cur.execute("SELECT unnest(enum_range(NULL::resource_types))")
        return [x[0] for x in cur.fetchall()]

    def connect(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123123"
        )
        self.conn.autocommit = True
