from db.connection import get_connection

def get_room_instances_by_type(room_description):
    connection = get_connection()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT rm.Room_ID, rm.Available_Beds
            FROM Rooms rm
            JOIN RoomTypes rt ON rm.Room_Type = rt.TypeID
            WHERE rt.Room_Description = %s
        """, (room_description,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching room instances: {e}")
        return []
    finally:
        cursor.close()
        connection.close()

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
            SELECT rt.Room_Description, rt.Price, rt.Total_Rooms
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
    
    cursor=connection.cursor(dictionary=True)

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
    
    cursor=connection.cursor(dictionary=True)

    try:
        pattern = f"%{room_size} in a room%"  # lowercase
        cursor.execute(
            """
            SELECT rm.Room_ID, rt.Room_Description, rt.Price, rm.Available_Beds
            FROM Rooms rm
            JOIN RoomTypes rt ON rm.Room_Type=rt.TypeID
            WHERE LOWER(rt.Room_Description) LIKE %s
            ORDER BY rt.Price, rt.Hostel_ID;
            """,
            (pattern,)
        )
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching rooms: {e}")
        return []

def get_rooms_by_price_and_beds(min_price, max_price, min_beds, max_beds):
    connection = get_connection()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    try:
        # Create SQL conditions dynamically
        bed_conditions = " OR ".join(["LOWER(rt.Room_Description) LIKE %s" for _ in range(min_beds, max_beds + 1)])
        bed_patterns = [f"%{i} in a room%" for i in range(min_beds, max_beds + 1)]

        query = f"""
            SELECT rm.Room_ID, rt.Room_Description, rt.Price, rm.Available_Beds
            FROM Rooms rm
            JOIN RoomTypes rt ON rm.Room_Type = rt.TypeID
            WHERE rt.Price BETWEEN %s AND %s AND ({bed_conditions})
            ORDER BY rt.Price, rt.Hostel_ID;
        """

        cursor.execute(query, (min_price, max_price, *bed_patterns))
        return cursor.fetchall()

    except Exception as e:
        print(f"Error fetching combined filtered rooms: {e}")
        return []
    finally:
        cursor.close()
        connection.close()