import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


# Initialize Nominatim API
geolocator = Nominatim(user_agent="fra")

billing_coordinates = []

def address():
    addresssData = pd.read_csv('./Source_Data/Customer_Address.txt', encoding='cp1252',dtype='str')
    addresssData.to_csv('./Source_Data/Customer_Address.csv', index=False)
    addresssData.sort_values(by="TRANS_ACCT_NUM")   
    riskData = pd.read_csv('./Source_Data/Fraud_Risk_Assessment.txt',dtype='str')
    riskData.to_csv('./Source_Data/Fraud_Risk_Assessment.csv', index=False)
    riskData.sort_values(by="TRANS_ACCT_NUM")
    riskData = pd.merge(riskData, addresssData, on="TRANS_ACCT_NUM")
    riskData.to_csv('./Source_Data/Fraud_Risk_Assessment.csv', index=False,)
    storeData = pd.read_csv("./Source_Data/Store_Addresses.txt",dtype='str')
    storeData.to_csv('./Source_Data/Store_Addresses.csv', index=False)
    riskData = pd.merge(riskData, storeData, left_on=" SALES_ID_LOC_STORE_NAME", right_on=" SALES_ID_LOC_STORE_NAME")
    riskData.to_csv('./Source_Data/Fraud_Risk_Assessment.csv', index=False)


def location():
    riskData = pd.read_csv('./Source_Data/Fraud_Risk_Assessment.csv',dtype='str')
    riskData["Full_Address"] = riskData["BILLING_ADDRESS_1"] + ", " + riskData["BILLING_ADDRESS_2"] + ", " + riskData["BILLING_ADDRESS_3"]
    riskData["Address"] = riskData["BILLING_ADDRESS_2"] + ", " + riskData["BILLING_ADDRESS_3"]
    riskData["Location"] = riskData["LATITUDE"] + ", " + riskData["LONGITUDE"]
    riskData.to_csv('./Source_Data/Fraud_Risk_Assessment.csv', index=False)


def geolocate():
    n=0
    riskData='./Source_Data/Fraud_Risk_Assessment.csv'
    #riskData = pd.read_csv('./Source_Data/Fraud_Risk_Assessment.csv')
    with open(riskData, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader)
        for row in datareader:
            location_1_raw = geolocator.geocode(row[32], timeout=None)
            if location_1_raw is None:
                location_1_raw = geolocator.geocode(row[33], timeout=None)
                location_1 = (location_1_raw.latitude, location_1_raw.longitude)
                miles = geodesic(location_1, row[34]).miles
                billing_coordinates.append(f"Miles: {miles:.2f}")
                print(f"Miles: {miles:.2f}")
                n+=1
                print(n)
            else:
                location_1_raw = geolocator.geocode(row[32], timeout=None)
                location_1 = (location_1_raw.latitude, location_1_raw.longitude)
                miles = geodesic(location_1, row[34]).miles
                billing_coordinates.append(f"Miles: {miles:.2f}")
                print(f"Miles: {miles:.2f}")
                n+=1
                print(n)

#address()
#location()
geolocate()

riskData = pd.read_csv('./Source_Data/Fraud_Risk_Assessment.csv',float_precision=None,dtype='str')
riskData["Distance"] = billing_coordinates
riskData.to_csv('./Source_Data/Fraud_Risk_Assessment.csv', index=False)
#write to excel
#riskData.to_excel("Fraud_Likely.xlsx", sheet_name="Fraud_Likely", index=False)























# location_1_raw = geolocator.geocode("Jackson, MS")
# location_1 = (location_1_raw.latitude, location_1_raw.longitude)
#print(location_1)

# location_2_raw = geolocator.geocode("Houston, TX")
# location_2 = (location_2_raw.latitude, location_2_raw.longitude)
#print(location_2)

#miles = geodesic(location_1, location_2).miles
#print(f"Miles: {miles:.2f}")








    #location_str = riskData["Full_Address"]
    # for i in riskData['Address']:
    #     for j in riskData['Location']:
    #         print(i, j)
    #         location_1_raw = geolocator.geocode(i, timeout=None)
    #         location_1 = (location_1_raw.latitude, location_1_raw.longitude)
    #         miles = geodesic(location_1, j).miles
    #         billing_coordinates.append("{miles:.2f}")
    #         billing_coordinates.append("{miles:.2f}")
    #         print(f"Miles: {miles:.2f}")
    #         n+=1
    #         print(n)



# location_no_str = i[51]
#         location_1_raw = geolocator.geocode(location_no_str)
#         location_1 = (location_1_raw.latitude, location_1_raw.longitude)
#         storeLocation = riskData[i]["Location"]
#         miles = geodesic(location_1, storeLocation).miles
#         print(f"Miles: {miles:.2f}")

    # location_1_raw = geolocator.geocode(location_no_str)
    # location_1 = (location_1_raw.latitude, location_1_raw.longitude)
    # miles = geodesic(location_1, riskData_location).miles
    # print(f"Miles: {miles:.2f}")
    # for value in riskData[" BILLING_ADDRESS_1"]:
    #     location = geolocator.geocode(value, timeout=500000)
    #     if value != "NoneType":
    #         billing_coordinates.append((location.longitude, location.latitude))

