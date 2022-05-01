
# -----------------------------
# Specify path to part 2 file
# -----------------------------
part2_file_path <- "the location of the files on your computer\ms000022020.pl"

# -----------------------------
# Import the data
# -----------------------------
part2  <- read.delim(part2_file_path, header=FALSE, colClasses="character", sep="|")

# -----------------------------
# Assign names to data columns:
# -----------------------------
#  FILEID    File Identification
#  STUSAB    State/US-Abbreviation (USPS)
#  CHARITER  Characteristic Iteration
#  CIFSN     Characteristic Iteration File Sequence Number
#  LOGRECNO  Logical Record Number
#  P0030001  P3-1: Total
#  P0030002  P3-2: Population of one race
#  P0030003  P3-3: White alone
#  P0030004  P3-4: Black or African American alone
#  P0030005  P3-5: American Indian and Alaska Native alone
#  P0030006  P3-6: Asian alone
#  P0030007  P3-7: Native Hawaiian and Other Pacific Islander alone
#  P0030008  P3-8: Some other race alone
#  P0030009  P3-9: Population of two or more races
#  P0030010  P3-10: Population of two races
#  P0030011  P3-11: White; Black or African American
#  P0030012  P3-12: White; American Indian and Alaska Native
#  P0030013  P3-13: White; Asian
#  P0030014  P3-14: White; Native Hawaiian and Other Pacific Islander
#  P0030015  P3-15: White; Some other race
#  P0030016  P3-16: Black or African American; American Indian and Alaska Native
#  P0030017  P3-17: Black or African American; Asian
#  P0030018  P3-18: Black or African American; Native Hawaiian and Other Pacific Islander
#  P0030019  P3-19: Black or African American; Some other race
#  P0030020  P3-20: American Indian and Alaska Native; Asian
#  P0030021  P3-21: American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0030022  P3-22: American Indian and Alaska Native; Some other race
#  P0030023  P3-23: Asian; Native Hawaiian and Other Pacific Islander
#  P0030024  P3-24: Asian; Some other race
#  P0030025  P3-25: Native Hawaiian and Other Pacific Islander; Some other race
#  P0030026  P3-26: Population of three races
#  P0030027  P3-27: White; Black or African American; American Indian and Alaska Native
#  P0030028  P3-28: White; Black or African American; Asian
#  P0030029  P3-29: White; Black or African American; Native Hawaiian and Other Pacific Islander
#  P0030030  P3-30: White; Black or African American; Some other race
#  P0030031  P3-31: White; American Indian and Alaska Native; Asian
#  P0030032  P3-32: White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0030033  P3-33: White; American Indian and Alaska Native; Some other race
#  P0030034  P3-34: White; Asian; Native Hawaiian and Other Pacific Islander
#  P0030035  P3-35: White; Asian; Some other race
#  P0030036  P3-36: White; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030037  P3-37: Black or African American; American Indian and Alaska Native; Asian
#  P0030038  P3-38: Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0030039  P3-39: Black or African American; American Indian and Alaska Native; Some other race
#  P0030040  P3-40: Black or African American; Asian; Native Hawaiian and Other Pacific Islander
#  P0030041  P3-41: Black or African American; Asian; Some other race
#  P0030042  P3-42: Black or African American; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030043  P3-43: American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0030044  P3-44: American Indian and Alaska Native; Asian; Some other race
#  P0030045  P3-45: American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030046  P3-46: Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030047  P3-47: Population of four races
#  P0030048  P3-48: White; Black or African American; American Indian and Alaska Native; Asian
#  P0030049  P3-49: White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0030050  P3-50: White; Black or African American; American Indian and Alaska Native; Some other race
#  P0030051  P3-51: White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander
#  P0030052  P3-52: White; Black or African American; Asian; Some other race
#  P0030053  P3-53: White; Black or African American; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030054  P3-54: White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0030055  P3-55: White; American Indian and Alaska Native; Asian; Some other race
#  P0030056  P3-56: White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030057  P3-57: White; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030058  P3-58: Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0030059  P3-59: Black or African American; American Indian and Alaska Native; Asian; Some other race
#  P0030060  P3-60: Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030061  P3-61: Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030062  P3-62: American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030063  P3-63: Population of five races
#  P0030064  P3-64: White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0030065  P3-65: White; Black or African American; American Indian and Alaska Native; Asian; Some other race
#  P0030066  P3-66: White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030067  P3-67: White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030068  P3-68: White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030069  P3-69: Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0030070  P3-70: Population of six races
#  P0030071  P3-71: White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040001  P4-1: Total
#  P0040002  P4-2: Hispanic or Latino
#  P0040003  P4-3: Not Hispanic or Latino
#  P0040004  P4-4: Population of one race
#  P0040005  P4-5: White alone
#  P0040006  P4-6: Black or African American alone
#  P0040007  P4-7: American Indian and Alaska Native alone
#  P0040008  P4-8: Asian alone
#  P0040009  P4-9: Native Hawaiian and Other Pacific Islander alone
#  P0040010  P4-10: Some other race alone
#  P0040011  P4-11: Population of two or more races
#  P0040012  P4-12: Population of two races
#  P0040013  P4-13: White; Black or African American
#  P0040014  P4-14: White; American Indian and Alaska Native
#  P0040015  P4-15: White; Asian
#  P0040016  P4-16: White; Native Hawaiian and Other Pacific Islander
#  P0040017  P4-17: White; Some other race
#  P0040018  P4-18: Black or African American; American Indian and Alaska Native
#  P0040019  P4-19: Black or African American; Asian
#  P0040020  P4-20: Black or African American; Native Hawaiian and Other Pacific Islander
#  P0040021  P4-21: Black or African American; Some other race
#  P0040022  P4-22: American Indian and Alaska Native; Asian
#  P0040023  P4-23: American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0040024  P4-24: American Indian and Alaska Native; Some other race
#  P0040025  P4-25: Asian; Native Hawaiian and Other Pacific Islander
#  P0040026  P4-26: Asian; Some other race
#  P0040027  P4-27: Native Hawaiian and Other Pacific Islander; Some other race
#  P0040028  P4-28: Population of three races
#  P0040029  P4-29: White; Black or African American; American Indian and Alaska Native
#  P0040030  P4-30: White; Black or African American; Asian
#  P0040031  P4-31: White; Black or African American; Native Hawaiian and Other Pacific Islander
#  P0040032  P4-32: White; Black or African American; Some other race
#  P0040033  P4-33: White; American Indian and Alaska Native; Asian
#  P0040034  P4-34: White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0040035  P4-35: White; American Indian and Alaska Native; Some other race
#  P0040036  P4-36: White; Asian; Native Hawaiian and Other Pacific Islander
#  P0040037  P4-37: White; Asian; Some other race
#  P0040038  P4-38: White; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040039  P4-39: Black or African American; American Indian and Alaska Native; Asian
#  P0040040  P4-40: Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0040041  P4-41: Black or African American; American Indian and Alaska Native; Some other race
#  P0040042  P4-42: Black or African American; Asian; Native Hawaiian and Other Pacific Islander
#  P0040043  P4-43: Black or African American; Asian; Some other race
#  P0040044  P4-44: Black or African American; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040045  P4-45: American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0040046  P4-46: American Indian and Alaska Native; Asian; Some other race
#  P0040047  P4-47: American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040048  P4-48: Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040049  P4-49: Population of four races
#  P0040050  P4-50: White; Black or African American; American Indian and Alaska Native; Asian
#  P0040051  P4-51: White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0040052  P4-52: White; Black or African American; American Indian and Alaska Native; Some other race
#  P0040053  P4-53: White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander
#  P0040054  P4-54: White; Black or African American; Asian; Some other race
#  P0040055  P4-55: White; Black or African American; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040056  P4-56: White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0040057  P4-57: White; American Indian and Alaska Native; Asian; Some other race
#  P0040058  P4-58: White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040059  P4-59: White; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040060  P4-60: Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0040061  P4-61: Black or African American; American Indian and Alaska Native; Asian; Some other race
#  P0040062  P4-62: Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040063  P4-63: Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040064  P4-64: American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040065  P4-65: Population of five races
#  P0040066  P4-66: White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0040067  P4-67: White; Black or African American; American Indian and Alaska Native; Asian; Some other race
#  P0040068  P4-68: White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040069  P4-69: White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040070  P4-70: White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040071  P4-71: Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  P0040072  P4-72: Population of six races
#  P0040073  P4-73: White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some other race
#  H0010001  H1-1: Total
#  H0010002  H1-2: Occupied
#  H0010003  H1-3: Vacant
# -----------------------------
colnames(part2) <- c("FILEID", "STUSAB", "CHARITER", "CIFSN", "LOGRECNO", 
                     paste0("P00", c(30001:30071, 40001:40073)), 
                     paste0("H00", 10001:10003))