import subprocess

# Comandos encadeados com if no PowerShell
comandos = """
cd code;
if ($?) { cd ch4-bookstore; }
if ($?) { docker-compose up -d --build; }
"""

# Executando no PowerShell
resultado = subprocess.run(["powershell", "-Command", comandos], capture_output=True, text=True)

# Saída
print("Saída:")
print(resultado.stdout)

if resultado.stderr:
    print("Erro:")
    print(resultado.stderr)
