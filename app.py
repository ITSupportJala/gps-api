from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Ganti ini dengan info database kamu
db_config = {
    'host': 'sql12.freesqldatabase.com',
    'user': 'sql12785001',
    'password': 'vbRCZFn5e6',
    'database': 'sql12785001'
}

@app.route('/api/gps-data', methods=['POST'])
def receive_data():
    data = request.get_json()

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = """
            INSERT INTO gps_data (
                VehicleId, VehicleNumber, DatetimeUTC, GpsLocation,
                Lon, Lat, Speed, Direction, Engine,
                Odometer, Car_Status, VehicleType
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data.get("VehicleId"),
            data.get("VehicleNumber"),
            data.get("DatetimeUTC"),
            data.get("GpsLocation"),
            data.get("Lon"),
            data.get("Lat"),
            data.get("Speed"),
            data.get("Direction"),
            data.get("Engine"),
            data.get("Odometer"),
            data.get("Car_Status"),
            data.get("VehicleType"),
        )

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Data saved successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/')
def home():
    return 'GPS API is running!'

app.run(host='0.0.0.0', port=8080)
