import psutil
import time

def monitorar_rede(intervalo):
    while True:
        net_stats = psutil.net_io_counters()
        bytes_sent = net_stats.bytes_sent
        bytes_recv = net_stats.bytes_recv

        print("Bytes Sent: {}".format(bytes_sent))
        print("Bytes Received: {}".format(bytes_recv))

        time.sleep(intervalo)

monitorar_rede(5)  # Monitora a rede a cada 5 segundos
