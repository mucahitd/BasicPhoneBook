import pickle
import os


def DisplayMenu() -> None:
    print("1. List")
    print("2. Search")
    print("3. Add")
    print("4. Delete")
    print("5. Quit")
    print()


def MenuLoop() -> str:
    while True:
        DisplayMenu()
        option = input("Chosee (1-5): ")
        print("\n")
        if option.isdigit() and 1 <= int(option) <= 5:
            break
    return option


def MainLoop() -> None:
    while True:
        option = MenuLoop()
        if option == "1":
            ListRecords()
        elif option == "2":
            SearchRecord()
        elif option == "3":
            AddRecord()
        elif option == "4":
            DeleteRecord()
        elif option == "5":
            pass


def ListRecords() -> None:
    recordList = ReadFile()
    print(f"Total Contact: {len(recordList)}\n")
    print(f"{'Name':^10} {'Surname':^10} {'Phone':^11}")
    for record in recordList:
        print(f"{record.get('name', ' '):10.10} {record.get('surName', ' '):10.10} {record.get('telNumber', ' '):11.11}")
    print()


def SearchRecord() -> None:
    print("Search")
    name = input("Name: ?")
    surName = input("Surname: ?")
    recordList = SearchRecordFromFile(name, surName)
    print("Phone number : ", end='')
    for record in recordList:
        print(f"{record.get('telNumber'):11.11}", end='')
    print("\n")


def AddRecord() -> None:
    print("Add new contact")
    name = input("Name: ?")
    surName = input("Surname: ?")
    telNumber = input("Phone number: ?")
    print(f"Yeni kayıt: {name} {surName} - {telNumber}")
    if AreYouSure():
        AddRecordToFile(name, surName, telNumber)
        print("Added!\n")



def DeleteRecord() -> None:
    print("Delete record")
    name = input("Name: ?")
    surName = input("Surname: ?")
    recordList = SearchRecordFromFile(name, surName)
    print("Phone number : ", end='')
    for record in recordList:
        print(f"{record.get('telNumber'):11.11}", end='')
    print("\n")
    if AreYouSure():
        DeleteRecordsFromFile(recordList)
        print("Deleted\n")

def AreYouSure() -> bool:
    while True:
        answer = input("Are you sure ?  (Y)es/(H)ayır")
        print()
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False


def WriteFile(recordsListParam : list) -> None:
    with open("data.bin","wb") as fileObject:
        pickle.dump(recordsListParam,fileObject)


def ReadFile() -> list:
    if os.path.isfile("data.bin"):
        with open("data.bin", "rb") as fileObject:
            recordList = pickle.load(fileObject)
    else:
        recordList = list()

    return recordList


def SearchRecordFromFile(nameParam :str, surNameParam : str) -> list:
    recordList = ReadFile()
    responseList = list()
    for record in recordList:
        if record.get("name").upper() == nameParam and\
            record.get("surName").upper() == surNameParam:
            responseList.append(record)
    return responseList


def AddRecordToFile(nameParam : str, surNameParam : str, telNumberParam : str) -> None:
    recordList = ReadFile()
    recordDict = dict(name = nameParam, surName = surNameParam, telNumber = telNumberParam)
    recordList.append(recordDict)
    WriteFile(recordList)

def DeleteRecordsFromFile(recordsListParam : list) -> None:
    recordsList = ReadFile()
    for record in recordsList:
        for recordForDelete in recordsListParam:
            if record.get("name") == recordForDelete.get("name") and \
                record.get("surName") == recordForDelete.get("surName"):
                recordsList.remove(recordForDelete)
                continue
    WriteFile(recordsList)


MainLoop()
