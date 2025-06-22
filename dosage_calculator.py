# Simple drug dosage calculator (e.g. Paracetamol)
# 15 mg per kg body weight
weight = float(input("Enter patient's weight in kg: "))
dose_per_kg = 15  # you can change this per drug
total_dose = weight * dose_per_kg
print(f"Recommended dose: {total_dose} mg")
