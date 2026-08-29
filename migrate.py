from sqlite3 import connect

with connect("lux.sqlite") as conn:
    conn.execute("CREATE INDEX IF NOT EXISTS idx_prod_obj ON productions(obj_id);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_prod_agt ON productions(agt_id);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_oc_obj  ON objects_classifiers(obj_id);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_oc_cls  ON objects_classifiers(cls_id);")
    conn.commit()
print("Indexes created.")