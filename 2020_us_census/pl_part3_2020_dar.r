
# -----------------------------
# Specify path to part 3 file
# -----------------------------
part3_file_path <- "the location of the files on your computer\ms000032020.pl"

# -----------------------------
# Import the data
# -----------------------------
part3  <- read.delim(part3_file_path, header=FALSE, colClasses="character", sep="|")

# -----------------------------
# Assign names to data columns:
# -----------------------------
#  FILEID   File Identification
#  STUSAB   State/US-Abbreviation (USPS)
#  CHARITER Characteristic Iteration
#  CIFSN    Characteristic Iteration File Sequence Number
#  LOGRECNO Logical Record Number
#  P0050001 Total:
#  P0050002 Institutionalized population:
#  P0050003 Correctional facilities for adults
#  P0050004 Juvenile facilities
#  P0050005 Nursing facilities/Skilled-nursing facilities
#  P0050006 Other institutional facilities
#  P0050007 Noninstitutionalized population:
#  P0050008 College/University student housing
#  P0050009 Military quarters
#  P0050010 Other noninstitutional facilities
# -----------------------------
colnames(part3) <- c("FILEID", "STUSAB", "CHARITER", "CIFSN", "LOGRECNO",
                     paste0("P00", 50001:50010))