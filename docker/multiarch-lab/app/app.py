import platform
import time

print("🚀 Aplicação iniciada")
print("Arquitetura:", platform.machine())

start = time.time()

# simula carga
for i in range(10_000_000):
    pass

end = time.time()

print("Tempo de execução:", end - start, "segundos")
