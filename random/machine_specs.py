import psutil

def get_ram_specs():
    ram = psutil.virtual_memory()
    return {
        'total': ram.total,
        'available': ram.available,
        'percent_used': ram.percent
    }

def get_cpu_specs():
    cpu = psutil.cpu_info()
    return {
        'cpu_model': cpu[0].model,
        'cpu_cores': psutil.cpu_count(logical=False),
        'cpu_threads': psutil.cpu_count(logical=True)
    }

def main():
    ram_specs = get_ram_specs()
    cpu_specs = get_cpu_specs()

    print("RAM Specifications:")
    print(f"Total RAM: {ram_specs['total'] / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {ram_specs['available'] / (1024 ** 3):.2f} GB")
    print(f"RAM Usage: {ram_specs['percent_used']}%")

    print("\nCPU Specifications:")
    print(f"CPU Model: {cpu_specs['cpu_model']}")
    print(f"Number of Cores: {cpu_specs['cpu_cores']}")
    print(f"Number of Threads: {cpu_specs['cpu_threads']}")

if __name__ == "__main__":
    main()
