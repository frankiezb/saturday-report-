from app.database import get_db

def results_formatter(results):
    out = []
    for result in results:  # Changed variable name from 'results' to 'result' to avoid confusion
        res = {
            "id": result[0],
            "name": result[1],
            "summary": result[2],
            "description": result[3],
            "is_done": result[4]
        }
        out.append(res)
    return out  # Moved return statement outside of the loop

def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task", ())
    results = cursor.fetchall()
    cursor.close()
    return results_formatter(results)

def select_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id = ?", (task_id,))
    result = cursor.fetchone()  # Using fetchone() to get a single result
    cursor.close()
    if result:  # Checking if result exists
        return results_formatter([result])[0]  # Passing a list with a single result to formatter
    return {}  # Returning an empty dictionary if no result found

def insert(task_data):
    data_tuple = (
        task_data.get("name"),
        task_data.get("summary"),
        task_data.get("description")
    )
    statement = """
        INSERT INTO task (
            name,
            summary,
            description 
        ) VALUES (?, ?, ?)
    """
    conn = get_db()
    conn.execute(statement, data_tuple)
    conn.commit()

def delete(task_id):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id = ?", (task_id,))
    conn.commit()
