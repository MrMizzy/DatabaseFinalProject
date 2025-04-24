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

def get_hostel_manager(hostel_id):
    connection= get_connection()
    if not connection:
        return []
    
    cursor=connection.cursor()

    try:
        cursor.execute(f"SELECT m.Manager_ID, m.Manager_Name, m.`PhoneNo.` FROM Hostels h JOIN Managers m ON h.Manager_ID = m.Manager_ID WHERE h.Hostel_ID = '{hostel_id}';")
        results= cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching rooms: {e}")
        return []

def get_hostel_location(hostel_id):
    connection= get_connection()
    if not connection:
        return []
    
    cursor=connection.cursor()

    try:
        cursor.execute(f"SELECT Location FROM Hostels where Hostel_ID = '{hostel_id}';")
        results= cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching location: {e}")
        return []
    
def get_hostel_rooms(hostel_id):
    connection= get_connection()
    if not connection:
        return []
    
    cursor=connection.cursor()

    try:
        cursor.execute(f"SELECT rm.Room_ID, rt.Room_Description, rt.Price, rm.Available_Beds FROM Rooms rm JOIN RoomTypes rt ON rm.Room_Type=rt.TypeID WHERE rt.Hostel_ID = '{hostel_id}';")
        results= cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching rooms: {e}")
        return []
    
def get_rooms_within_price_range(min_price, max_price):
    connection= get_connection()
    if not connection:
        return []
    
    cursor=connection.cursor()

    try:
        cursor.execute(f"SELECT rm.Room_ID, rt.Room_Description, rt.Price, rm.Available_Beds FROM Rooms rm JOIN RoomTypes rt ON rm.Room_Type=rt.TypeID  WHERE Price BETWEEN {min_price} AND {max_price} ORDER BY rt.Hostel_ID, rt.Price;")
        results= cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching rooms: {e}")
        return []

def get_rooms_by_room_size(room_size):
    connection= get_connection()
    if not connection:
        return []
    
    cursor=connection.cursor()

    try:
        cursor.execute(f"SELECT rm.Room_ID, rt.Room_Description, rt.Price, rm.Available_Beds FROM Rooms rm JOIN RoomTypes rt ON rm.Room_Type=rt.TypeID WHERE rt.Room_Description Like '%{room_size} in a Room%' ORDER BY rt.Price,rt.Hostel_ID;")
        results= cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching rooms: {e}")
        return []