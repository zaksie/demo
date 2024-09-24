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

    def get_all_scans(self, page_index: int = 0, page_size: int= 10):
        cur = self.conn.cursor()
        q = f"WITH r AS (SELECT * FROM scan LIMIT {page_size} OFFSET {page_size * page_index}) SELECT json_agg(r) FROM r "
        print(q)
        cur.execute(q)
        return cur.fetchone()[0]

    def get_all_resources(self, type: Optional[str] = None, scan_id: Optional[int] = None, page_index: int = 0, page_size: int= 10):
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
        cur.execute(f"WITH r AS (SELECT * FROM resource {condition} LIMIT {page_size} OFFSET {page_size * page_index}) SELECT json_agg(r) FROM r ")
        return cur.fetchone()[0]

    def get_resource_types(self):
        cur = self.conn.cursor()
        cur.execute("SELECT unnest(enum_range(NULL::resource_types))")
        return [x[0] for x in cur.fetchall()]

    def init(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123123"
        )
        self.conn.autocommit = True
