def detect_ddos(requests):
    threshold = 50

    if requests > threshold:
        print("⚠️ Possible DDoS Attack Detected!")
    else:
        print("Normal Traffic")

detect_ddos(80)