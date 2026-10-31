from pathlib import Path

filePath = Path("TestFolder")

imagesFolder = Path("TestFolder/Images")
imagesFolder.mkdir(exist_ok=True)

documentFolder = Path("TestFolder/Documents")
documentFolder.mkdir(exist_ok=True)

videosFolder = Path("TestFolder/Videos")
videosFolder.mkdir(exist_ok=True)

archivesFolder = Path("TestFolder/Archives")
archivesFolder.mkdir(exist_ok=True)



def organizeFiles(filePath):

    imageCount = 0
    documentCount = 0
    videoCount = 0
    archiveCount = 0
    unknownCount = 0
    totalCount = 0
    
    for item in filePath.iterdir():
        if(item.is_file()):
            extension = item.suffix.lower()
            if extension in ['.jpg', '.png', '.jpeg']:
                print(item.name + " - Images")
                destination = imagesFolder / item.name
                if destination.exists():
                    print("Item already exists.")
                    newName = f"{item.stem}_1{item.suffix}"
                    newDestination = imagesFolder / newName
                    nameCounter = 1
                    while newDestination.exists():
                        nameCounter += 1
                        newName = f"{item.stem}_{nameCounter}{item.suffix}"
                        newDestination = imagesFolder / newName  
                    item.rename(newDestination)
                    imageCount += 1
                    totalCount += 1
                else:
                    item.rename(destination)
                    imageCount += 1
                    totalCount += 1            
            elif extension in ['.pdf', '.txt','.docx']:
                print(item.name + " - Documents")
                destination = documentFolder / item.name
                if destination.exists():
                    print("Item already exists.")
                    newName = f"{item.stem}_1{item.suffix}"
                    newDestination = documentFolder / newName
                    nameCounter = 1
                    while newDestination.exists():
                        nameCounter += 1
                        newName = f"{item.stem}_{nameCounter}{item.suffix}"
                        newDestination = documentFolder / newName

                    item.rename(newDestination)
                    documentCount += 1
                    totalCount += 1
                else:
                    item.rename(destination)
                    documentCount += 1
                    totalCount += 1
            elif extension in ['.mp4', '.mov']:
                print(item.name + " - Videos")
                destination = videosFolder / item.name
                if destination.exists():
                    print("Item already exists.")
                    newName = f"{item.stem}_1{item.suffix}"
                    newDestination = videosFolder / newName
                    nameCounter = 1
                    while newDestination.exists():
                        nameCounter += 1
                        newName = f"{item.stem}_{nameCounter}{item.suffix}"
                        newDestination = videosFolder / newName

                    item.rename(newDestination)
                    videoCount += 1
                    totalCount += 1
                else:
                    item.rename(destination)
                    videoCount += 1
                    totalCount += 1
            elif extension in ['.zip', '.rar']:
                print(item.name + " - Archives")
                destination = archivesFolder / item.name
                if destination.exists():
                    print("Item already exists.")
                    newName = f"{item.stem}_1{item.suffix}"
                    newDestination = archivesFolder / newName
                    nameCounter = 1
                    while newDestination.exists():
                        nameCounter += 1
                        newName = f"{item.stem}_{nameCounter}{item.suffix}"
                        newDestination = archivesFolder / newName

                    item.rename(newDestination)
                    archiveCount += 1
                    totalCount += 1
                else:
                    item.rename(destination)
                    archiveCount += 1
                    totalCount += 1
            else:
                print(item.name + " - unknown file type")
                unknownCount += 1
                totalCount += 1

    return imageCount, documentCount, videoCount, archiveCount, unknownCount, totalCount        



imageCount, documentCount, videoCount, archiveCount, unknownCount, totalCount = organizeFiles(filePath)

print("File Organization Complete!")

print(f"Images organized: {imageCount}")
print(f"Documents organized: {documentCount}")
print(f"Videos organized: {videoCount}")
print(f"Archives organized: {archiveCount}")

