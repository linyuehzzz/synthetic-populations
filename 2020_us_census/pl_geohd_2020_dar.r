
# -----------------------------
# Specify path to header file
# -----------------------------
header_file_path <- "the location of the files on your computer\msgeo2020.pl"

# -----------------------------
# Import the data
# -----------------------------
header <- read.delim(header_file_path, header=FALSE, colClasses="character", sep="|")

# -----------------------------
# Assign names to data columns
# -----------------------------
#  FILEID        File Identification 
#  STUSAB        State/US-Abbreviation (USPS) 
#  SUMLEV        Summary Level 
#  GEOVAR        Geographic Variant 
#  GEOCOMP       Geographic Component 
#  CHARITER      Characteristic Iteration 
#  CIFSN         Characteristic Iteration File Sequence Number 
#  LOGRECNO      Logical Record Number 
#  GEOID         Geographic Record Identifier 
#  GEOCODE       Geographic Code Identifier 
#  REGION        Region 
#  DIVISION      Division 
#  STATE         State (FIPS) 
#  STATENS       State (NS) 
#  COUNTY        County (FIPS) 
#  COUNTYCC      FIPS County Class Code 
#  COUNTYNS      County (NS) 
#  COUSUB        County Subdivision (FIPS) 
#  COUSUBCC      FIPS County Subdivision Class Code 
#  COUSUBNS      County Subdivision (NS) 
#  SUBMCD        Subminor Civil Division (FIPS) 
#  SUBMCDCC      FIPS Subminor Civil Division Class Code 
#  SUBMCDNS      Subminor Civil Division (NS) 
#  ESTATE        Estate (FIPS) 
#  ESTATECC      FIPS Estate Class Code 
#  ESTATENS      Estate (NS) 
#  CONCIT        Consolidated City (FIPS) 
#  CONCITCC      FIPS Consolidated City Class Code 
#  CONCITNS      Consolidated City (NS) 
#  PLACE         Place (FIPS) 
#  PLACECC       FIPS Place Class Code 
#  PLACENS       Place (NS) 
#  TRACT         Census Tract 
#  BLKGRP        Block Group 
#  BLOCK         Block 
#  AIANHH        American Indian Area/Alaska Native Area/Hawaiian Home Land (Census) 
#  AIHHTLI       American Indian Trust Land/Hawaiian Home Land Indicator 
#  AIANHHFP      American Indian Area/Alaska Native Area/Hawaiian Home Land (FIPS) 
#  AIANHHCC      FIPS American Indian Area/Alaska Native Area/Hawaiian Home Land Class Code 
#  AIANHHNS      American Indian Area/Alaska Native Area/Hawaiian Home Land (NS) 
#  AITS          American Indian Tribal Subdivision (Census) 
#  AITSFP        American Indian Tribal Subdivision (FIPS) 
#  AITSCC        FIPS American Indian Tribal Subdivision Class Code 
#  AITSNS        American Indian Tribal Subdivision (NS) 
#  TTRACT        Tribal Census Tract 
#  TBLKGRP       Tribal Block Group 
#  ANRC          Alaska Native Regional Corporation (FIPS) 
#  ANRCCC        FIPS Alaska Native Regional Corporation Class Code 
#  ANRCNS        Alaska Native Regional Corporation (NS) 
#  CBSA          Metropolitan Statistical Area/Micropolitan Statistical Area 
#  MEMI          Metropolitan/Micropolitan Indicator 
#  CSA           Combined Statistical Area 
#  METDIV        Metropolitan Division 
#  NECTA         New England City and Town Area 
#  NMEMI         NECTA Metropolitan/Micropolitan Indicator 
#  CNECTA        Combined New England City and Town Area 
#  NECTADIV      New England City and Town Area Division 
#  CBSAPCI       Metropolitan Statistical Area/Micropolitan Statistical Area Principal City Indicator 
#  NECTAPCI      New England City and Town Area Principal City Indicator 
#  UA            Urban Area 
#  UATYPE        Urban Area Type 
#  UR            Urban/Rural 
#  CD116         Congressional District (116th) 
#  CD118         Congressional District (118th) 
#  CD119         Congressional District (119th) 
#  CD120         Congressional District (120th) 
#  CD121         Congressional District (121st) 
#  SLDU18        State Legislative District (Upper Chamber) (2018) 
#  SLDU22        State Legislative District (Upper Chamber) (2022) 
#  SLDU24        State Legislative District (Upper Chamber) (2024) 
#  SLDU26        State Legislative District (Upper Chamber) (2026) 
#  SLDU28        State Legislative District (Upper Chamber) (2028) 
#  SLDL18        State Legislative District (Lower Chamber) (2018) 
#  SLDL22        State Legislative District (Lower Chamber) (2022) 
#  SLDL24        State Legislative District (Lower Chamber) (2024) 
#  SLDL26        State Legislative District (Lower Chamber) (2026) 
#  SLDL28        State Legislative District (Lower Chamber) (2028) 
#  VTD           Voting District 
#  VTDI          Voting District Indicator 
#  ZCTA          ZIP Code Tabulation Area (5-Digit) 
#  SDELM         School District (Elementary) 
#  SDSEC         School District (Secondary) 
#  SDUNI         School District (Unified) 
#  PUMA          Public Use Microdata Area 
#  AREALAND      Area (Land) 
#  AREAWATR      Area (Water) 
#  BASENAME      Area Base Name 
#  NAME          Area Name-Legal/Statistical Area Description (LSAD) Term-Part Indicator 
#  FUNCSTAT      Functional Status Code 
#  GCUNI         Geographic Change User Note Indicator 
#  POP100        Population Count (100%) 
#  HU100         Housing Unit Count (100%) 
#  INTPTLAT      Internal Point (Latitude) 
#  INTPTLON      Internal Point (Longitude) 
#  LSADC         Legal/Statistical Area Description Code 
#  PARTFLAG      Part Flag 
#  UGA           Urban Growth Area 
# -----------------------------
colnames(header) <- c("FILEID", "STUSAB", "SUMLEV", "GEOVAR", "GEOCOMP", "CHARITER", "CIFSN", "LOGRECNO", "GEOID", 
                      "GEOCODE", "REGION", "DIVISION", "STATE", "STATENS", "COUNTY", "COUNTYCC", "COUNTYNS", "COUSUB",
                      "COUSUBCC", "COUSUBNS", "SUBMCD", "SUBMCDCC", "SUBMCDNS", "ESTATE", "ESTATECC", "ESTATENS", 
                      "CONCIT", "CONCITCC", "CONCITNS", "PLACE", "PLACECC", "PLACENS", "TRACT", "BLKGRP", "BLOCK", 
                      "AIANHH", "AIHHTLI", "AIANHHFP", "AIANHHCC", "AIANHHNS", "AITS", "AITSFP", "AITSCC", "AITSNS",
                      "TTRACT", "TBLKGRP", "ANRC", "ANRCCC", "ANRCNS", "CBSA", "MEMI", "CSA", "METDIV", "NECTA",
                      "NMEMI", "CNECTA", "NECTADIV", "CBSAPCI", "NECTAPCI", "UA", "UATYPE", "UR", "CD116", "CD118",
                      "CD119", "CD120", "CD121", "SLDU18", "SLDU22", "SLDU24", "SLDU26", "SLDU28", "SLDL18", "SLDL22",
                      "SLDL24", "SLDL26", "SLDL28", "VTD", "VTDI", "ZCTA", "SDELM", "SDSEC", "SDUNI", "PUMA", "AREALAND",
                      "AREAWATR", "BASENAME", "NAME", "FUNCSTAT", "GCUNI", "POP100", "HU100", "INTPTLAT", "INTPTLON", 
                      "LSADC", "PARTFLAG", "UGA")