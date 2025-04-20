import json
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, BucketRetentionRules
from influxdb_client.client.write_api import SYNCHRONOUS

# MQTT settings
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "medical/+/vitals"

# InfluxDB settings
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "admintoken"
INFLUX_ORG = "medorg"
INFLUX_BUCKET = "medical"  # <--- Use single bucket

influx = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = influx.write_api(write_options=SYNCHRONOUS)
buckets_api = influx.buckets_api()

# Create "medical" bucket if it doesn't exist
def create_bucket_if_not_exists(bucket_name):
    existing = buckets_api.find_bucket_by_name(bucket_name)
    if not existing:
        buckets_api.create_bucket(bucket_name=bucket_name,
                                  retention_rules=BucketRetentionRules(type="infinite"),
                                  org=INFLUX_ORG)
        print(f"Created bucket: {bucket_name}")

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        patient_id = payload.get("patient_id")
        if not patient_id:
            return

        # Always use "medical" bucket
        create_bucket_if_not_exists(INFLUX_BUCKET)
        point = {
            "measurement": "vitals",
            "tags": {
                "patient_id": patient_id,
                "patient_name": payload.get("patient_name", "")
            },
            "fields": {
                "heart_rate": float(payload.get("heart_rate", 0)),
                "blood_pressure_systolic": int(payload.get("blood_pressure_systolic", 0)),
                "blood_pressure_diastolic": int(payload.get("blood_pressure_diastolic", 0)),
                "oxygen": float(payload.get("oxygen", 0)),
                "temperature": float(payload.get("temperature", 0)),
                "glucose": int(payload.get("glucose", 0)),
            }
        }

        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)

    except Exception as e:
        print("Error handling message:", e)

# Start MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()