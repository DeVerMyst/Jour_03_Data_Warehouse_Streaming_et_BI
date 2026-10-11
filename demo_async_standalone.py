import time
import asyncio
import aiohttp
import requests

# Simulation de 10 requetes API distantes avec 100 ms de latence chacune
URLS = [f"https://httpbin.org/delay/0.1" for _ in range(10)]

def run_synchronous():
    print("\n--- 1. APPROCHE SYNCHRONE (Bloquante) ---")
    t0 = time.time()
    for i, url in enumerate(URLS, 1):
        resp = requests.get(url)
        print(f"  [Sync] Requete {i}/10 terminee (Code {resp.status_code})")
    total_time = time.time() - t0
    print(f"Temps total synchrone : {total_time:.2f} secondes")
    return total_time

async def fetch_one(session, url, idx):
    async with session.get(url) as response:
        data = await response.json()
        print(f"  [Async] Requete {idx}/10 recue !")
        return data

async def run_asynchronous():
    print("\n--- 2. APPROCHE ASYNCHRONE (Non-bloquante / Concurrente) ---")
    t0 = time.time()
    async with aiohttp.ClientSession() as session:
        # Lancement de toutes les coroutines en parallele sur l'Event Loop
        tasks = [fetch_one(session, url, i) for i, url in enumerate(URLS, 1)]
        results = await asyncio.gather(*tasks)
    total_time = time.time() - t0
    print(f"Temps total asynchrone : {total_time:.2f} secondes")
    return total_time

if __name__ == "__main__":
    print("=" * 60)
    print("DEMO SCRIPT PYTHON (.py) : SYNCHRONE VS ASYNCHRONE")
    print("Dans un fichier .py, on utilise imperativement : asyncio.run(...)")
    print("=" * 60)

    # 1. Test synchrone
    sync_duration = run_synchronous()

    # 2. Test asynchrone (avec le point d'entree standard asyncio.run)
    async_duration = asyncio.run(run_asynchronous())

    print("\n" + "=" * 60)
    print(f"Bilan : L'asynchrone est {sync_duration / async_duration:.1f} fois plus rapide !")
    print("=" * 60)
