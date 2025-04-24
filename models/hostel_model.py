from db.connection import get_connection

def get_hostel_details_by_name(hostel_name):
    conn = get_connection()
    if not conn:
        return {}

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT h.Hostel_ID, h.Hostel_Name, h.Location, m.Manager_Name, m.`PhoneNo.`
            FROM Hostels h
            JOIN Managers m ON h.Manager_ID = m.Manager_ID
            WHERE h.Hostel_Name = %s
        """, (hostel_name,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error fetching hostel details: {e}")
        return {}
    finally:
        cursor.close()
        conn.close()

def get_room_types_by_hostel_name(hostel_name):
    conn = get_connection()
    if not conn:
        return []

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT rt.Room_Description, rt.Price, rt.Total_Rooms, rt.Booked_Rooms,
                   (rt.Total_Rooms - rt.Booked_Rooms) AS Available_Rooms
            FROM RoomTypes rt
            JOIN Hostels h ON rt.Hostel_ID = h.Hostel_ID
            WHERE h.Hostel_Name = %s
        """, (hostel_name,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching room types: {e}")
        return []
    finally:
        cursor.close()
        conn.close()