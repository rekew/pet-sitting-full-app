import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_URI

def get_db_connection():
    return psycopg2.connect(DB_URI)

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    
   
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username VARCHAR(100),
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
   
    cur.execute('''
        CREATE TABLE IF NOT EXISTS nannies (
            user_id BIGINT PRIMARY KEY REFERENCES users(user_id),
            name VARCHAR(100) NOT NULL,
            city VARCHAR(100) NOT NULL,
            experience INTEGER NOT NULL,
            pet_types TEXT[] DEFAULT '{}',
            description TEXT,
            hourly_rate NUMERIC(10, 2),
            available BOOLEAN DEFAULT TRUE,
            rating NUMERIC(3, 2) DEFAULT 0.0,
            password VARCHAR(100) NOT NULL,
            CONSTRAINT experience_positive CHECK (experience >= 0)
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id SERIAL PRIMARY KEY,
            nanny_id BIGINT REFERENCES nannies(user_id),
            reviewer_id BIGINT REFERENCES users(user_id),
            rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
            comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
   
    cur.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id SERIAL PRIMARY KEY,
            owner_id BIGINT REFERENCES users(user_id),
            nanny_id BIGINT REFERENCES nannies(user_id),
            start_time TIMESTAMP NOT NULL,
            end_time TIMESTAMP NOT NULL,
            status VARCHAR(20) DEFAULT 'pending',
            pet_details TEXT,
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT valid_times CHECK (end_time > start_time)
        )
    ''')
    
    conn.commit()
    cur.close()
    conn.close()

def add_user(user_id, username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (user_id, username) VALUES (%s, %s) ON CONFLICT (user_id) DO NOTHING",
        (user_id, username)
    )
    conn.commit()
    cur.close()
    conn.close()

def add_nanny(user_id, nanny_data):
    conn = get_db_connection()
    cur = conn.cursor()
    

    cur.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))
    if not cur.fetchone():
       
        cur.execute(
            "INSERT INTO users (user_id, username) VALUES (%s, %s)",
            (user_id, nanny_data.get('name', 'Unknown'))
        )
    
   
    password = nanny_data.get('password', '1234')
    

    cur.execute(
        """
        INSERT INTO nannies (user_id, name, city, experience, pet_types, description, hourly_rate, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (user_id) DO UPDATE SET
            name = EXCLUDED.name,
            city = EXCLUDED.city,
            experience = EXCLUDED.experience,
            pet_types = EXCLUDED.pet_types,
            description = EXCLUDED.description,
            hourly_rate = EXCLUDED.hourly_rate
        """,
        (
            user_id, 
            nanny_data.get('name'), 
            nanny_data.get('city'), 
            nanny_data.get('experience'), 
            nanny_data.get('pet_types', []),
            nanny_data.get('description', ''),
            nanny_data.get('hourly_rate', 0),
            password
        )
    )
    
    conn.commit()
    cur.close()
    conn.close()

def get_nanny(user_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM nannies WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def get_all_nannies(city=None, pet_type=None, min_rating=None):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    query = "SELECT * FROM nannies WHERE available = TRUE"
    params = []
    
    if city:
        query += " AND LOWER(city) = LOWER(%s)"
        params.append(city)
    
    if pet_type:
        query += " AND %s = ANY(pet_types)"
        params.append(pet_type)
    
    if min_rating is not None:
        query += " AND rating >= %s"
        params.append(min_rating)
    
    query += " ORDER BY rating DESC, experience DESC"
    
    cur.execute(query, params)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def add_booking(owner_id, nanny_id, start_time, end_time, pet_details, address):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(
        """
        INSERT INTO bookings (owner_id, nanny_id, start_time, end_time, pet_details, address)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
        """,
        (owner_id, nanny_id, start_time, end_time, pet_details, address)
    )
    
    booking_id = cur.fetchone()['id']
    conn.commit()
    cur.close()
    conn.close()
    return booking_id

def update_booking_status(booking_id, status):
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute(
        "UPDATE bookings SET status = %s WHERE id = %s",
        (status, booking_id)
    )
    
    conn.commit()
    cur.close()
    conn.close()

def add_review(nanny_id, reviewer_id, rating, comment):
    conn = get_db_connection()
    cur = conn.cursor()
    
   
    cur.execute(
        """
        INSERT INTO reviews (nanny_id, reviewer_id, rating, comment)
        VALUES (%s, %s, %s, %s)
        """,
        (nanny_id, reviewer_id, rating, comment)
    )
    cur.execute(
        """
        UPDATE nannies
        SET rating = (
            SELECT AVG(rating) FROM reviews WHERE nanny_id = %s
        )
        WHERE user_id = %s
        """,
        (nanny_id, nanny_id)
    )
    
    conn.commit()
    cur.close()
    conn.close()

def verify_login(username, password):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(
        "SELECT user_id FROM nannies WHERE name = %s AND password = %s",
        (username, password)
    )
    
    result = cur.fetchone()
    cur.close()
    conn.close()
    
    return result['user_id'] if result else None

def get_nanny_bookings(nanny_id, status=None):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    query = """
        SELECT b.*, u.username as owner_name
        FROM bookings b
        JOIN users u ON b.owner_id = u.user_id
        WHERE b.nanny_id = %s
    """
    params = [nanny_id]
    
    if status:
        query += " AND b.status = %s"
        params.append(status)
    
    query += " ORDER BY b.start_time"
    
    cur.execute(query, params)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def get_owner_bookings(owner_id, status=None):
    
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    query = """
        SELECT b.*, n.name as nanny_name
        FROM bookings b
        JOIN nannies n ON b.nanny_id = n.user_id
        WHERE b.owner_id = %s
    """
    params = [owner_id]
    
    if status:
        query += " AND b.status = %s"
        params.append(status)
    
    query += " ORDER BY b.start_time"
    
    cur.execute(query, params)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
