"""Contains the function used to query based on label, date, agent, and classification"""
from sys import stderr, exit as exit_function
from contextlib import closing
from sqlite3 import connect

def get_info(date_arg, agt_arg, cls_arg, label_arg):
    """Queries and gives back the queried database according to the arguments date,agt,cls,label"""
    params = []
    db_url = "file:lux.sqlite?mode=ro"
    try:
        with connect(db_url, isolation_level=None,
                uri=True) as connection:

            with closing(connection.cursor()) as cursor:

                stmt_str = """
            SELECT oid, olabel, odate, GROUP_CONCAT(DISTINCT par) AS group_par, LOWER(GROUP_CONCAT(DISTINCT clam)) AS clams 
            FROM 
            (SELECT oid, olabel, odate, agentname, clame || '),' AS clam, agentname || ' (' || party || ')' || '),' AS par 
            FROM 
              (SELECT objects.id AS oid, objects.label AS olabel, objects.date AS odate, agents.name AS agentname, classifiers.name AS clame, productions.part AS party 
              FROM objects 
              LEFT JOIN productions ON objects.id = productions.obj_id 
              LEFT JOIN agents ON agents.id = productions.agt_id 
              LEFT JOIN objects_classifiers ON objects.id = objects_classifiers.obj_id 
              LEFT JOIN classifiers ON objects_classifiers.cls_id = classifiers.id 
              ) 
              ORDER BY agentname ASC, party ASC, LOWER(clam) ASC 
              ) 
              GROUP BY oid HAVING 1 = 1 
              """
                addand = "AND "
                if agt_arg:
                    stmt_str += addand + "agentname LIKE '%' || ? || '%' "
                    params.append('%' + agt_arg + '%')
                if date_arg:
                    stmt_str += addand + "odate LIKE '%' || ? || '%' "
                    params.append('%' + date_arg + '%')
                if cls_arg:
                    stmt_str += addand + "clams LIKE '%' || ? || '%' "
                    params.append('%' + cls_arg + '%')
                if label_arg:
                    stmt_str += addand + "olabel LIKE '%' || ? || '%' "
                    params.append('%' + label_arg + '%')
                stmt_str += " ORDER BY olabel ASC, odate ASC "
                stmt_str += " LIMIT 1000; "

                cursor.execute(stmt_str, params)
                rows = cursor.fetchall()

                return rows

    except Exception as ex:
        print(ex, file=stderr)
        return []

def search_labels(label_arg, limit=25):
    """Fast label-only search for the live as-you-type dropdown."""
    db_url = "file:lux.sqlite?mode=ro"
    try:
        with connect(db_url, uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    "SELECT id, label, date FROM objects "
                    "WHERE label LIKE '%' || ? || '%' "
                    "ORDER BY label LIMIT ?;",
                    (label_arg, limit))
                return cursor.fetchall()
    except Exception as ex:
        print(ex, file=stderr)
        return []

# def _test():
#     table = get_info('', 'gogh', '', '')
#     print(table)
#     print("")
#     print(table[0])
#     print("")
#     print(table[0])
#     print("")
#     print(table[0])

# if __name__ == '__main__':
#     _test()
