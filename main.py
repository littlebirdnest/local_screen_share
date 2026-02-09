from flask import Flask, Response
import cv2
import mss
import numpy as np
import socket

app = Flask(__name__)

def generate_frames():
    """
    Generator function that captures the screen and yields JPEG frames.
    """
    # [Important] Initialize mss inside the function context.
    # Flask is multi-threaded, and mss is not thread-safe if initialized globally.
    # Creating a new instance per request ensures thread safety.
    with mss.mss() as sct:
        # Select the first monitor. 
        # Check 'sct.monitors' to see available screens.
        monitor = sct.monitors[1]
        
        while True:
            try:
                # 1. Capture the screen (returns raw pixels)
                img = sct.grab(monitor)
                
                # 2. Convert to numpy array for OpenCV processing
                frame = np.array(img)
                
                # 3. Color Space Conversion
                # MSS returns BGRA (Blue, Green, Red, Alpha).
                # OpenCV uses BGR. We drop the Alpha channel here.
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                
                # [Optional] Resize frame to reduce bandwidth usage
                # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

                # 4. Compression
                # Encode the frame as JPEG. 
                # '50' is the quality (0-100). Lower means smaller size & lower latency.
                ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                frame_bytes = buffer.tobytes()

                # 5. Yield the frame in MJPEG format
                # The boundary '--frame' separates individual JPEG images.
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            
            except Exception as e:
                print(f"[Error] Screen capture failed: {e}")
                break

@app.route('/')
def index():
    """
    Route to stream the screen.
    Browser treats this as a continuous video stream due to the mimetype.
    """
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def get_local_ip():
    """
    Helper function to find the local IP address.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Doesn't need to be reachable
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

if __name__ == '__main__':
    # Print access instructions
    local_ip = get_local_ip()
    port = 5000
    print(f"\n[+] Server started successfully!")
    print(f"[-] Local Access:   http://127.0.0.1:{port}")
    print(f"[-] Network Access: http://{local_ip}:{port}")
    print(f"[-] Press CTRL+C to stop.\n")

    # 'host=0.0.0.0' exposes the server to the local network.
    # 'threaded=True' handles multiple viewers simultaneously.
    app.run(host='0.0.0.0', port=port, threaded=True)
