"""Generate a sample .xlsx from this directory. Run: python generate.py"""
from xlsxwriter import Workbook
from pathlib import Path

out = Path(__file__).resolve().parent / "output.xlsx"
wb = Workbook(str(out))
ws = wb.add_worksheet("Data")
bold = wb.add_format({"bold": True})
ws.write(0, 0, "Name", bold)
ws.write(0, 1, "Value", bold)
ws.write(1, 0, "Example")
ws.write(1, 1, 42)
wb.close()
print("Wrote", out)
