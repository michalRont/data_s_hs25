import ifcopenshell
import pandas as pd
import os
import sqlite3

# Load the IFC file
ifc_file_path = r"C:\Users\MichalRontsinsky\OneDrive - beyondBIM\PERSONAL\PROJEKTE\HSLU\Nest_Modell\ARC_Modell_NEST_Räume.ifc"

dir_path = r"C:\Users\MichalRontsinsky\OneDrive - beyondBIM\Dokumente\VS_Projects\HSLU_Data_2_FS"
db_export_path = f"{dir_path}/ifc_data.db"
ifc_file = ifcopenshell.open(ifc_file_path)

# Get all IfcElements or IfcProducts
#elements = ifc_file.by_type("IfcElement") + ifc_file.by_type("IfcProduct")
elements = ifc_file.by_type("IfcSpace")

# Dictionary to store extracted data
data = []

# Collect all unique PropertySet and Property names
all_properties = set()
for element in elements:
    if element.IsDefinedBy:
        for rel in element.IsDefinedBy:
            if hasattr(rel, "RelatingPropertyDefinition"):
                prop_def = rel.RelatingPropertyDefinition
                if prop_def.is_a("IfcPropertySet"):
                    for prop in prop_def.HasProperties:
                        all_properties.add(f"{prop_def.Name}:{prop.Name}")

# Convert set to sorted list for consistent ordering
all_properties = sorted(all_properties)

# Extract data for each element
for element in elements:
    row = {
        "GUID": element.GlobalId,
        "IfcClass": element.is_a()
    }
    
    # Initialize all property columns with empty string
    for prop in all_properties:
        row[prop] = ""
    
    if element.IsDefinedBy:
        for rel in element.IsDefinedBy:
            if hasattr(rel, "RelatingPropertyDefinition"):
                prop_def = rel.RelatingPropertyDefinition
                if prop_def.is_a("IfcPropertySet"):
                    for prop in prop_def.HasProperties:
                        col_name = f"{prop_def.Name}:{prop.Name}"
                        if hasattr(prop, "NominalValue"):
                            value = prop.NominalValue.wrappedValue
                            if "m²" in str(value):
                                value = float(str(value).replace("m²", "").strip())

                        else:
                            value = str(prop)
                        row[col_name] = value
    
    data.append(row)

# Convert to DataFrame and export to Excel
df = pd.DataFrame(data)


conn = sqlite3.connect(db_export_path)

df.to_sql("spaces_nest", conn, if_exists="replace", index=False)

query = "SELECT * FROM spaces_nest"
df_from_db = pd.read_sql(query, conn)
print(df_from_db)
conn.close()

