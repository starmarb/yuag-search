"""Queries the database to output to the site"""
from sys import stderr, exit as exit_function
from contextlib import closing
from sqlite3 import connect

def get_object_info(object_id):
    """Acquires the info through the object id, and then fetching their respective information"""

    db_url = "file:lux.sqlite?mode=ro"

    try:
        with connect(db_url, isolation_level=None, uri=True) as connection:
            with closing(connection.cursor()) as cursor:

                summary = fetch_summary(object_id, cursor)
                label = fetch_label(object_id, cursor)
                produced_by = fetch_produced_by(object_id, cursor)
                classified_as = fetch_classified_as(object_id, cursor)
                information = fetch_information(object_id, cursor)

                return summary, label, produced_by, classified_as, information

    except Exception as ex:
        print(ex, file=stderr)
        exit_function(1)

def fetch_summary(object_id, cursor):
    """Gathers the summary  through a summary query, below"""
    # Define SQL queries to retrieve 'Summary' details
    summary_query = """SELECT objects.accession_no, objects.date, GROUP_CONCAT(places.label, ', ')
                        AS places, departments.name
                        FROM objects
                        LEFT JOIN objects_departments ON objects_departments.obj_id = objects.id
                        LEFT JOIN departments ON objects_departments.dep_id = departments.id
                        LEFT JOIN objects_places ON objects.id = objects_places.obj_id
                        LEFT JOIN places ON objects_places.pl_id = places.id
                        WHERE objects.id = ?
                        GROUP BY objects.accession_no, objects.date, departments.name"""
    # Execute fetch
    cursor.execute(summary_query, (object_id,))
    summary_details = cursor.fetchall()

    return summary_details

def fetch_label(object_id, cursor):
    """Gathers the label queries using the query command below"""
    # Define SQL queries to retrieve 'Label' details
    label_query = """SELECT objects.label FROM objects WHERE objects.id = ?"""
    # Execute fetch
    cursor.execute(label_query, (object_id,))
    label_details = cursor.fetchall()

    return label_details

def fetch_produced_by(object_id, cursor):
    """Gathers the produced by queries with the queries below"""
    # Define SQL queries to retrieve 'Produced By' details
    produced_by_query = """SELECT productions.part, agents.name, agents.begin_date, agents.end_date,
                            GROUP_CONCAT(nationalities.descriptor, ', ') AS nationalities 
                                FROM objects
                                LEFT JOIN productions ON objects.id = productions.obj_id
                                LEFT JOIN agents ON productions.agt_id = agents.id
                                LEFT JOIN agents_nationalities ON agents.id = agents_nationalities.agt_id
                                LEFT JOIN nationalities ON agents_nationalities.nat_id = nationalities.id
                                WHERE objects.id = ?
                                GROUP BY productions.part, agents.name, agents.begin_date, agents.end_date
                                ORDER BY agents.name COLLATE NOCASE ASC, productions.part COLLATE NOCASE ASC, 
                                    nationalities.descriptor COLLATE NOCASE ASC"""
    # Execute fetch
    cursor.execute(produced_by_query, (object_id,))
    produced_by_details = cursor.fetchall()

    return produced_by_details

def fetch_classified_as(object_id, cursor):
    """Gathers the Classification queries using the query command below"""
    # Define SQL queries to retrieve 'Classified As' details
    classified_as_query = """SELECT classifiers.name
                                FROM objects 
                                LEFT JOIN objects_classifiers ON objects.id = objects_classifiers.obj_id 
                                LEFT JOIN classifiers ON classifiers.id = objects_classifiers.cls_id 
                                WHERE objects.id = ? 
                                ORDER BY classifiers.name COLLATE NOCASE ASC"""
    # Execute fetch
    cursor.execute(classified_as_query, (object_id,))
    classified_as_details = cursor.fetchall()

    return classified_as_details

def fetch_information(object_id, cursor):
    """Gathers the Information details using the query command below"""
    # Define SQL queries to retrieve 'Information' details
    information_query = """SELECT \"references\".\"type\", \"references\".\"content\"
                            FROM objects 
                            LEFT JOIN \"references\" ON objects.id = \"references\".obj_id 
                            WHERE objects.id = ?"""
    # Execute fetch
    cursor.execute(information_query, (object_id,))
    information_details = cursor.fetchall()

    return information_details

def _test(id_test):
    summary, label, produced_by, classified_as, information = get_object_info(id_test)
    print(summary[0][0])
    print("")
    print(label)
    print("")
    print(produced_by)
    print("")
    print(classified_as)
    print("")
    print(information)


if __name__ == '__main__':
    _test(1)
