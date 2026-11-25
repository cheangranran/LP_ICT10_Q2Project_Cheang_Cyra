
from pyscript import document

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "SE": ("Selenium", 34, 78.971),
    "F": ("Fluorine", 9, 18.998),
    "CL": ("Chlorine", 17, 35.45),
    "BR": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.90),
    "HE": ("Helium", 2, 4.0026),
    "NE": ("Neon", 10, 20.180),
    "AR": ("Argon", 18, 39.948),
    "KR": ("Krypton", 36, 83.798),
    "XE": ("Xenon", 54, 131.29),
    "RN": ("Radon", 86, 222)
}


def search_element(event=None):
    symbol = document.getElementById("symbol").value.strip().upper()

    element, atomic_number, atomic_mass = non_metals.get(
        symbol,
        ("Element not found", "-", "-")
    )

    document.getElementById("result").innerHTML = f"""
    <b>Result:</b><br>
    <b>Symbol:</b> {symbol}<br>
    <b>Element:</b> {element}<br>
    <b>Atomic Number:</b> {atomic_number}<br>
    <b>Atomic Mass:</b> {atomic_mass}<br>
    """