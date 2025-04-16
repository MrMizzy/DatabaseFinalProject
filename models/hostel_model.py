from db.connection import get_connection

def get_all_hostels():
    conn = get_connection()
    if not conn:
        return []

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, name, location, total_rooms FROM hostels")
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching hostels: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_rooms_by_hostel(hostel_id):
    conn = get_connection()
    if not conn:
        return []

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, room_number, is_available FROM rooms WHERE hostel_id = %s", (hostel_id,))
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching rooms: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
