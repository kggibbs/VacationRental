import mechanize
import re
import time

url = "https://parcel.sanjuanco.com/PropertyAccess/?cid=0"

fres = open("results-2019-20_20190515_A.txt", "w")

#with open("VacationRentalPermits_20190515.txt") as f:
with open("failedA.txt") as f:
    index = 0
    while 1:
        id = f.readline().rstrip()
        index += 1
        fres.write(f"processing {index},{id}\n")
        fres.flush()
        if index > 1070:
            break
        try:
            if id == "\n" or id == "":
                fres.write("id was null {index}\n")
                fres.flush()
                break
            else:
                time.sleep(1.0)
                brwsr = mechanize.Browser()
                brwsr.set_handle_robots(False)
                brwsr.open(url)
                brwsr.select_form(nr=0)
                brwsr["propertySearchOptions$geoid"] = id
                response = brwsr.submit()
                data = response.get_data()
                mch = re.search(r'<td align="right">\$([0-9]?,?[0-9]+,[0-9]+)</td>', data.decode("utf-8"))
                if mch:
                    val = int(mch.group(1).replace(",", ""))
                    fres.write(f"{index},{id},{val}\n")
                    fres.flush()
                else:
                    fres.write(f"nomatch {index},{id}\n")
                    fres.flush()
        except:
            fres.write(f"fetch failed at: {index},{id}\n")
            fres.flush()
