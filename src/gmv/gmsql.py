
import sqlite3
import pprint;

class GMSQL:

    conn = None
    pp = pprint.PrettyPrinter(indent=4)

    @classmethod
    def connect(cls, file):
        if not cls.conn:
            cls.conn = sqlite3.connect(file)
        
    @classmethod
    def init(cls):
       c = cls.conn.cursor()
       # TODO
       # create table emails(gmid text primary key, threadid text, gmfrom text, gmto text,subject text, date text,labels text)without rowid;
       cls.conn.commit()
    
    @classmethod    
    def store_email(cls, id, threadid, h_from, h_to, subject, date, labels):
        cls.delete_email(id)
        c = cls.conn.cursor()
        args = (
                id,
                threadid,
                h_from if h_from is not None else '', 
                h_to if h_to is not None else '', 
                subject, 
                date.isoformat(' '), 
                ",".join(labels)
        )
        # cls.pp.pprint(args)
        c.execute('insert into emails (gmid,threadid,gmfrom,gmto,subject,date,labels) values (?,?,?,?,?,?,?)', args)
        cls.conn.commit()
        
    @classmethod
    def delete_email(cls, id):
        c = cls.conn.cursor()
        args = (id,)
        # cls.pp.pprint(args)
        c.execute('delete from emails where gmid = ?', args)
        cls.conn.commit()

    @classmethod
    def close(cls):
        if cls.conn:
            cls.conn.close()
            cls.conn = None
