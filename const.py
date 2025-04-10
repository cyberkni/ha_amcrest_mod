"""Constants for amcrest component."""

DOMAIN = "amcrest_mod"
DATA_AMCREST = DOMAIN
CAMERAS = "cameras"
DEVICES = "devices"

BINARY_SENSOR_SCAN_INTERVAL_SECS = 5
CAMERA_WEB_SESSION_TIMEOUT = 10
COMM_RETRIES = 1
COMM_TIMEOUT = 6.05
SENSOR_SCAN_INTERVAL_SECS = 10
SNAPSHOT_TIMEOUT = 20

SERVICE_EVENT = "event"
SERVICE_UPDATE = "update"

RESOLUTION_LIST = {"high": 0, "low": 1}
RESOLUTION_TO_STREAM = {0: "Main", 1: "Extra"}
