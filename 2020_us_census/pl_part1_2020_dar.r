
# -----------------------------
# Specify path to part 1 file
# -----------------------------
part1_file_path <- "the location of the files on your computer\ms000012020.pl"

# -----------------------------
# Import the data
# -----------------------------
part1  <- read.delim(part1_file_path, header=FALSE, colClasses="character", sep="|")

# -----------------------------
# Assign names to data columns
# -----------------------------
#  FILEID    File Identification
#  STUSAB    State/US-Abbreviation (USPS)
#  CHARITER  Characteristic Iteration
#  CIFSN     Characteristic Iteration File Sequence Number
#  LOGRECNO  Logical Record Number
#  P0010001  Total:
#  P0010002  Population of one race:
#  P0010003  White alone
#  P0010004  Black or African American alone
#  P0010005  American Indian and Alaska Native alone
#  P0010006  Asian alone
#  P0010007  Native Hawaiian and Other Pacific Islander alone
#  P0010008  Some Other Race alone
#  P0010009  Population of two or more races:
#  P0010010  Population of two races:
#  P0010011  White; Black or African American
#  P0010012  White; American Indian and Alaska Native
#  P0010013  White; Asian
#  P0010014  White; Native Hawaiian and Other Pacific Islander
#  P0010015  White; Some Other Race
#  P0010016  Black or African American; American Indian and Alaska Native
#  P0010017  Black or African American; Asian
#  P0010018  Black or African American; Native Hawaiian and Other Pacific Islander
#  P0010019  Black or African American; Some Other Race
#  P0010020  American Indian and Alaska Native; Asian
#  P0010021  American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0010022  American Indian and Alaska Native; Some Other Race
#  P0010023  Asian; Native Hawaiian and Other Pacific Islander
#  P0010024  Asian; Some Other Race
#  P0010025  Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010026  Population of three races:
#  P0010027  White; Black or African American; American Indian and Alaska Native
#  P0010028  White; Black or African American; Asian
#  P0010029  White; Black or African American; Native Hawaiian and Other Pacific Islander
#  P0010030  White; Black or African American; Some Other Race
#  P0010031  White; American Indian and Alaska Native; Asian
#  P0010032  White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0010033  White; American Indian and Alaska Native; Some Other Race
#  P0010034  White; Asian; Native Hawaiian and Other Pacific Islander
#  P0010035  White; Asian; Some Other Race
#  P0010036  White; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010037  Black or African American; American Indian and Alaska Native; Asian
#  P0010038  Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0010039  Black or African American; American Indian and Alaska Native; Some Other Race
#  P0010040  Black or African American; Asian; Native Hawaiian and Other Pacific Islander
#  P0010041  Black or African American; Asian; Some Other Race
#  P0010042  Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010043  American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0010044  American Indian and Alaska Native; Asian; Some Other Race
#  P0010045  American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010046  Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010047  Population of four races:
#  P0010048  White; Black or African American; American Indian and Alaska Native; Asian
#  P0010049  White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0010050  White; Black or African American; American Indian and Alaska Native; Some Other Race
#  P0010051  White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander
#  P0010052  White; Black or African American; Asian; Some Other Race
#  P0010053  White; Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010054  White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0010055  White; American Indian and Alaska Native; Asian; Some Other Race
#  P0010056  White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010057  White; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010058  Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0010059  Black or African American; American Indian and Alaska Native; Asian; Some Other Race
#  P0010060  Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010061  Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010062  American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010063  Population of five races:
#  P0010064  White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0010065  White; Black or African American; American Indian and Alaska Native; Asian; Some Other Race
#  P0010066  White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010067  White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010068  White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010069  Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0010070  Population of six races:
#  P0010071  White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020001  Total:
#  P0020002  Hispanic or Latino
#  P0020003  Not Hispanic or Latino:
#  P0020004  Population of one race:
#  P0020005  White alone
#  P0020006  Black or African American alone
#  P0020007  American Indian and Alaska Native alone
#  P0020008  Asian alone
#  P0020009  Native Hawaiian and Other Pacific Islander alone
#  P0020010  Some Other Race alone
#  P0020011  Population of two or more races:
#  P0020012  Population of two races:
#  P0020013  White; Black or African American
#  P0020014  White; American Indian and Alaska Native
#  P0020015  White; Asian
#  P0020016  White; Native Hawaiian and Other Pacific Islander
#  P0020017  White; Some Other Race
#  P0020018  Black or African American; American Indian and Alaska Native
#  P0020019  Black or African American; Asian
#  P0020020  Black or African American; Native Hawaiian and Other Pacific Islander
#  P0020021  Black or African American; Some Other Race
#  P0020022  American Indian and Alaska Native; Asian
#  P0020023  American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0020024  American Indian and Alaska Native; Some Other Race
#  P0020025  Asian; Native Hawaiian and Other Pacific Islander
#  P0020026  Asian; Some Other Race
#  P0020027  Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020028  Population of three races:
#  P0020029  White; Black or African American; American Indian and Alaska Native
#  P0020030  White; Black or African American; Asian
#  P0020031  White; Black or African American; Native Hawaiian and Other Pacific Islander
#  P0020032  White; Black or African American; Some Other Race
#  P0020033  White; American Indian and Alaska Native; Asian
#  P0020034  White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0020035  White; American Indian and Alaska Native; Some Other Race
#  P0020036  White; Asian; Native Hawaiian and Other Pacific Islander
#  P0020037  White; Asian; Some Other Race
#  P0020038  White; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020039  Black or African American; American Indian and Alaska Native; Asian
#  P0020040  Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0020041  Black or African American; American Indian and Alaska Native; Some Other Race
#  P0020042  Black or African American; Asian; Native Hawaiian and Other Pacific Islander
#  P0020043  Black or African American; Asian; Some Other Race
#  P0020044  Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020045  American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0020046  American Indian and Alaska Native; Asian; Some Other Race
#  P0020047  American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020048  Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020049  Population of four races:
#  P0020050  White; Black or African American; American Indian and Alaska Native; Asian
#  P0020051  White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander
#  P0020052  White; Black or African American; American Indian and Alaska Native; Some Other Race
#  P0020053  White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander
#  P0020054  White; Black or African American; Asian; Some Other Race
#  P0020055  White; Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020056  White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0020057  White; American Indian and Alaska Native; Asian; Some Other Race
#  P0020058  White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020059  White; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020060  Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0020061  Black or African American; American Indian and Alaska Native; Asian; Some Other Race
#  P0020062  Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020063  Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020064  American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020065  Population of five races:
#  P0020066  White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander
#  P0020067  White; Black or African American; American Indian and Alaska Native; Asian; Some Other Race
#  P0020068  White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020069  White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020070  White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020071  Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
#  P0020072  Population of six races:
#  P0020073  White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race
# -----------------------------
colnames(part1) <- c("FILEID", "STUSAB", "CHARITER", "CIFSN", "LOGRECNO", 
                     paste0("P00", c(10001:10071, 20001:20073)))